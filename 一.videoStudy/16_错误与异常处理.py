# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 16_错误与异常处理.py
# @Time     : 2020/12/14 19:52
# @Software : PyCharm
# @Introduce: This is

# 1. 异常处理

"""
1. try 内的代码块写可能出错的代码块
2. except  捕获异常后执行的代码块, 默认是捕获所有错误(Exception as msg)， 也可以指定 异常
3. else 没有发生异常执行的代码块
4. finally 有无异常都会执行的代码块
"""
try:
    b = [1]
    print(b[11])
    print(b)
    print("异常后的代码")
    pass
except NameError as msg:
    print(msg)
    pass
except IndexError as msg:
    print(msg)
except Exception as msg:
    print(msg)
    pass
else:
    pass
finally:
    pass


# 2. 自定义异常

class ToolongMyException(Exception):
    def __init__(self, length):
        """

        :param length:
        """
        self.__length = length
        pass

    def __str__(self):
        return "您输入的数据长度" + str(self.__length) + "超过长度了"

    pass


def nameTest():
    name = input("请输入姓名： ")
    try:
        if len(name) > 5:
            raise ToolongMyException(len(name))
        else:
            print(name)
    except ToolongMyException as result:
        print(result)
    pass

nameTest()
