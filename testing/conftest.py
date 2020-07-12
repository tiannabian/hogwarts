#coding: utf-8
#author = hewangtong
#date = 2020/7/11
from typing import List
import pytest

# @pytest.fixture()
# def login(request):
#     print("setup")
#     #rint(request.param)
#     yield
#     print('teardown')
#from pythoncode.cacl import Calculator


# @pytest.fixture(scope="function", autouse=True)
# def setup():
#     print("setup")

# @pytest.fixture(scope="function", autouse=True)
# def teardown():
#     print("teardown")
import yaml


#自定义测试用例的执行顺序
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)
    print(len(items))
    # 倒序执行 items里面的测试用例
    #items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        if 'sub' in item.nodeid:
            item.add_marker(pytest.mark.sub)
        if 'multi' in item.nodeid:
            item.add_marker(pytest.mark.multi)
        if 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)



# 处理命令行传来的参数，设置成fixture，将 test 环境和dev环境以及st环境分别处理，获取想要的不同环境下的测试数据。
@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        datapath = 'datas/test/data.yaml'

    if myenv == 'dev':
        datapath = 'datas/dev/data.yaml'

    if myenv == 'st':
        datapath = 'datas/st/data.yaml'

    with open(datapath) as f:
        datas = yaml.safe_load(f)

    return myenv, datas
