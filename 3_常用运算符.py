# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 3_常用运算符.py
# @Time     : 2020/12/12 10:51
# @Software : PyCharm
# @Introduce: This is 运算符


# 算术运算符

a = 7
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)  # 注意 a / b 的类型会变为 float
print(type(a / b))
print(a % b)
print(a // b)  # 地板除 x//y结果是只保留整数位
print(a ** b)  # 幂等  a^b

# 比较运算符
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print(a > b)
print(a < b)

# 逻辑运算符

a, b, c, d = 23, 18, 10, 3
print(a + b > c and c < d)  # 等同与 && （短路操作）
print(a + b > c or c < d)  # 等同于 ||  （短路操作）
print(not a < b)  # 等同于 ！

# 赋值运算符

a = b
a += b
a -= b
a *= b
a /= b
a %= b
a //= b
a **= b  # 幂等  a = a^b
