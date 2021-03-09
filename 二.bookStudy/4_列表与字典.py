# !/usr/bin/env Python2
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 4_列表与字典.py
# @Time     : 2021/1/6 18:48
# @Software : PyCharm
# @Introduce: This is

D1 = {'1': 2}
D2 = {'name': 'bob', 1:'2'}
D3 = dict([('name', 'bob'), ('age', 40)])
keys = []
vals = []
D4 = dict(zip(keys, vals))
D5 = dict.fromkeys(['a','b'])

print ('age' in D5)
print (D1.values())
print D1.items()
D6 = D1.copy()
print D6 is D1
D6['1'] = 2
print D1
D1.clear()
D1.update(D2)
print D1.get('1', 1) # 通过键获取，得不到返回第二个参数（默认设置None）
print D1.pop('1', 2) # 通过键删除，失败返回 第二个参数
D1.setdefault('111', 3) # 通过键获取，不存在时设置为  键：默认值
D1['111'] = 42 #新增修改键
print len(D1)

# 将值映射为键
table = { 'holy' : '1975'}
V = '1975'
print ([key for (key, val) in table.items() if val == V])


import copy

X = { 'A' : 1,
    'B' : 2,
    'C' : {'1': 1}}

# 嵌套字典类型，使用 deepcopy() 更为合适
x = copy.deepcopy(X)



# 字典比较操作: 比较键

print '111' 

"""
注意: 
1. 序列运算无效
2. 对新索引赋值会添加项
3. 键不一定总是字符串
"""