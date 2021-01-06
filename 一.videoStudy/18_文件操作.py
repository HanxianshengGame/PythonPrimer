# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : 18_文件操作.py
# @Time     : 2020/12/14 21:24
# @Software : PyCharm
# @Introduce: This is

# 1. 文件打开操作

# 默认的编码是 gbk，这个是中文编码，最好打开时指定其编码类型

file_obj = open("test.txt", "w", encoding="utf-8")

# 2. 写操作

file_obj.write("在苍茫的大海上")

file_obj.close()

#  以二进制格式打开一个文件用于写入

file_obj = open("test.txt", "wb")  # str-->bytes
file_obj.write("在乌云与大海之间".encode("utf-8"))  # 加码
file_obj.close()

# 3. 读操作

file_obj = open("test.txt", "r", encoding="utf-8")
# print(file_obj.read())    # 读取所有数据
# print(file_obj.read(12))  # 读取指定字节
file_obj.readline()
file_obj.close()

# 二进制读
file_obj = open("test.txt", "rb")
print(file_obj.read().decode("utf-8"))  # 解码
file_obj.close()

# 4. with 上下文管理
# with语句，不管在处理文件过程中是否发生异常，都能保证with
# 语句执行关闭后已经关闭打开的文件句柄

with open("test.txt", "rb") as f:
    print(f.read().decode("utf-8"))
    pass

"""
总结：
r r+ 只读，普通读取场景
rb rb+ 适用于文件图片视频音频的文件读取
w wb+ w+ 每次都会去创建文件
a ab a+ 在原有的文件基础上进行文件末尾追加

注意编码问题
"""



def copyBigFile():
    old_file = input("请输入备份的文件名")
    file_list = old_file.split(".")
    new_file = file_list[0] + "_备份." + file_list[1]

    try:
        with open(old_file, "rb") as old_file, open(new_file, "wb") as new_file:
            while True:
                content = old_file.read(1024).decode("utf-8")
                new_file.write(content.encode("utf-8"))
                if len(content) < 1024:
                    break

    except Exception as msg:
        print(msg)


# 5. tell() 文件定位(光标在文件中的位置)

with open("test.txt", "r", encoding="utf-8") as file_obj:
    print(file_obj.read(1024))
    print(file_obj.tell())


# 6. truncate  对原文件进行截取操作，或者制造文件空洞

file_obj = open("test.txt", "r", encoding="utf-8")
print(file_obj.read())
file_obj.close()

file_obj = open("test.txt", "r+", encoding="utf-8")
file_obj.truncate(15)
print(file_obj.read())
file_obj.close()

# seek() 更改文件位置

file_obj = open("test.txt", "r+", encoding="utf-8")

# offset： 偏移量，  whence: 0为开头，1为当前，2 为末尾
file_obj.seek(4,0)
file_obj.close()

