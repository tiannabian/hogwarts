#coding: utf-8
#author = hewangtong
#date = 2020/7/11
import pytest

def func(x):
    return x + 1

@pytest.mark.parametrize('a,b',[
    (2,3),
    (-1,5),
    (0,4)
])
def test_answer(a,b):
    assert func(a) == b

def test_answer1():
    assert func(4) == 5

@pytest.fixture()
def login():
    print('登录操作')
    username = 'heyang'
    return username

class TestDemo:
    def test_a(self, login):
        print(f'a username = {login}')

    def test_b(self):
        print('b')

    def test_c(self, login):
        print(f'c login = {login}')

# if __name__ == '__main__':
#     pytest.main(['test_a.py::TestDemo'])