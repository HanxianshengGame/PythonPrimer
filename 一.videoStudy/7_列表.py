# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 7_列表.py
# @Time     : 2020/12/12 20:13
# @Software : PyCharm
# @Introduce: This is list 列表

# 1. 是python 当中非常重要的数据结构， 是一种有序的数据集合
# 2. 列表中的数据是可以变化的，【数据项值可以变化，内存地址不会改变】
# 3. 支持增删查改
# 4. 用[]来表示列表类型，数据项之间用逗号来分割，注意：数据项可以是任何类型的数据
# 5. 支持索引和切片来进行操作

# first_list = []  # 空列表
first_list = [1, 2, 3, "你好"]

print(type(first_list))
print(len(first_list))  # len 函数可以获取到集合/列表的数据个数

print(first_list)  # 输出完整的列表
print(first_list[::-1])  # reverse
print(first_list[0])  # 输出第一个元素
print(first_list[:3])  # 切片输出
print(first_list * 3)  # 输出多次

# 1. 查找

second_list = ["abcd", 785, 12.23, True]

# [elem_val, start_pos, end_pos]
print(second_list.index(785, 0, len(second_list)))

# 2. 追加

third_list = ["abcd", 785, 12.23, True]
print(third_list)
third_list.append(["fff", "ddd"])  # 追加一个列表项（类型是列表）
third_list.append("ss")
print(third_list)

third_list.insert(1, "insert_data")  # 插入操作 [insert_pos, elem]
print(third_list)

fourth_list = list(range(10))  # 为列表随机扩展10个空间
third_list.extend(fourth_list)  # 拓展等于批量追加
print(third_list)

# 3. 修改

fifth_list = ["abcd", 785, 12.23, True]
fifth_list[0] = 1
print(fifth_list)

# 4. 删除

sixth_list = ["abcd", 785, 12.23, True]
del sixth_list[0]  # 删除列表中第一个元素
print(sixth_list)
del sixth_list[1:3]  # 删除列表中角标 [1,3) 的元素
print(sixth_list)

sixth_list.remove(785)  # 移除指定的元素值
print(sixth_list)

sixth_list.extend([1, 2, 3, 4, 5])
sixth_list.pop(1)  # 移除指定的元素项 [角标]
print(sixth_list)

# 5. list comprehension 列表推导式子

students = [("hzj", 25), ("elaine", 24),
            ("john", 34)]

# 将 30 岁以上的学生信息取出
print([student for student in students if student[1] > 30])

temp_list = []
for student in students:
    if student[1] > 30:
        temp_list.append(student)

print(temp_list)

# 将 30 岁以上的学生名字取出
print([student[0] for student in students if student[1] > 30])

temp_list = []
for student in students:
    if student[1] > 30:
        temp_list.append(student[0])

print(temp_list)
