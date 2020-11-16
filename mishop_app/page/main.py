from mishop_app.page.base_page import BasePage
from mishop_app.page.search import Search


class Main(BasePage):
    """工作台PO"""
    def goto_search(self):
        """
        超级搜索结果页面
        """
        self.steps("", "")
        return Search(self.driver)

    def goto_distributionrules(self):
        """
        专卖店稀缺货品分货规则页面
        :return:
        """
        pass

    def goto_newcapams(self):
        """
        北京（线下）页面
        :return:
        """
        pass

    def goto_newmonthdata(self):
        """
        本月销售汇总页面
        :return:
        """
        pass

    def goto_newrebatedata(self):
        """
        专卖店返利数据页面
        :return:
        """
        pass

    def goto_newtodaydata(self):
        """
        当日销售页面
        :return:
        """
        pass

    def goto_newbusinesstop(self):
        """
        本月合作商排名
        :return:
        """
        pass

    def goto_newstoretop(self):
        """
        本月门店排名
        :return:
        """
        pass









