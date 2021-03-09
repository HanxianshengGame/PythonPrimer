# !/usr/bin/env Python2
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 6_python语句简介.py
# @Time     : 2021/1/6 18:49
# @Software : PyCharm
# @Introduce: This is


# python 语句大全

'''
 语句            功能           
[1] 赋值         创建引用
[2] 调用表达式   运行函数
[3] print 调用   打印对象
[4] if/elif/else 选择动作
[5] for/else     序列迭代
[6] while/else   通用循环
[7] pass         空占位符
[8] break        循环退出
[9] continue     循环继续
[10] def         函数方法
[11] return      函数结果
[12] yield       生成器函数          
[13] global      命名空间             
[14] nonlocal    命名空间
[15] import      获取模块
[16] from        获取属性
[17] class       构建对象
[18] try/except/finally 捕获异常
[19] raise       触发异常
[20] assert      调试检查
[21] with/as     上下文管理器
[22] del         删除引用
'''


# [1] 编写规范

mylist = [111, 
          222,
          333]

x = ( 1 + 2 + 
      3 + 4)

if (x == 1 and 
    2 == 2 and
    2 == 3):
    print('spam' * 3)
