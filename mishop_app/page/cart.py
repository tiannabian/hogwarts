#coding: utf-8
#author = hewangtong
#date = 2020/9/27
from mishop_app.page.base_page import BasePage
from mishop_app.page.checkout import Checkout

class Cart(BasePage):
    """购物车PO"""
    def goto_checkout(self):
        """
        进入结算页面
        :return:
        """
        return Checkout(self.driver)
