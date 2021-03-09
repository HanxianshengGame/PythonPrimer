# !/usr/bin/env Python2
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 23_类代码编写基础.py
# @Time     : 2021/1/6 18:56
# @Software : PyCharm
# @Introduce: This is

class ThirdClass:
    def __init__(self, val):
        self.data = val
        pass

    def __add__(self, other):
        return ThirdClass(self.data + other.data)

    def __str__(self):
        return str(self.data)


obj1 = ThirdClass(1)
obj2 = ThirdClass(2)
print obj1 + obj2
