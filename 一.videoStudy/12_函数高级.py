# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 12_函数高级.py
# @Time     : 2020/12/13 9:55
# @Software : PyCharm
# @Introduce: This is

# 1. 全局变量在函数内部的修改

# 在函数内部修改全局变量时需要先声明
# global global_var
# global_var = 1

name = "handling"


def printInfo():
    global name
    name = "1"


printInfo()
print(name)

# 2. 函数参数全部是引用传参

# python 中万物皆是对象，值是靠引用来传递的
# 如果参数是可变类型则进行修改会影响到本体，如果不可变类型进行修改就会新开辟，且不影响本体

# 不可变类型： 整型，字符串，元组
# 可变类型： 集合，字典，列表

a = 1


def func(x):
    print("x的地址: {}".format(id(x)))
    x = 2
    print("x修改后的地址: {}".format(id(x)))
    pass


print("a的地址: {}".format(id(a)))
func(a)
print(a)

first_list = [1, 2, 3]


def func(tmp_list):
    tmp_list.append(1)


func(first_list)
print(first_list)

# 3. 匿名函数

# python使用lambda关键字创建匿名函数（无名字创建的标准函数）
# lambda 的设计就是为了满足简单函数的场景，仅仅能封装有限的逻辑，复杂逻辑实现不了，
# 使用def来解决复杂函数
# lambda 参数1，参数2，参数3: 表达式

# 特点：
"""
1. 使用 lambda 关键字取创建函数
2. 没有名字的函数
3. 匿名函数冒号后的表达式有且仅有一个，自带return，return
的结果就是表达式计算后的结果
"""


def calculate(x, y):
    return x + y


print(calculate(11, 45))

m = lambda x, y: x + y
print(m(11, 12))
print((lambda x, y: x if x > y else y)(11, 12))

age = 15
print("可以参军" if age > 18 else "继续上学")


# 4. 递归函数

# 1. 自己调用自己
# 2. 必须有一个明确的结束条件

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


import os  # 引入文件操作模块


def findFile(file_path):
    list_resources = os.listdir(file_path)
    for child_file in list_resources:
        child_file_path = os.path.join(file_path, child_file)
        if os.path.isdir(child_file_path):
            findFile(child_file_path)
            pass
        else:
            print(child_file_path)
            pass
    else:
        return
    pass


findFile("H:\\EffectiveC++")
