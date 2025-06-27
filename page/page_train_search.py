# 机票搜索	- 单程/往返搜索
# - 多舱位（经济舱、商务舱）筛选
# - 特价机票显示	出发地：上海
# 目的地：广州
# 日期：未来一周随机日期
# 舱位：经济舱
import page
from base.base import Base
from page.page_login import PageLogin
from selenium.webdriver import ActionChains


class PageTrainSearch(Base):

    # 机票搜索
    def page_train(self):
        self.base_click(page.train_btn)


    def page_train_from(self,from_):
        # 点击事件
        self.base_input(page.train_from,from_)
        self.page_click_blank()

    def page_train_time(self, time_):
        date_input = self.base_find(page.train_date)
        # 设置日期
        driver=self.base_get_driver()
        driver.execute_script("arguments[0].value = arguments[1];", date_input, time_)
        driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", date_input)
        self.page_click_blank()

    def page_train_to(self,to_):
        self.base_input(page.train_to,to_)
        self.page_click_blank()

    def page_train_first_buy(self):
        self.base_click(page.train_tickets_buy)

    def page_train_search(self):
        self.base_click(page.train_search)

    def page_train_prices_info(self):
        return self.base_get_text(page.train_tickets_info)

    def page_click_blank(self):
        action = ActionChains(self.base_get_driver())
        action.move_by_offset(0, 0)
        action.click()
        action.perform()

    def page_train_buy(self,from_,time_,to_,name_,phone_):
        self.page_train_from(from_)
        self.page_train_to(to_)
        self.page_train_time(time_)
        self.page_click_blank()
        self.page_click_blank()
        self.page_train_search()

        self.base_click(page.train_tickets_buy)
        self.base_input(page.train_info_name,name_)
        self.base_input(page.train_info_phone,phone_)

    def page_train_back(self):
        driver=self.base_get_driver()
        driver.back()
        driver.back()






