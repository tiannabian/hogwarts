#coding: utf-8
#author = hewangtong
#date = 2020/7/9
import pytest
from pythoncode.cacl import Calculator

def setup_module():
    print("【开始计算】")

def teardown_module():
    print("【计算结束】")

class TestCacl:
    def teardown(self):
        print("teardown")

    # @pytest.mark.add
    @pytest.mark.parametrize('a,b,result',[
        (0,0,0),(2,2,4),(-100,-100,-200),(2,-3,-1),(0.01,0.02,0.03)
    ],ids=['两个0相加','两个正整数相加','两个负整数相加','正整数和负整数相加','两个浮点数相加'])
    def test_add(self, a, b, result):
        assert result == Calculator().add(a, b)

    # @pytest.mark.add
    @pytest.mark.parametrize("a, b, result",[
        (0,0,0),
        (2,2,0),
        (-100,-100,0),
        (2,-3,5),
        (0.01,0.02,-0.01)
    ],ids=['两个0相减','两个正整数相减','两个负整数相减','正整数和负整数相减','两个浮点数相减'])
    def test_sub(self,a,b,result):
        assert result == Calculator().sub(a,b)

    @pytest.mark.parametrize("a, b, result", [
        (0, 0, 0),
        (2, 2, 4),
        (-100, -100, 10000),
        (2, -3, -6),
        (0.1, 2, 0.2)
    ], ids=['两个0相乘', '两个正整数相乘', '两个负整数相乘', '正整数和负整数相乘', '一个正整数一个浮点数相乘'])
    def test_multi(self, a, b, result):
        assert result == Calculator().multi(a,b)

    # @pytest.mark.div
    @pytest.mark.parametrize("a, b, result", [
        (2, 2, 1),
        (-100, -100, 1),
        (6, -3, -2),
        (0.2, 0.1, 2)
    ], ids=['两个正整数相除', '两个负整数相除', '正整数和负整数相除', '两个浮点数相除'])
    def test_div(self, a, b, result):
        assert result == Calculator().div(a, b)
