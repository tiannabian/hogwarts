from mishop_app.page.base_page import BasePage
from mishop_app.page.product import Product


class Search(BasePage):

    def goto_product(self):

        return Product(self.driver)

