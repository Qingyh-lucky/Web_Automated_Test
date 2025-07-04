from selenium import webdriver



# class GetDriver:
#     driver = None  # 类变量，用于存储驱动实例
#
#     @classmethod
#     def get_driver(cls, browser="edge"):
#         """
#         获取浏览器驱动实例
#         :param browser: 浏览器类型 (chrome/edge/firefox)
#         :return: WebDriver 实例
#         """
#         if cls.driver is None:
#             # 根据浏览器类型创建驱动
#             if browser.lower() == "chrome":
#                 options = webdriver.ChromeOptions()
#                 options.add_argument('--no-sandbox')
#                 options.add_argument('--disable-dev-shm-usage')
#                 options.add_argument('--disable-gpu')
#                 options.add_argument('--window-size=1920,1080')
#
#                 # 添加其他常用选项
#                 options.add_argument('--ignore-certificate-errors')
#                 options.add_argument('--allow-running-insecure-content')
#                 options.add_argument('--disable-extensions')
#                 options.add_argument('--disable-popup-blocking')
#
#                 # 创建 Chrome 驱动
#                 cls.driver = webdriver.Chrome(options=options)
#
#             elif browser.lower() == "edge":
#                 options = webdriver.EdgeOptions()
#                 options.add_argument('--no-sandbox')
#                 options.add_argument('--disable-dev-shm-usage')
#                 options.add_argument('--disable-gpu')
#                 options.add_argument('--window-size=1920,1080')
#
#                 # 创建 Edge 驱动
#                 cls.driver = webdriver.Edge(options=options)
#
#             elif browser.lower() == "firefox":
#                 options = webdriver.FirefoxOptions()
#                 options.add_argument('--width=1920')
#                 options.add_argument('--height=1080')
#
#                 # 创建 Firefox 驱动
#                 cls.driver = webdriver.Firefox(options=options)
#
#             else:
#                 raise ValueError(f"不支持的浏览器类型: {browser}")
#
#             # 最大化浏览器窗口
#             cls.driver.maximize_window()
#
#             # 设置隐式等待
#             cls.driver.implicitly_wait(10)
#
#             # 打开初始页面（可选）
#             # cls.driver.get(Config.BASE_URL)  # 从配置文件获取URL
#
#         return cls.driver
#
#     @classmethod
#     def quit_driver(cls):
#         """关闭浏览器驱动"""
#         if cls.driver:
#             try:
#                 cls.driver.quit()
#             except Exception as e:
#                 print(f"关闭浏览器时出错: {str(e)}")
#             finally:
#                 cls.driver = None
from selenium import webdriver
import page
class GetDriver:
    # 设置类属性
    driver = None

    # 获取driver
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            options = webdriver.EdgeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            options.add_argument('--window-size=1920,1080')

            # 创建 Edge 驱动
            cls.driver = webdriver.Edge(options=options)
            # 最大化
            cls.driver.maximize_window()
            # 打开浏览器
            cls.driver.get(page.url)
        return cls.driver

    # 退出driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            print("关闭之前：", cls.driver)
            cls.driver.quit()
            print("关闭之后：", cls.driver)

            # 注意：此处有一个很大坑
            cls.driver = None
            # print("置空之后：", cls.driver)
