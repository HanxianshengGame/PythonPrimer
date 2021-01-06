# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 4_输入输出.py
# @Time     : 2020/12/12 11:11
# @Software : PyCharm
# @Introduce: This is 输入输出


# 1. 格式化输出的方式

# % 占位符
name = '镇江'
address = '河南'
print('my name is %s：come from：【%s】'
      % (name, address))

# \n 换行

print('\nname')

# 常用的格式化符号

"""
%c   字符 
%d   有符号整型      
%u   无符号整型
%o   八进制整数
%x   十六进制整数
%e   索引符号（小写'e'）
%E   索引符号 (大写 'E')
%f   浮点实数
%g   %f 和 %e 的简写
%G   %f 和 %E 的简写


"""

# .format()
name = 'handling'
age = 12
print('name: {} age: {}'.format(name, age))

# 2. 输入

# input("name: ")： 返回的是 str 类型

name = input("please input your name: ")
print(name)

age = int(input('please input your age: '))
print(age)
