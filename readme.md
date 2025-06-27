## 概述
基于 Selenium 和 pytest 实现的自动化网站测试。
**特点：**
1.实现页面和操作分离（PO 模式）
2.数据驱动测试
**功能：**
1.实现多种异常场景（密码错误，未勾选协议等）
2.测试买票功能
3.使用 allure 生成测试报告

更多功能，敬请期待。。。
## 配置
allure 库依赖 jdk1.8+以上环境(
    参考博客：https://blog.csdn.net/m0_70545163/article/details/141332829)
安装好 allure 需要配置环境变量(
    参考博客：https://blog.csdn.net/lixiaomei0623/article/details/120185069)。
## 报告
1. 生成allure报告
`allure generate .allure_results -o allure_report --clean`
2. 运行命令查看报告
运行下面的命令或者打开allure_report中的index.html文件
`allure open allure_report`