# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 11_函数基础.py
# @Time     : 2020/12/13 8:52
# @Software : PyCharm
# @Introduce: This is 函数


# 1. 函数定义
"""
def 函数名(参数列表 0-n个) :
      注释
      code
"""


def printInfo():
    """
    这个函数是用来打印一些信息的
    :return:
    """
    print("printInfo")


# 2. 函数的调用

printInfo()


# 3. 定义带参数的函数

def printInfo(name, height, weight):
    """
    打印一些信息
    :param name: 名字
    :param height: 身高
    :param weight: 体重
    :return:
    """

    print("%s的身高是%f" % (name, height))
    print("%s的体重是%f" % (name, weight))
    pass


printInfo("小李", 122, 111)

# 4. 参数的分类

"""
1. 必选参数: 调用的时候必须赋值的
2. 默认参数[缺省情况下]： 和 C++相同
3. 可选参数: 当参数的个数不确定时使用，比较灵活(本身为元组类型 tuple)
4. 关键字参数: 本身为字典类型（dict）
"""


# 必选参数
def mySum(a, b):  # 形式参数
    temp_sum = a + b
    print(temp_sum)


mySum(20, 15)


# 默认参数(和C++相同)

def mySum(a=20, b=30):
    temp_sum = a + b
    print(temp_sum)


mySum()


# 可变参数 *args定义

def getComputer(*args):
    """
    计算累加和
    :param args: 可变长的参数类型
    :return:
    """
    print(args)
    print(sum(args))


getComputer(1, 2, 3, 4)


# 关键字可变参数  **来定义
# 在函数体内，参数关键字是一个字典类型，key 是一个字符串

def keyFunc(**kwargs):
    print(kwargs)


first_dict = {"name": "leo",
              "age": 35}

keyFunc(**first_dict)

# 以 key=value 会识别为dict的元素
keyFunc(name="peter", age=26)


# 可选参数必须放到关键字可选参数之前
def complexFunc(*args, **kwargs):
    print(args)
    print(kwargs["name"])
    kwargs.update({"grade": 6})


complexFunc(1, 2, **first_dict)
print(first_dict)  # 传的first_dict是值类型


# 5. 函数返回值

# 类型： 可以返回任意类型，返回值取决于 return 紧跟着的类型

def mySum(a, b):
    tmp_list = []
    tmp = a + b
    tmp_list.append(tmp)
    return tmp_list


print(mySum(10, 30))


def returnTuple():
    """
    返回元组类型的数据
    :return: tuple
    """
    return 1, 2, 3


print(type(returnTuple()))


# 6. 函数的嵌套调用

def func1():
    print("-----------func1 start------------")
    print("-----------func1 end------------")


def func2():
    print("-----------func2 start------------")
    func1()
    print("-----------func2 end------------")


func2()
