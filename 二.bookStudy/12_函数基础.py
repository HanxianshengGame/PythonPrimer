# !/usr/bin/env Python2
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 12_函数基础.py
# @Time     : 2021/1/6 18:53
# @Software : PyCharm
# @Introduce: This is


'''
1. def 是可执行的代码
2. def 创建了一个对象并将其赋值给某一变量名
'''

def printer(message):
    print('Hello' + message) 



'''
1. lambda 创建了一个对象并作为结果返回
'''

funcs = [lambda x: x ** 2 , lambda y : y * 2]


'''
1. yield 向调用者发回一个结果对象， 但是会记着它离开的位置
'''

def squares(x):
    for i in range(x):
        yield i ** 2

print(squares(2))


'''
1. global ： 在函数中想要改变外层模块的变量， 需要在 global 语句声明它
'''

x = 'old'
def changer():
    global x;
    x = 'new'
    
'''
1. nonlocal ： 声明了一个需要被赋值的外层函数变量
'''

def outer():
    x = 'old'
    def changer():
        nonlocal x;        # 3.x
        x = 'new'



