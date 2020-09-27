from mishop_app.page.base_page import BasePage
from mishop_app.page.cart import Cart
from mishop_app.page.checkout import Checkout


class Product(BasePage):
    """单品页PO"""
    def goto_cart(self):

        return Cart(self.driver)
