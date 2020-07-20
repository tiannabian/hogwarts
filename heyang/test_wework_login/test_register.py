#coding: utf-8
#author = hewangtong
#date = 2020/7/19
from heyang.test_wework_login.index import Index


class TestRegister:

    def setup(self):
        self.index = Index()


    def test_register(self):
        result = self.index.goto_register().register()
        assert result

