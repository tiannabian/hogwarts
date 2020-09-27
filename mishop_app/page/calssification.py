from mishop_app.page.base_page import BasePage
from mishop_app.page.product import Product

class Classification(BasePage):
    """这个是分类页的PO"""
    def goto_product(self):
        """
        进入单品页
        :return:
        """
        return Product(self.driver)