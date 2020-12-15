# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 13_python内置函数.py
# @Time     : 2020/12/13 17:29
# @Software : PyCharm
# @Introduce: This is python 内置函数

# 1. 数学运算

#  abs 取绝对值

print(abs(-1))

# round : 取浮点类型的近似值

print(round(3.66, 1))

# pow 求次方

print(pow(3.3, 3))

# max 求最大值

print(max([1, 12, 12]))

# min 最小值

# sum() 求和

# 语法： sum(iterable[,start)
print(sum(range(50)))

# eval() 动态执行字符串表达式

a, b, c = 1, 2, 3
print(eval("a+b+c"))
print(eval("e+f+g", {"e": 1, "f": 2, "g": 3}))


def testFunc():
    print("我执行了")


eval("testFunc()")

# 2. 类型转换

int()
float()
str()

ord("a")  # char 转数字
chr(85)  # 数字转字符 ASIC
bool()
bin(16)  # 二进制
hex(23)  # 16进制

first_tuple = (1, 2, 3, 4)
first_list = list(first_tuple)  # 元组转列表

first_tuple = tuple(first_list)  # 列表转元组

dic = dict(name="小明", age=18)
dic["name"] = "小明"

print(bytes("我喜欢python", encoding="utf-8"))

# 3. 序列操作函数


# all() 函数判定给定的可迭代参数 iterable 中的所有元素是否都为TRUE
# 对象中的元素除了0，空， FALSE 外都算 TRUE
first_tuple = [()]
print(all(first_tuple))

# any() 函数判定给定的可迭代参数 iterable 中的是否有一个元素为TRUE
# 对象中的元素除了0，空， FALSE 外都算 TRUE

first_tuple = [(), 1]
print(any(first_tuple))

# sort与sorted 带d的都不会在原始对象进行操作，而是返回新的，不带d的会操作到原对象
# sorted() 函数对所有可迭代的对象进行排序(返回一个新的结果)

first_list = [1, 523, 42, 34]
first_list = sorted(first_list, reverse=True)
print(first_list)

# list.sort() 函数对 list 可迭代对象进行排序 (会更改到原始对象)

first_list = [1, 523, 42, 34]
first_list.sort(reverse=True)
print(first_list)

# list.reverse() 和 reversed

reversed(first_list)
first_list.reverse()

# range() 函数可创建一个整数列表， 一般在for循环中
# 语法： range(beg_num, end_num, step)
print(range(0, 10, 2))

# zip()  函数将可迭代对象（可多个元素一一对应）
#        作为参数，将对象中对应的元素打包成一个个元组
#        然后返回由这些元组组成的列表

# 如果各个迭代器的元素不一致，则返回列表长度与最段的对象相同，利用*号，可解压为列表

s1 = ["a", "b", "c"]
s2 = ["你", "我", "他", 1]
print(list(zip(s1, s2)))


def bookInfo():
    book_name = input("请输入书名，以空格分割: ")
    book_count = input("请输入书的数量，以空格分割: ")
    name_list = book_name.split(" ")
    count_list = book_count.split(" ")
    book_infos = list(zip(name_list, count_list))
    print([book_info for book_info in book_infos])


# bookInfo()


# enumerate(): 函数用于将可遍历的数据对象组合成一个索引序列(一般用于for循环中)

first_list = ["a", "b", "c"]
for index, item in enumerate(first_list, 5):
    print(index, item)

first_dict = {}
first_dict["name"] = "handling"
first_dict["hobby"] = "sing"

for index, key in enumerate(first_dict):
    print(key)

# 4. set 集合：是python中的一个数据结构，是一个无序且不重复的元素集合(不支持索引和切片)
# 只有key没有value

first_set = {1, 2, 3, 1}
print(first_set)
print(type(first_set))

first_set.add("python")
first_set.remove("python")
first_set.clear()

# set.difference 求差集 (a-b   a中存在，b中不存在)

first_set = {1, 2, 3}
second_set = {2, 3}
print(first_set.difference(second_set))
print(first_set - second_set)

# set.intersection 求并集 (a&b a中存在，b中也存在)

print(first_set.intersection(second_set))
print(first_set & second_set)

# set.union 并集操作 (a|b a和b累加)

print(first_set.union(second_set))
print(first_set | second_set)

# pop 就是从集合中拿第一个数据并且删除

first_set.pop()
print(first_set)

# update 更新集合  和并集类似

a = {1, 2, 3}
b = {4, 5, 6}
a.update(b)
print(a)


