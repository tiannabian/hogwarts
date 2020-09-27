from mishop_app.page.base_page import BasePage
from mishop_app.page.my_order import MyOrder


class PayList(BasePage):
    """支付列表页PO"""
    def goto_myorder(self):
        """
        进入我的订单列表页
        :return:
        """
        return MyOrder(self.driver)