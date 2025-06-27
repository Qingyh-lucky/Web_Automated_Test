import pytest
from base.get_driver import GetDriver
from page.page_train_search import PageTrainSearch
from tool.read_json import read_json
import logging
import allure
# from allure_commons import servity

# 配置日志
logger = logging.getLogger()
logger.setLevel(logging.INFO)
sh = logging.StreamHandler()
logger.addHandler(sh)

# 获取测试数据
def get_data():
    arrs = []
    for data in read_json("train.json").values():
        arrs.append((data.get("from"),
                     data.get("time"),
                     data.get("to"),
                     data.get("name"),
                     data.get("phone")))
    return arrs

# 使用pytest.fixture替代setUpClass和tearDownClass
@pytest.fixture(scope="class", autouse=True)
def setup_class(request):
    """类级别初始化，整个测试类只执行一次"""
    # 实例化页面对象
    driver = GetDriver().get_driver()
    login = PageTrainSearch(driver)
    login.page_train()
    # 将login绑定到类实例上
    request.cls.login = login

    # 测试类结束时的清理
    yield
    # 关闭driver
    GetDriver().quit_driver()

# 使用pytest.mark.parametrize替代parameterized.expand
@allure.epic("买票测试")
@allure.feature("买票功能")
# @allure.severity("critical")  # 为整个类设置严重性级别
class TestTrain:
    @pytest.mark.parametrize("from_, time, to_, name, phone", get_data())
    def test_train(self, from_, time, to_, name, phone):
        """火车票搜索测试方法"""
        # 调用搜索方法
        self.login.page_train_buy(from_, time, to_, name, phone)
        price = self.login.page_train_prices_info()
        print(price)
        self.login.page_train_back()