# !/usr/bin/env Python2
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 26_运算符重载.py
# @Time     : 2021/1/6 18:59
# @Software : PyCharm
# @Introduce: This is

'''
方法名       实现功能      触发调用的形式
__init__    构造函数       对象创建时
__del__     析构函数       X对象回收
__add__      + 运算符     X + Y, X+=Y        __iadd__   +=
__or__       | 运算符     X | Y, X|=Y        __ior__    |=
__repr__, __str__ 打印，转换  print(X), repr(X), str(X)
__call__     函数调用     X(*args, **kargs)
__getattr__  属性访问     X.undefined
__setattr__  属性赋值     X.any = value
__delattr__  属性删除     del x.any
__getattribute__ 属性访问  X.any
__getitem__       索引分片   x[key], x[i:j]
__setitem__       索引赋值和分片赋值    x[key] = val
__delitem__       索引删除与分片删除    del x[key]
__len__           长度                 len(X)
__bool__          布尔测试              bool(X)
__lt__, __gt__      比较               X < Y, X > Y, X <= Y, X >= Y, X == Y, X ！= Y
__le__, __ge__,
__eq__,__ne__
__radd__            +
__iadd__            +=

__iter__, __next__  迭代上下文
__contains__        成员关系测试          item in X
__index__           整数值转换            hex(X), bin(X), O[X]
__enter__, __exit__ 上下文管理器          with obj as var:
__get__, __set__     描述符属性           X.attr, X.attr = value, del X.attr
__delete__           析构函数
__new__              创建               __init__ 之前的对象创建

'''


# [1] 索引与分片 __getitem__ 和 __setitem__
# 如果一个类定义（继承）了__getitem__ 的话， 当实例X 出现 X【i】 索引运算中，就会调用改__getitem__方法，
# 把 X 作为第一个参数，索引值是第二个参数

class Indexer:
    def __getitem__(self, item):
        return item ** 2


X = Indexer()
print X[2]  # __getitem__(X, 2)

# __getitem__ 也会被分片表达式调用， 分片操作其实是 分片对象制作了一个分片边界(start, stop, step)，并传入列表的索引实现

L = [1, 2, 3, 5]
print L[slice(2, 4)]


class Indexer:
    def __init__(self):
        self.data = [1, 2, 3, 4]

    def __getitem__(self, index):
        if isinstance(index, int):
            print('getitem', index)
        else:
            print('slicing', index.start, index.stop, index.step)


X = Indexer()
print X[2:None]

# __getitem__ 也可以是 python 中重载迭代的方式

class StepperIndex:
    def __init__(self):
        self.data = []
        pass

    def __getitem__(self, item):
        return self.data[item]


# __setitem__ 索引赋值方法的话， 拦截索引复制和分片赋值

class IndexSetter:
    def __init__(self):
        self.data = [1,2,3]
        pass

    def __setitem__(self, key, value):
        self.data[key] = value
        pass


X = IndexSetter()
X[1] = 3
print X.data

X[:] = [1,2,3,4]
print X.data


# [2] 可迭代对象: __iter__ 和 __next__

class Squares:
    def __init__(self, start, stop):
        self.val = start -1
        self.stop = stop

    def __iter__(self):
        return self

    def next(self):
        if self.val == self.stop:
            raise StopIteration
        self.val += 1
        return self.val ** 2





