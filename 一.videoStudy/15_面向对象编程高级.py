# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 15_面向对象编程高级.py
# @Time     : 2020/12/14 13:24
# @Software : PyCharm
# @Introduce: This is

"""
单下划线，双下划线，头尾双下划线：

1. 单下划线表示的是 protected 类型
2. 双下划线表示的是 private 类型
3. 前后双下划线表示的是 魔术方法
4. xxx_ ： 避免属性名与 python 关键字冲突
"""


# 1. 私有化属性


class Person:
    __hobby = "跳舞"

    def __init__(self):
        self.__name = "李四"  # 加两个下划线，将此属性私有化
        self.__age = 30
        pass

    def printInfo(self):
        print(self.__name, self.__age)


hzj = Person()
hzj.printInfo()


# 2. 私有化方法

class Person:
    __hobby_ = "跳舞"

    def __init__(self):
        self.__name_ = "李四"  # 加两个下划线，将此属性私有化
        self.__age_ = 30
        pass

    # 私有化方法
    def __info(self):
        return [self.__name_, self.__name_]

    def printInfo(self):
        print(self.__info())


# 3. Property 属性函数

class Person(object):
    def __init__(self):
        self.__age = 18

    # def getAge(self):
    #     return self.__age
    #
    # def setAge(self, age):
    #     if age < 0:
    #         print("年龄不能小于0")
    #     else:
    #         self.__age = age
    #         pass
    #     pass
    #
    # # 1. 定义一个类属性，实现通过直接访问属性的形式去访问私有的属性
    # age = property(getAge, setAge)

    # 2. 装饰器的方式
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, parms):
        if parms < 0:
            print("年龄不能小于0")
        else:
            self.__age = parms
            pass
        pass

    pass


p1 = Person()
print(p1.age)

# 4. 单例模式与再探 __new__方法

"""
__new__ 注意点：

1. 继承自 object 的新式类才有 new 这一魔术方法
2. __new__ 是在一个对象实例化的时候调用的第一个方法
3. __new__ 至少必须有一个参数 cls，代表要实例化的类， 此参数在实例化时由
python 解释器自动提供，其他的参数用来直接传递给 __init__ 方法
4. 不要尝试去 cls.__new__(cls) 会死循环
 
"""


class Animal(object):
    def __init__(self):
        self.color = "红色"
        pass

    # 在python当中， 如果不重写, __new__ 默认结构如下
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    pass


tigger = Animal()  # 实例化的过程会自动调用 __new__ 分配内存，调用__init__ 进行构造


# 单例模式

class DataBaseClass(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


db1 = DataBaseClass()
print(id(db1))

db2 = DataBaseClass()
print(id(db2))
