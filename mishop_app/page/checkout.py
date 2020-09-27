from mishop_app.page.base_page import BasePage
from mishop_app.page.paylist import PayList


class Checkout(BasePage):
    """这个是结算页PO"""
    def goto_paylist(self):
        """
        进入支付列表页
        :return:
        """
        return PayList(self.driver)