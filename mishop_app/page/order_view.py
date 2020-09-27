#coding: utf-8
#author = hewangtong
#date = 2020/9/27
from mishop_app.page.base_page import BasePage
from mishop_app.page.product import Product


class OrderView(BasePage):
    """订单详情PO"""
    def goto_product(self):
        """
        进入单品页
        :return:
        """
        return Product(self.driver)
