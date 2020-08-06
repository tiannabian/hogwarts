from mishop_app.page.base_page import BasePage
from mishop_app.page.checkout import Checkout


class Product(BasePage):

    def goto_checkout(self):

        return Checkout(self.driver)
