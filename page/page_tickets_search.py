# 机票搜索	- 单程/往返搜索
# - 多舱位（经济舱、商务舱）筛选
# - 特价机票显示	出发地：上海
# 目的地：广州
# 日期：未来一周随机日期
# 舱位：经济舱
import page
from base.base import Base
from page.page_login import PageLogin

class PageTicketsSearch(PageLogin):


    # 机票搜索
    def page_tickets(self):
        self.base_click(page.tickets_btn)


    def page_tickets_from(self,from_):
        self.base_input(page.tickets_from,from_)

    def page_tickets_from_time(self, from_time):
        self.base_click(page.tickets_from_time)
        self.base_click(page.tickets_from_time_select)
        # self.base_input(page.tickets_from_time, from_time)

    def page_tickets_to(self,to_):
        self.base_input(page.tickets_to,to_)

    def page_tickets_to_time(self, to_time):
        self.base_input(page.tickets_to_time, to_time)

    def page_tickets_search(self):
        self.base_click(page.tickets_search)

    def page_tickets_alone(self, from_, from_time, to, to_time):
        if self.page_is_login_success:
            self.base_click(page.tickets_btn)
            self.base_click(page.tickets_alone)
            self.page_tickets_from(from_)
            self.page_tickets_from_time(from_time)
            self.page_tickets_to(to)
            # self.page_tickets_to_time(to_time)
            self.page_tickets_search()
        else:
            print("尚未登录成功")

    #国内往返搜索
    def page_tickets_reverse(self,from_,from_time,to,to_time):
        if self.page_is_login_success:
            self.base_click(page.tickets_btn)
            self.base_click(page.tickets_alone)
            self.page_tickets_from(from_)
            self.page_tickets_from_time(from_time)
            self.page_tickets_to(to)
            self.page_tickets_to_time(to_time)
            self.page_tickets_search()
        else:
            print("尚未登录成功")

    def page_get_ticktes_price(self):
        return self.base_find(self.page_get_ticktes_price()).text()

