# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 9_字典.py
# @Time     : 2020/12/12 21:22
# @Software : PyCharm
# @Introduce: This is dict

# 字典： 是python中重要的数据结构
# 1. 键值对组成的集合，通常使用键访问数据效率比较高，支持数据的 增，删，改
# 2. 不是序列类型，没有下标的概念，是一个无序的键值集合，是内置的高级数据结构
# 3. 键 必须是不可变的类型 [元组， 字符串] 值可以是任意的类型
# 4. 每个键必定是唯一的，如果存在重复的键，则覆盖

# 基本创建使用字典

first_dict = {}  # 空字典
first_dict = {"pro": "艺术",
              "key": "value"}
print(type(first_dict))

first_dict["name"] = "李易峰"
first_dict["age"] = 30
first_dict["employee"] = "歌手"

print(first_dict)

# 查找键对应的值

print(first_dict["name"])  # 通过键获取对应的值

# 修改键对应的值

first_dict["name"] = "韩镇江"
first_dict.update({"age": 32})  # 可以添加或修改

# 获取所有的键

print(first_dict.keys())

# 获取所有的值

print(first_dict.values())

# 获取所有的数据项

print(first_dict.items())

# 遍历键值对

for key, value in first_dict.items():
    print("%s==%s" % (key, value))

# 删除一个键值对

del first_dict["name"]
first_dict.pop("age")

print(first_dict)

# 排序

print(sorted(first_dict.items(), key=lambda d: d[0]))  # 按key排序

second_dict = {"key1": "1",
               "key2": "2",
               "key3": "0"}
print(sorted(second_dict.items(), key=lambda d: d[1]))  # 按value排序
