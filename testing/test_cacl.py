#coding: utf-8
#author = hewangtong
#date = 2020/7/9
from decimal import Decimal
import pytest
import yaml

from pythoncode.cacl import Calculator

def setup_module():
    print("【开始计算】")

def teardown_module():
    print("【计算结束】")

with open("datas/cacl.yaml") as f:
    datas = yaml.safe_load(f)
    add_datas = datas['add'].values()
    add_ids = list(datas['add'].keys())
    sub_datas = datas['sub'].values()
    sub_ids = list(datas['sub'].keys())
    multi_datas = datas['multi'].values()
    multi_ids = list(datas['multi'].keys())
    div_datas = datas['div'].values()
    div_ids = list(datas['div'].keys())




class CheckCacl:

    @pytest.mark.dependency()
    @pytest.mark.parametrize('a,b,result', add_datas ,ids=add_ids)
    def check_add(self, a, b, result):
        assert result == Calculator().add(a, b)


    @pytest.mark.dependency(depends=["check_add"])
    @pytest.mark.parametrize("a, b, result", sub_datas ,ids=sub_ids)
    def test_sub(self,a,b,result):
        assert result == Calculator().sub(a,b)


    @pytest.mark.dependency()
    @pytest.mark.parametrize("a, b, result", multi_datas, ids=multi_ids)
    def check_multi(self, a, b, result):
        print(type(a),type(b))
        if type(a)=='float' and type(b)=='float':
            assert result == Calculator().multi(Decimal(a), Decimal(b))
        else:
            assert result == Calculator().multi(a,b)


    @pytest.mark.dependency(depends=["check_multi"])
    @pytest.mark.parametrize("a, b, result", div_datas, ids=div_ids)
    def check_div(self, a, b, result):
        assert result == Calculator().div(a, b)


    # def test_assume(self):
    #     print("登录操作")
    #     pytest.assume(2==2)
    #     print("加购操作")





