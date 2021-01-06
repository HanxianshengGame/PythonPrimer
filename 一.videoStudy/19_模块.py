# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 19_模块.py
# @Time     : 2020/12/15 9:27
# @Software : PyCharm
# @Introduce: This is

# 模块： 工具包库

# 调用模块的方法： 模块名.函数名


# 1. 导入模块

"""

模块搜索路径：
1. 本目录搜索
2. 环境变量搜索， 使用 sys.path 查看所有路径
3. 搜索默认路径，linux路径  /usr/local/bin/python/

"""
# 导入所有有3步:
# 1. 打开文件
# 2. 执行模块对应的文件，将执行过程中产生的名字都丢到模块的名字空间
# 3. 在程序中会有一个模块的名称指向模块的名称空间中

# 导入所有
import time as myTime  # 使用 as 重新声明模块名

print(myTime.ctime())

# 导入部分的三个步骤
# 1. 以模块为准创造一个模块的名称空间
# 2. 执行模块对应的文件，将执行过程中产生的名字都丢到模块的名称空间
# 3. 在当前执行文件的名称空间拿到一个名字，该名字直接指向模块中的某一个名字
# 优点：不用加模块前缀  缺点： 容易产生名字冲突

# 导入部分

from time import ctime
from time import *

print(ctime())

# 2. os 模块操作文件

"""
对文件进行重命名，删除等一些操作，可以使用 os 模块

os模块提供一些系统级别的操作命令
"""

import os
import shutil

# os.rename("test.txt", "test_重命名.txt")
# os.remove("test_重命名.txt")
# os.mkdir("test_dir")
# os.rmdir("test_dir")
# os.mkdir("d:/python") # 不能创建多级目录
# os.makedirs("d:/python/sub") # 可创建多级目录
# os.rmdir("d:/python") # 只能删除空目录
# shutil.rmtree("d:/python") # 递归删除所有

# print(os.getcwd())  # 获取当前目录
# print(os.path.join(os.getcwd(), "venv")) # 拼接路径

# print(os.listdir("e:/"))  # 获取该级目录的目录列表
# print(os.scandir("d:/"))  # 获取该级目录的目录列表现代化写法
with os.scandir("d:/") as entries:
    for entry in entries:
        print(entry.name)

base_path = os.getcwd()


def printTreeDir(base_path):
    for entry in os.listdir(base_path):
        file_path = os.path.join(base_path, entry)
        if os.path.isfile(file_path):
            print(file_path)
        if os.path.isdir(file_path):
            printTreeDir(file_path)


printTreeDir(base_path)


# 3. 模块的制作

"""
1. 在python中，一个 .py文件就是一个模块
"""
# 导入自定义模块
# import moduleTest
from moduleTest import add


print(__name__)