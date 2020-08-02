#coding: utf-8
#author = hewangtong
#date = 2020/7/26
#主页面
from app.page.contactlistpage import ContactListPage


class MainPage:
    def goto_contactlist(self):
        """进入到通讯录"""

        return ContactListPage()

