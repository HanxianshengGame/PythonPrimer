# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 17_动态绑定属性与方法.py
# @Time     : 2020/12/14 20:14
# @Software : PyCharm
# @Introduce: This is

# 1. 动态添加属性  (运行中给对象或类添加属性)

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    pass

    def __str__(self):
        return "{} 今年 {} 岁了".format(self.__name, self.__age)

    pass


hzj = Student("handling", 20)
hzj.weight = 80  # 动态添加实例属性，仅针对改实例对象，其他实例对象无
print(hzj.weight)

Student.school = "南阳理工"  # 动态添加类属性
print(hzj.school)

import types  # 添加方法的库


# 2. 动态添加方法

def dynamicMethod(self):
    print("体重 {} 身高 {}".format(self.weight, self.height))


hzj.height = 180
hzj.printInfo = types.MethodType(dynamicMethod, hzj)  # 动态的绑定实例方法
hzj.printInfo()


@classmethod
def classMethod(cls):
    pass


@staticmethod
def staticMethod():
    pass


Student.TestMethod = classMethod
Student.staticMethod = staticMethod

# 3. __slots__ 属性限制
"""

"""


class Student(object):
    # 不在 __slots__ 声明的属性不能被动态添加
    __slots__ = ("name", "age")

    def __str__(self):
        return "{} {}".format(self.name, self.age)


hzj = Student()
hzj.name = "小王"
hzj.age = 20
# 未用 __slots__ 属性定义属性时数据都会在 __dict__ 存储，空间占用大
# 用了 __slots__ 后，__dict__ 就会消失
# print(hzj.__dict__)


# 在继承关系中使用 __slots__

# 子类未声明 __slots__时，是不会继承父类的 __slots__ 的, 一旦声明就会继承
class subStudent(Student):
    __slots__ = ()
    pass


ln = subStudent()
# ln.gender = "男"



