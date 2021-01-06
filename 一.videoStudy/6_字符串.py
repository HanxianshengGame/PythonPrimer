# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 6_字符串.py
# @Time     : 2020/12/12 15:35
# @Software : PyCharm
# @Introduce: This is 字符串


# 序列： 字符串，元组，列表
# 支持索引与切片的集合/容器
# 特征： 第一个正索引是0，指向的是左端，第一个
# 索引为负数的时候，指向的是右端

# 切片： 截取序列的其中一段内容
# 语法： [start,end,step] step默认是1

one_str = "python"
print(type(one_str))
print(one_str[0])

temp_str = "1111" \
           "sss"  # 使用\来继续字符串的书写
print(temp_str)

temp_str = r"\n"  # 在字符串前加 r 可以防止转义

# for item in one_str:
#     print(item, end=" ")

print()

# 判断字符串数据

name = "peter"
print(name.isalnum())  # 判断是否是字母和数字
print(name.isalpha())  # 判断是否是字母
print(name.isdigit())  # 判断是否是数字

# 1. 改动字符串中的数据

name = "peter"
print(name.capitalize())  # 首字母变大写

name = "peterpeter"
print(name.title())  # 把每个单词的首字母变大写

print(name.lower())  # 全小写
print(name.upper())  # 全大写
print(name.swapcase())  # 大写变小写，小写变大写

print(name.replace("peter", "nihao", 2))  # 替换子字符串[old_child_str, replace_str, count=None]，第三个参数最多替换次数,默认全部替换
print(name.split("p", -1))  # 根据 p 为分割边界 来分割字符串 [split_pos_str, max_count],返回 一个list存放切割后的字符组

str_msg = "hello world"

# slice[start:end:step] 切片，左闭右开

print(str_msg[2:5])
print(str_msg[2:])  # end 默认到底
print(str_msg[:3])  # start 默认起点
print(str_msg[::-1])  # 负号表示方向，从右往左去遍历

# 2. 删除字符串中的数据

name = "    hello "
print(name.strip())  # 删除两边的空格
print(name.lstrip())  # 删除左边的空格
print(name.rstrip())  # 删除右边的空格

# 3. 复制字符串

new_name = name  # new_name 是 name的引用

# id(obj) 取变量的地址

if id(new_name) == id(name):
    print("引用传递")

# 4. 查找字符串中的数据

data_str = "I love python"

print(data_str.count("l", 1, 1))  # [child_str, beg_pos, end_pos] 取子字符串数量

print(data_str.find("--"))  # 可以查找目标对象在序列对象的位置，找不到返回-1
print(data_str.index("lo"))  # 检测字符串是否包含子字符串，返回下标，找不到返回异常
print(data_str.startswith("I"))  # 检测字符串开头是否是子字符串，返回 true or false
print(data_str.endswith("I"))  # 检测字符串结尾是否是子字符串，返回 true or false
