# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : moduleTest.py
# @Time     : 2020/12/15 18:27
# @Software : PyCharm
# @Introduce: This is
import binascii
import struct

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


packed_data = DataPack("i", 5201314)
print(packed_data)
output_data = binascii.hexlify(packed_data).decode(encoding="utf-8")   # 变为字符串
output_data = output_data.encode(encoding="utf-8")
print(DataUnpack("i", binascii.unhexlify(output_data)))

if type(1) == int:
    print(1)

print(len("你好".encode(encoding="utf-8")))



