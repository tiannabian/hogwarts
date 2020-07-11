#coding: utf-8
#author = hewangtong
#date = 2020/7/11
import pytest


def test_cart1(login):
    print("购物车用例1")

def test_cart2(login):
    print("购物车用例2")



#参数化结合fixture结合使用
#情况一：
#情况二：传入一个fixture方法，将数据传入到fixture方法中；fixture方法使用request参数来接收这组数据，在方法体里面使用request.param来使用这组数据
@pytest.mark.parametrize('login',[
    ('username1','password1'),
    ('username2','password2')
], indirect=True)
def test_cart3(login):
    print("购物车用例3")