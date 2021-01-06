# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 飞机大战项目.py
# @Time     : 2020/12/14 20:54
# @Software : PyCharm
# @Introduce: This is

# plane pro 需求分析
"""
1. 对象

我方飞机，敌方飞机，我方子弹，敌方子弹

2. 功能

我方飞机可以移动 [根据按键来控制的]
敌方飞机也可以移动 [随机的自动移动]

双方飞机都可以发送子弹

步骤：
创建一个窗口
创建一个我方飞机，根据方向键左右的移动
给我方飞机添加发射子弹的功能 【按下空格键去发送】

创建一个敌人飞机
敌人飞机可以自由的移动
敌人飞机可以自动的发射子弹
"""


# 引用第三方模块
import pygame
from pygame.locals import *
