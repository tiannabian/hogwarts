#coding: utf-8
#author = hewangtong
#date = 2020/7/11
import pytest
import yaml


# class TestData:
#     @pytest.mark.parametrize(('a, b'), yaml.safe_load(open("./data.yaml")))
#     def test_data(self, a ,b):
#         print(a+b)


class TestDemo:
    @pytest.mark.parametrize("env",yaml.safe_load(open("./env.yaml")))
    def test_demo(self, env):
        if "test" in env:
            print("这是测试环境")
            print(env['test'])
        elif "dev" in env:
            print("这是开发环境")