# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 5_选择循环语句.py
# @Time     : 2020/12/12 13:52
# @Software : PyCharm
# @Introduce: This is 选择循环语句

# 1. if-else 语句

# 单分支：
# if 条件表达式
#     code
#     pass 结尾

score = 80
if score <= 60:
    print('成绩不是很理想')
    pass  # 空语句

print('if 语句运行结束')

# 双分支
# if 条件表达式:
#     code
#     pass 结尾
# else:
#     code
#     pass 结尾

if score > 60:
    print("成绩不错哦")
    pass
else:
    pass

# 多分支

# if 条件表达式：
#     code
#     pass 结尾
# elif 条件表达式:
#     code
#     pass 结尾
# else:
#     code
#     pass 结尾

score = int(input('请输入你的成绩：'))
if score > 90:
    print('A+')
    pass
elif score >= 80:
    print('B+')
    pass
elif score >= 70:
    print('C+')
    pass
else:
    print('D-')
    pass

# 嵌套 if-else

score = int(input("请输入你的成绩:"))
grade = int(input("请输入你的学分:"))

if score > 10:
    if grade >= 80:
        print("恭喜升级")
        pass
    else:
        print("很遗憾，你的成绩不达标")
        pass
else:
    print("您的表现也太差了把")
    pass

print('程序运行结束')

# 2. while 循环

# while 条件表达式:
#     code
#     pass

while True:
    print("1")
    break
    pass

# 九九乘法表
row = 1
while row <= 9:
    col = 1
    while col <= row:
        # end 是 重定义默认的换行操作
        print("%d * %d = %d" % (row, col, col * row), end=" ")
        col += 1
        pass
    print()
    row += 1
    pass

# 3. for 循环： 遍历操作，依次取集合容器的每个值

# for 临时变量 in 字符串，列表:
#     code
#     code
#     pass

sentense = "我是一个中国人"
for chinese_character in sentense:
    print(chinese_character)
    pass

# range 此函数可以生成一个数据集合列表
# range(起始,结束，步长)  步长不能为0, 左闭右开区间
my_list = range(1, 100, 1)

sum = 0
for single_val in range(1, 101):
    sum += single_val
    pass

print("sum=%d" % sum)

# 5. break 与 continue

sum = 0
for item in range(1, 101):
    if sum > 100:
        print("循环执行到 %d 退出" % item)
        break
        pass
    sum += item
    pass

for item in range(1, 101):
    if item % 2 == 0:
        continue
        pass
    print(item)
    pass

# 6. for-------else , while-----else 只要循环内没有出现break就会执行else

for item in range(1, 11):
    if item >= 5:
        break
else:
    print("就是在上面循环中，只要是出现了break 那么else的"
          "代码将不会再执行,for--else 适用于倒计次数的例子")

account = "han1534930844@163.com"
pwd = "123"
for i in range(3):  # range(0,3)
    input_account = input("请输入账号：")
    input_password = input("请输入密码：")
    if account == input_password and input_password == pwd:
        print("恭喜你登录成功")
        break
else:
    print("您的账号已经被锁定由于多次密码错误")

index = 1
while index <= 10:
    index += 1
    if index == 6:
        break
else:
    print("我退出了")
