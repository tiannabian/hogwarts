#coding: utf-8
#author = hewangtong
#date = 2020/7/11
import pytest

# @pytest.fixture()
# def login(request):
#     print("setup")
#     #rint(request.param)
#     yield
#     print('teardown')
from pythoncode.cacl import Calculator


@pytest.fixture(scope="function", autouse=True)
def setup():
    print("setup")

# @pytest.fixture(scope="function", autouse=True)
# def teardown():
#     print("teardown")