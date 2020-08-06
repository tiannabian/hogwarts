from mishop_app.page.base_page import BasePage
from mishop_app.page.pay import Pay


class Checkout(BasePage):

    def goto_pay(self):

        return Pay(self.driver)