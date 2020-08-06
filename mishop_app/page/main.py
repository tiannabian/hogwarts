from mishop_app.page.base_page import BasePage
from mishop_app.page.calssification import Classification


class Main(BasePage):

    def goto_classification(self):
        """
        进入分类页面
        """
        return Classification(self.driver)