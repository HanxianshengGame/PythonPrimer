# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 10_高级数据结构的公共方法.py
# @Time     : 2020/12/13 7:57
# @Software : PyCharm
# @Introduce: This is

# 共有方法操作

# + : 合并： 字符串，列表, 元组

first_str = "人生苦短"
second_str = "我用python"
print(first_str + second_str)

first_list = list(range(0, 10))
second_list = list(range(10, 20))
print(first_list + second_list)

# *： 重复复制： 字符串，列表，元组

print(first_list * 3)
print(first_str * 3)

# in:  判断对象是否存在:  字符串，列表，元组, 字典

print("人" in first_str)
first_dict = {"name": "韩镇江"}
print("name" in first_dict)
