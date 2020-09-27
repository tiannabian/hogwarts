#coding: utf-8
#author = hewangtong
#date = 2020/9/27
from mishop_app.page.base_page import BasePage
from mishop_app.page.order_view import OrderView


class MyOrder(BasePage):
    """我的订单列表页"""
    def goto_orderview(self):
        """
        进入订单详情
        :return:
        """
        return OrderView(self.driver)