# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 8_元组.py
# @Time     : 2020/12/12 20:46
# @Software : PyCharm
# @Introduce: This is 元组

# 元组：
# 1. 不可变的序列，在创建之后不能做任何的修改
# 2. 用（）创建元组类型，数据项用逗号来分割
# 3. 可以是任何的类型
# 4. 当元组中只有一个元素时，要加上逗号，不然解释器会当作整形来处理
# 5. 同样支持切片操作

first_tuple = ()  # 空元组
first_tuple = ("python",) # 单个元素的元组
print(id(first_tuple))
first_tuple = ("abcd", 89, 9.33, "peter", [11, 22, 33])
print(id(first_tuple))  # 由于元组并不支持修改，所以重新赋值元组则重新开辟新地址

first_tuple[first_tuple.index([11, 22, 33])][0] = 1  # 列表可生成
print(first_tuple)

# 遍历打印元组

for item in first_tuple:
    print(item, end=" ")

print(first_tuple[2:4])
print(first_tuple[::-1])  # -1 表示从右往左遍历， 1 代表步长
print(first_tuple[::-2])  # 反转元组，每隔2个取一个
print(first_tuple[-2:-1:])  # 取倒数第二个开始到最后一个的元组

# 子元素计数

second_tuple = [11, 11]
print(second_tuple.count(11))
