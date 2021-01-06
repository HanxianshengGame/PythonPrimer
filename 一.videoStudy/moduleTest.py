# !/usr/bin/env Python2
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : moduleTest.py
# @Time     : 2020/12/15 18:27
# @Software : PyCharm
# @Introduce: This is
import binascii
import struct
import sys

defaultencoding = 'utf-8'

if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

type_dict = {"int8": (1, "b"),
             "uint8": (1, "B"),
             "int16": (2, "h"),
             "uint16": (2, "H"),
             "int32": (4, "i"),
             "uint32": (4, "I"),
             "float": (4, "f"),
             "double": (8, "d"),
             "bool": (1, "?"),
             "string": (-1, "s")  # 特殊 2+L暂定
             }


def DataPack(placeholder_ch, val):
    s = struct.Struct("<" + placeholder_ch)
    return s.pack(val)


def DataUnpack(placeholder_ch, byte_buffer):
    s = struct.Struct("<" + placeholder_ch)
    return s.unpack(byte_buffer)


packed_data = DataPack("i", 4)
print(packed_data)
output_data = packed_data.encode("hex")  # 变为字符串
print output_data

# 压缩工作
bin_str = ""
for hex_ch in output_data:
    hex_num = int(eval("0x" + hex_ch))
    tmp_str = ""
    while hex_num != 0:
        tmp_str += str(hex_num % 2)
        hex_num = int(hex_num / 2)
    while len(tmp_str) < 4:
        tmp_str += "0"

    bin_str += tmp_str[::-1]
print bin_str

comp_str = ""
for index in range(0, len(bin_str), 8):
    pow_num = 8
    tmp_num = 0
    while pow_num:
        tmp_num += int(bin_str[index]) * pow(2, pow_num-1)
        pow_num -= 1
        index += 1
    comp_str += chr(tmp_num)
    pass
print comp_str
print 1
print comp_str.encode("hex")

result_str = ""
for index in range(0, len(bin_str), 4):
    tmp_num = 0
    pow_num = 4
    while pow_num:
        tmp_num += int(bin_str[index]) * pow(2, pow_num - 1)
        pow_num -= 1
        index += 1
    result_str += hex(tmp_num)[2::]
    pass

print result_str

output_data = output_data.decode("hex")
print output_data
output_data = output_data
print(DataUnpack("i", output_data)[0])
#
# if type(1) == int:
#     print(1)
# print(len("你好".encode(encoding="utf-8")))
#
# print len("骨精灵")
