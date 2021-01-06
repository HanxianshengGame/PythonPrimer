# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 14_面向对象编程基础.py
# @Time     : 2020/12/14 9:04
# @Software : PyCharm
# @Introduce: This is

# 1. 定于类和对象

# class 类名
#     属性
#     方法

class Person(object):
    # 属性
    name = "小明"
    age = 20

    # 行为
    def eat(self):
        print("大口大口吃饭")
        pass

    def run(self):
        print("飞快的跑")
        pass


hzj = Person()  # 创建对象
hzj.eat()
hzj.run()


# 2. 实例方法与属性

#  实例方法： 类的实例可调用，第一个参数是 self (C++中的成员函数)
#  属性：
#       1. 类中定义的 变量，在方法外面的属性是类属性
#       2. 在方法里面使用 self 引用的属性称为实例属性 （成员变量）

class Animal(object):
    color = "白色"  # 类属性

    def __init__(self):
        self.name = "旺财"  # 实例属性

    def test(self):
        print("我是实例方法")
        pass


dog = Animal()
dog.test()


# 3. __init__(self) 声明实例属性（实例属性类似声明C++成员变量）
# 特点：__init__(self) : 初始化方法，实例化对象的时候自动调用，完成一些初始化设置
#      __init__(self,arg)：可进行传递参数，类似（C++构造函数）

# 使用双下划线包起来的叫 魔术方法

class People:
    # def __init__(self):
    #     self.name = ""
    #     self.sex = ""
    #     self.age = ""

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = 20
        pass

    def eat(self):
        print("喜欢吃榴莲")
        pass


xq = People("小倩", "女", 20)
xq.name = "小倩"
xq.sex = "女生"
xq.age = 20
print(xq.name, xq.sex, xq.age)


# 4. 理解 self

# self 和对象指向同一片内存地址，可以认为 self 就是实例对象的引用(类似C++ this)
# self 传参问题，当实例对象调用方法时，python 解释器会把这个对象作为
#       第一个参数传递给 self，开发者只需要传递后面的参数即可

class Person(object):
    """
    定义类
    """

    def __init__(self, pro):
        self.pro = ""

    def eat(self):
        """
        实例方法
        :return:
        """
        print(id(self))
        pass


xw = Person("软件工程")
print(id(xw))
xw.eat()

# 5. 魔术方法 __xxx__

# python 对象内部内置号的特定的方法， 方法名 __xxx__ 在特定时机被调用

"""
__init__: 初始化一个类，在创建实例对象为其赋值时调用 (构造函数)
__str__ : 将对象转换为字符串 str(对象)测试时，打印对象的信息时调用 (format(class))
__new__ : 创建并返回一个实例对象时被调用，调用一次，得到一个对象 (static void* operator new(std::size_t size))
__class__: 获得已知对象的类 （对象.__class_）
__del__ : 对象在程序运行结束后进行对象销毁时调用,释放资源 (析构函数)
"""


# __str__ 方法
# __new__ 方法

class Person(object):
    """
    定义类
    """

    def __init__(self, name, pro):
        self.name = name
        self.pro = pro
        print("__init__执行")

    def __str__(self):
        return "{} 职业是：{} ".format(self.name, self.pro)

    def __new__(cls, *args, **kwargs):
        """
        创建对象实例的方法

        场景：可以控制创建对象的一些属性限定，经常用来单例模式使用
        :param args:
        :param kwargs:
        """
        print("__new__ 执行")
        return object.__new__(cls)  # new执行完对象便得到了内存，之后执行init方法对对象进行初始化

    def eat(self):
        """
        实例方法
        :return:
        """
        print(id(self))
        pass


xw = Person("handling", "软件工程")
print(xw)


# 6. 析构函数 __del__


class Person(object):
    """
    定义类
    """

    def __init__(self, name, pro):
        self.name = name
        self.pro = pro
        print("__init__执行")

    def __del__(self):
        print("__del__执行")

    def __str__(self):
        return "{} 职业是：{} ".format(self.name, self.pro)

    def __new__(cls, *args, **kwargs):
        """
        创建对象实例的方法

        场景：可以控制创建对象的一些属性限定，经常用来单例模式使用
        :param args:
        :param kwargs:
        """
        print("__new__ 执行")
        return object.__new__(cls)  # new执行完对象便得到了内存，之后执行init方法对对象进行初始化

    def eat(self):
        """
        实例方法
        :return:
        """
        print(id(self))
        pass


zcy = Person("zcy", "软件工程")
del zcy  # 主动 del 对象


# 7. 继承 is-a

class Base(object):
    def eat(self):
        pass


class Drived(Base):
    pass


derived = Drived()
derived.eat()


# 8. 多继承

class Base1(object):
    def eat(self):
        pass


class Base2(object):
    def eat(self):
        pass


class Drived(Base1, Base2):
    pass


derived = Drived()
print(Drived.__mro__)  # 显示类的继承层次关系
derived.eat()  # Base1,Base2 顺序查找，找到即决定是其, 不会再去找了


# 9. 重写和调用父类方法

class Base(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def eat(self):
        print("我喜欢吃面条")
        pass

#
# class Drived(Base):
#     def __init__(self, name, color):
#         super().__init__(name, color)  # super() 自动找父类的(按搜索顺序)，进而调用方法
#         self.height = 90
#         self.weight = 20
#
#     def eat(self):
#         super().eat()
#         print("我喜欢吃素")
#         pass
#
#
# derived = Drived("hzj", "蓝")
# derived.eat()


# 10. 多态

class Animal(object):
    """
    父类
    """

    def sayWho(self):
        print("我是一个动物")
        pass

    pass


class Duck(Animal):
    """
    子类
    """

    def sayWho(self):
        print("我是一个鸭子")
        pass

    pass


class Dog(Animal):
    """
    子类
    """

    def sayWho(self):
        print("我是一个小狗子")
        pass

    pass


duck1 = Duck()
duck1.sayWho()

dog1 = Dog()
dog1.sayWho()


def commonInvoke(animal):
    animal.sayWho()


animals_list = [Duck(), Dog()]
for animal in animals_list:
    commonInvoke(animal)


# 11. 类属性与实例属性再谈

# 类属性： 是类所拥有的属性，可直接通过类名或对象名访问(整个类的实例对象共享)
# 实例属性：只能被实例对象访问

class Student:
    name = "李明"

    def __init__(self, age):
        self.age = age
        pass


print(Student.name)
Student.name = "11"  # 只能通过类名.类属性=  进行修改
print(Student.name)


# 12. 类方法与静态方法

class People:
    country = "china"

    # 类方法 用 classmethod 来进行修饰，主要与类属性与类方法打交道
    @classmethod
    def getCountry(cls):
        return cls.country

    @classmethod
    def setCountry(cls, country):
        cls.country = country

    # 静态方法 用staticmethod 来进行装饰
    # 静态方法主要存放逻辑性的代码，本身和类以及实例对象没有交互。
    @staticmethod
    def getData():
        return People.country


print(People.getCountry())  # 通过类名去引用类方法
p = People()
print(p.getCountry())  # 通过对象名去访问类方法
People.setCountry("england")
print(People.getCountry())

print(People.getData())  # 通过类名去调用静态方法

import time


class TimeTest:
    @staticmethod
    def showTime():
        return time.strftime("%H:%M:%S", time.localtime())


print(TimeTest.showTime())
