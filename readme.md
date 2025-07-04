# 概述
基于 Selenium 和 pytest 实现的自动化网站测试。
**特点：**
1.实现页面和操作分离（PO 模式）
2.数据驱动测试

# 功能测试
### 登录测试
测试了实现多种异常场景如未勾选协议、用户名或密码输入不正确、滑动框的拖动等
![登录测试](https://github.com/user-attachments/assets/4d1006c7-22ac-41cb-8978-f19861cbc77e)

### 测试订票功能
实现输入不同地方，不同时间，选择购买首次火车票获取票价信息；进入订单下单页面，获取该次订单信息;
![买票测试](https://github.com/user-attachments/assets/ff48ebbe-d324-46b7-ba86-60508bff3930)

### 使用 allure 生成测试报告
![网页报告](https://github.com/user-attachments/assets/614baaab-c92a-4abd-8034-607281e17d88)

更多功能，敬请期待。。。
## 环境配置
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
