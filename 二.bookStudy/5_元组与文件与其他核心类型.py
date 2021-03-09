# !/usr/bin/env Python2
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 5_元组与文件与其他核心类型.py
# @Time     : 2021/1/6 18:49
# @Software : PyCharm
# @Introduce: This is
import codecs
import struct

T1 = (0,)
T2 = (0, 'Ni', 1.2, 3)
T3 = 0, 'Ni', 1.2, 3
T4 = ('Bob', ('dev', 'mgr'))
T5 = tuple('sss')

T6 = ((1,2,3), 1)
tmp = T6[0]
tmp = tmp + (1,)
print('111', tmp)

print (T5[1:1])
print (len(T5))
print (T5 + T3)
print (T5 * 3)
print T5.count('sss')  # sss 的数量
# print T5.index('sss')  # sss 的角标

print sorted(T5)

from collections import namedtuple

rec = namedtuple('hanzhenjiang', ['name', 'age', 'jobs'])
bob = rec('bob', age=40.5, jobs=['dev', 'mgr'])

print bob

output = open('spam', 'w')

output = codecs.open('f.txt', 'w', encoding='utf8')
output.writelines(['11111111'])
output.flush()
output.close()

input = codecs.open('f.txt', 'r', encoding='utf8')
data = eval(input.readline())
print data
input.flush()
input.close()

#  在文件中存储 python 对象： 转换
# 1. eval（高高兴兴执行python的任何表达式）
# 2. pickle(适用于存储python原生对象)
# 3. json python 标准库内的非常直接的转换


# eval(expression[, globals[, locals]])
# 参数
# expression -- 表达式。
# globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
# locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
import sys

file_obj = open('spam', 'w')
file_obj.write('[1,2,3]&{"a" : 1 , "b" : 2}')
file_obj.close()
file_obj = open('spam', 'r')
F = file_obj.readline()
file_obj.close()

print(F)
parts = F.split('&', 1)
print(parts[0], parts[1])
list1 = eval(parts[0])
dict1 = eval(parts[1])
print(list1, dict1)

print(eval('sys.path'))

D = {'a': 1, 'b': 2}
F = open('data_file.pkl', 'wb')
import pickle

pickle.dump(D, F)
F.close()

F = open('data_file.pkl', 'rb')
E = pickle.load(F)
print E

name = dict(first='Bob', last='Smith')
rec = dict(name=name, job=['dev', 'mgr'], age=40.5)
print rec
import json

json_str = json.dumps(rec)
print json_str

dict1 = json.loads(json_str)
print (dict1)

# 存储与打包二进制数据  struct


type_dict = {"int8": (1, "b"),
             "uint8": (1, "B"),
             "int16": (2, "h"),
             "uint16": (2, "H"),
             "int32": (4, "i"),
             "uint32": (4, "I"),
             "float": (4, "f"),
             "double": (8, "d"),
             "bool": (1, "?"),
             "string": (-1, "s")  # 特殊 2+L暂定
             }


def DataPack(placeholder_ch, val):
    s = struct.Struct("<" + placeholder_ch)
    return s.pack(val)


def DataUnpack(placeholder_ch, byte_buffer):
    s = struct.Struct("<" + placeholder_ch)
    return s.unpack(byte_buffer)


#  文件上下文管理器 with
# with 让我们可以把文件处理代码包装到一个逻辑层中， 以确保在退出后一定会自动关闭文件（同时将其输出
# 缓冲区内容写入磁盘, 而不是依赖于垃圾回收自动关闭）

with open('data_file.pkl', 'r') as file_obj:
    content = file_obj.read()


# None 对象

# None 是一个真正的对象， 并且有一块真实的内存， None 是由 python 给定的一个内置名称


# 类型的对象

# [对象的类型本身 也属于 type 类型的对象]


print (isinstance([1], list)) # 测试实例
print (isinstance([1], type([2])))


a = [1,2,3]
a.append(None)
a[-1] = [1,2]
print a

a.append([1,23])
print a
def list_covert_tuple(list_data):
    for index in range(len(list_data)):
        if isinstance(list_data[index], list):
            list_covert_tuple(list_data[index])
            list_data[index] = tuple(list_data[index])

a = [[1,2,3], 1, [1,[1]]]
list_covert_tuple(a)
a = tuple(a)
print a


def tuple_covert_list(tuple_data):
    list_data = []
    for index in range(len(tuple_data)):
        if isinstance(tuple_data[index], tuple):
            list_data.append(tuple_covert_list(tuple_data[index]))
        else:
            list_data.append(tuple_data[index])
    return list_data


a = ((1,2,3), ( 1, 2), 2, 3, '', (1,(2,)))

print tuple_covert_list(a)