import pytest
from base.get_driver import GetDriver
from page.page_login import PageLogin
from tool.read_json import read_json
import logging
import allure
# from allure import severity

# 配置日志
logger = logging.getLogger()
logger.setLevel(logging.INFO)
sh = logging.StreamHandler()
logger.addHandler(sh)

# 获取测试数据
def get_data():
    arrs = []
    for data in read_json("login.json").values():
        arrs.append((
            data.get("username"),
            data.get("password"),
            data.get("expect_result")
        ))
    return arrs

# 使用pytest重写测试类
@allure.epic("登录测试")
@allure.feature("登录功能")
# @allure.severity("critical")  # 为整个类设置严重性级别
class TestLogin:
    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self, request):
        """类级别初始化，整个测试类只执行一次"""
        # 获取驱动
        driver = GetDriver().get_driver()
        # 实例化页面对象
        login_page = PageLogin(driver)
        # 点击登录链接
        login_page.page_click_login_link()
        logger.info("测试类初始化完成")

        # 将driver和login_page绑定到类实例上
        request.cls.driver = driver
        request.cls.login_page = login_page

        # 测试类结束时的清理
        yield
        # 关闭驱动
        GetDriver().quit_driver()
        logger.info("测试类清理完成")

    @allure.story("登录功能验证")
    @allure.title("测试登录功能 - {username}/{password} 期望结果: {expect_result}")
    @pytest.mark.parametrize("username,password,expect_result", get_data())
    def test_login(self, username, password, expect_result):
        """登录测试方法"""
        with allure.step("执行登录操作"):
            self.login_page.page_login(username, password)

        with allure.step("获取错误信息并验证"):
            # 获取实际结果
            actual_result = self.login_page.page_get_error_info()

            # 添加截图到Allure报告
            # if actual_result != expect_result:
            # allure.attach(
            #     self.login_page.page_get_img(),
            #     name=f"login_failure_{username}",
            #     attachment_type=allure.attachment_type.PNG
            # )
            # 确保在断言失败时才尝试截图
            if actual_result != expect_result:
                try:
                    # 检查浏览器是否仍然有效
                    if self.driver.service.is_connectable():
                        screenshot = self.driver.get_screenshot_as_png()
                        if screenshot:  # 确保截图不为空
                            allure.attach(
                                screenshot,
                                name=f"login_failure_{username}",
                                attachment_type=allure.attachment_type.PNG
                            )
                        else:
                            logger.warning("截图返回空数据")
                    else:
                        logger.warning("浏览器已断开连接，无法截图")
                except Exception as e:
                    logger.error(f"截图失败: {str(e)}")

            assert actual_result == expect_result, \
                f"期望: {expect_result}, 实际: {actual_result}"

            # 使用pytest断言
            assert actual_result == expect_result, \
                f"登录验证失败: 期望结果 '{expect_result}', 实际结果 '{actual_result}'"

            # 记录日志
            logger.info(
                f"测试完成: 用户名={username}, 密码={password}, 期望结果={expect_result}, 实际结果={actual_result}")