from mishop_app.page.base_page import BasePage
from mishop_app.page.calssification import Classification
from mishop_app.page.search import Search


class Main(BasePage):
    """这个是首页的PO"""
    def goto_search(self):
        """
        进入搜索结果页面
        """
        self.steps("", "")
        return Search(self.driver)