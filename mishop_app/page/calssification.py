from mishop_app.page.base_page import BasePage
from mishop_app.page.search import Search


class Classification(BasePage):

    def goto_search(self):

        return Search(self.driver)