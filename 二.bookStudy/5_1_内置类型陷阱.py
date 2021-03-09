# !/usr/bin/env Python2
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 5_1内置类型陷阱.py
# @Time     : 2021/1/6 18:49
# @Software : PyCharm
# @Introduce: This is


# [1] 赋值创建引用，而不是复制

L = [1,2, 3]
M = ['X', L, 'Y']
print(M)
L[1] = 0
print(M)


# 若非需要共享引用，请采纳分片和 copy/ copy.deepcopy


L = [1,2, 3]
M = ['X', L[:], 'Y']
print(M)
L[1] = 0
print(M)




# [2] 重复会增加层次深度

L = [4, 5, 6]
X = L * 4
Y = [L] * 4

print(X)
print(Y)  # 生成的是 4 个 L 的引用 [[],[],[],[]]

L[0] = 0     
print(X)     # 不变
print(Y)     # 联动修改


L = [4, 5, 6]
Y = [list(L)] * 4     # 实质是先拷贝了 L 一份，再生成4份相同的引用
L[1] = 0
print(Y)
Y[0][1] = 99
print(Y)


# [3] 注意(避免， 自己引用自己)循环数据结构

L = ['grail']
L.append(L)   # 避免
print(L)  

# [4] 不可变类型不可以在原位置修改

T = (1,2,3)
# T[1] = 3   # Error
T = T[:1] + (3,3)
print(T)
