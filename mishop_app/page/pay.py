from mishop_app.page.base_page import BasePage


class Pay(BasePage):

    def goto_success(self):
        
        return Success(self.driver)