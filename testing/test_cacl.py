#coding: utf-8
#author = hewangtong
#date = 2020/7/9
import pytest

from pythoncode.cacl import Calculator


def setup_module():
    print("模块级别setup")

def teardown_module():
    print("模块级别teardown")

def setup_function():
    print("函数级别setup")

def teardown_function():
    print("函数级别teardown")

class TestCacl:
    def setup(self):
        self.cal = Calculator()
        print("setup")

    def teardown(self):
        print("teardown")

    @pytest.mark.add
    @pytest.mark.parametrize("a, b, result",[
        (1,1,2),
        (2,2,4),
        (100,500,600)
    ],ids=['int','flaot','bignum'])
    def test_add(self, a, b, result):
        assert result == self.cal.add(a,b)

    @pytest.mark.add
    def test_add1(self):
        assert 3 == self.cal.add(1,2)

    @pytest.mark.div
    def test_div(self):
        assert 1 == self.cal.div(1, 0)
