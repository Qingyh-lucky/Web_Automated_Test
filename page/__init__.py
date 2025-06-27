from selenium.webdriver.common.by import By
"""项目配置地址"""
url = "https://flight.qunar.com/"


"""以下为登录页面元素配置信息"""
# 登录链接
login_link = By.PARTIAL_LINK_TEXT, "登录"
# 切换密码登录界面
login_trave_page = By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div[2]"
# 用户名
login_username = By.CSS_SELECTOR, "#username"
# 密码
login_pwd = By.CSS_SELECTOR, "#password"

# 点击同意隐私登录
login_aggre_btn = By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[4]/input"

# 登录按钮
login_btn = By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[3]/div/div[3]/span"

login_slide_code = By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[3]/div/div[5]/div/div/div[3]/div[3]/i"
# 获取异常文本信息
login_err_info = By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[3]/div/div[4]/div/span"

# 安全退出
login_logout = By.PARTIAL_LINK_TEXT, "安全退出"






###########################################################################
#机票界面
tickets_btn=By.LINK_TEXT,"机票"
tickets_alone=By.XPATH,"/html/body/div[6]/div/div[2]/div/div/div/div[2]/ul/li[1]/a"
tickets_from=By.XPATH,"/html/body/div[6]/div/div[2]/div/div/div/div[3]/div[1]/form/div[2]/div[1]/div/input"

tickets_search=By.XPATH,"/html/body/div[6]/div/div[2]/div/div/div/div[3]/div[1]/form/div[4]/button"
tickets_to=By.XPATH,"/html/body/div[6]/div/div[2]/div/div/div/div[3]/div[1]/form/div[2]/div[2]/div/input"
tickets_to_time=By.XPATH,"/html/body/div[6]/div/div[2]/div/div/div/div[3]/div[1]/form/div[3]/div[1]/div/input"
tickets_get_price=By.CLASS_NAME,"fix_price"

tickets_from_time=By.XPATH,"/html/body/div[6]/div/div[2]/div/div/div/div[3]/div[1]/form/div[3]/div[1]/div/div[1]/div[3]/b"
tickets_from_time_select=By.XPATH,"/html/body/div[6]/div/div[2]/div/div/div/div[3]/div[1]/form/div[3]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr[4]/td[7]/div"

# tickets_reverse_time=By.XPATH,"/html/body/div[6]/div/div[2]/div/div/div/div[3]/div[1]/form/div[3]/div[3]/div/div[1]/div[3]/b"
# tickets_reverse_time_select=By.XPATH,"/html/body/div[6]/div/div[2]/div/div/div/div[3]/div[1]/form/div[3]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div[3]/table/tbody/tr[4]/td[7]/div"
"""以下为订单页面配置数据"""



###########################################################################
#火车票界面
train_btn=By.LINK_TEXT,"火车票"
# 输入起始地
train_from=By.XPATH,"//*[text()='出发']/../input"
# 输入目的地
train_to=By.XPATH,"//*[text()='到达']/../input"

# 输入日期
train_date=By.XPATH,"//*[text()='日期']/../input"
# 搜索按钮
train_search=By.XPATH,'//*[@id="js-con"]/div[1]/form/div[2]/div/span/button'

#购买第一个
train_tickets_buy=By.XPATH,'//*[@id="list_listInfo"]/ul[2]/li[1]/div/div[7]/a[1]'

train_info_name=By.XPATH, '//*[text()="姓名（必填）"]/../input'
train_info_phone=By.XPATH, '//*[text()="手机号码（必填）"]/../input'
#打印票价信息
train_tickets_info=By.XPATH,'//*[@id="fillOrder_remindInfo"]/div'
