#coding: utf-8
#author = hewangtong
#date = 2020/7/11

def fun():
    for i in range(3):
        print(f"i = {i}")
        yield  #return  同时相当于暂停并且记住上一次的执行位置
        print('end')

f = fun()
next(f)