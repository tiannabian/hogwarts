#coding: utf-8
#author = hewangtong
#date = 2020/7/11
import pytest


@pytest.fixture()
def login(request):
    print("登陆方法")
    print(request.param)
    yield ['123455']
    print('teardown')