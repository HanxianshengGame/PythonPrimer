# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : protoPraser.py
# @Time     : 2020/12/16 9:43
# @Software : PyCharm
# @Introduce: This is

# 一. 协议文本制作规则

"""
{
     变量类型 变量名
     变量类型 变量名
}

1. 以  { } 开始 和 结束
2. 变量类型 变量名 ，中间存在多个空格（至少一个），每个声明式由分号分割(分号前可能存在多个空格)
3. 字段与字段之间存有 换行符，制表符，空格
4. 变量名的命名规则符合 c 语言规则

{
  string name;
  int32  id ;   uint16 level;
}

"""

# 二. 变量类型分为基本类型和组合类型，基本类型和组合类型也会有其对应数组类型
import struct
import binascii

"""
基本类型：

int8	8位有符号整数	1
uint8	8位无符号整数	1
int16	16位有符号整数	2
uint16	16位无符号整数	2
int32	32位有符号整数	4
uint32	32位无符号整数	4
float	单精度浮点	    4
double	双精度浮点	    8
bool	布尔（1真0假）	1
string	字符串	        2+L

注意： L 为字符串长度，本身占 2字节， 字符串内容为 utf-8 编码

组合类型: 若干个任意类型字段的组合体，类似于C语言中的结构体，以“{”开始，“}”结束，

{
   {
      int32  id;
      string name;
   } pet;
   string name;
}


数组类型分两种：

1. 变长数组，表示为 T[], T表示变量类型
2. 定长数组，表示为 T[N], T表示变量类型，N是正整数常量
int 16[5] x;
string [] strs;
{
   bool flag;
   string name;
   int32  id;
} []AOS;

"""

# 三. 序列化规则

"""
1. 结构化对象的每个字段以协议描述文本中出现的顺序依次进行序列化
2. 每种基本类型的数值遵循 C 语言规范的小端格式序列化为二进制格式
3. 除了变长数组和字符串，类型信息本身不会被序列化
4. 对于字符串，其长度值作为 uint16 数值被序列化，然后按字符串头到尾的顺序
对每个字符进行序列化
5. 对于变长数组，其长度作为 uint16 数值被序列化，然后按数组头到尾的顺序对每个数组元素进行序列化。
6. 组合类型的序列化是紧凑的，即不需要考虑字段间字节对齐问题而产生padding。

string a;
uint16[] b;
float[2] c;
bool f;

050068656c6c6f03000c0040000104000048419a9905c201
"""


class ProtoParser(object):
    proto_dict = {}
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

    def __init__(self):
        pass

    @staticmethod
    def DataPack(placeholder_ch, val):
        format_str = "<" + placeholder_ch
        s = struct.Struct(format_str)
        if type(val) == str:
            return s.pack(val.encode(encoding="utf-8"))
        return s.pack(val)

    @staticmethod
    def DataUnpack(placeholder_ch, byte_buffer):
        s = struct.Struct("<" + placeholder_ch)
        return s.unpack(byte_buffer)

    @classmethod
    def __buildDescCore(cls, proto_content):
        info_dict = {}

        proto_content = proto_content.strip()
        beg_pos = 1
        end_pos = len(proto_content)
        auxiliary_pos = 1

        while beg_pos != end_pos:
            if proto_content[beg_pos] == "{":
                result = cls.__buildDescCore(proto_content[beg_pos:end_pos:])
                beg_pos += result[1]

                auxiliary_pos = beg_pos
                var_count = 1
                if proto_content[beg_pos] == "[":
                    while proto_content[beg_pos] != "]":
                        beg_pos += 1
                    var_count = -1 if auxiliary_pos + 1 == beg_pos else int(proto_content[auxiliary_pos + 1:beg_pos:])
                    beg_pos += 1
                    auxiliary_pos = beg_pos
                    pass

                while proto_content[beg_pos] != ";":
                    beg_pos += 1
                    pass
                var_name = proto_content[auxiliary_pos:beg_pos:].strip()
                info_dict[var_name] = (result[0], var_count)
                beg_pos += 1
                auxiliary_pos = beg_pos
                pass
            elif proto_content[beg_pos] == "}":
                return info_dict, beg_pos + 1
                pass
            elif proto_content[beg_pos] == ";":
                variable_info = proto_content[auxiliary_pos:beg_pos:]
                variable_info = variable_info.strip()
                if variable_info.find(" ") != -1:
                    info_list = variable_info.split(" ")
                else:
                    info_list = variable_info.split("]")
                    info_list[0] += "]"
                info_list[0] = info_list[0].strip()
                info_list[1] = info_list[1].strip()
                var_count = 1
                if info_list[0][-1::] == "]":
                    var_count = -1 if info_list[0][-2:-1] == "[" else int(info_list[0][-2:-1:])
                    if var_count == -1:
                        info_list[0] = info_list[0][0:-2]
                    else:
                        info_list[0] = info_list[0][0:-3]
                info_dict[info_list[1]] = (info_list[0], var_count)
                beg_pos += 1
                auxiliary_pos = beg_pos
                pass
            else:
                beg_pos += 1
            pass

        return info_dict, end_pos

    def buildDesc(self, filename):
        ProtoParser.proto_dict = {}
        file_obj = open(filename, "r", encoding="utf-8")
        proto_content = file_obj.read()
        file_obj.close()
        proto_content = proto_content.replace("\n", "").replace("\t", "")

        print(proto_content)

        ProtoParser.proto_dict = self.__buildDescCore(proto_content)[0]
        pass

    ## ================序列化================

    # 转存储数组或字符串长度
    def __dumpsLen(self, len):
        placeholder_ch = self.type_dict["uint16"][1]
        pack_data = ProtoParser.DataPack(placeholder_ch, len)
        return binascii.hexlify(pack_data).decode(encoding="utf-8")
        # 转存储基本类型

    def __dumpsSimpleType(self, var_name, var_value, proto_dict):
        dumps_len_str = ""
        placeholder_ch = ""
        if type(var_value) == str:
            # 避免汉字被记录为 1字节，将 字符串进行转换为 bytes 再进行 len
            dumps_len = len(var_value.encode(encoding="utf-8"))
            placeholder_ch += str(dumps_len)
            dumps_len_str = self.__dumpsLen(dumps_len)

        placeholder_ch += self.type_dict[proto_dict[var_name][0]][1]
        pack_data = ProtoParser.DataPack(placeholder_ch, var_value)
        dumps_data_str = binascii.hexlify(pack_data).decode(encoding="utf-8")
        return dumps_len_str + dumps_data_str

    def __dumpsCore(self, data_dict, proto_dict):
        result_str = ""
        for var_name, var_value in data_dict.items():
            # 基本类型且单数的情况 获取pack的占位符，再获取val,字符串先打包进去一个uint16的长度
            if type(var_value) == tuple:
                is_fixed_length = False if proto_dict[var_name][1] == -1 else True
                # 可变长数组存储其长度
                if not is_fixed_length:
                    result_str += self.__dumpsLen(len(var_value))
                # 遍历数组取其元素并存储
                for elem in var_value:
                    if type(elem) == dict:
                        result_str += self.__dumpsCore(elem, proto_dict[var_name][0])
                    else:
                        result_str += self.__dumpsSimpleType(var_name, elem, proto_dict)
                pass
            elif type(var_value) == dict:
                result_str += self.__dumpsCore(var_value, proto_dict[var_name][0])
            else:
                result_str += self.__dumpsSimpleType(var_name, var_value, proto_dict)
            pass

        return result_str

    def dumps(self, d):
        return self.__dumpsCore(d, self.proto_dict)

    ## ================反序列化================

    def __loadsLen(self):
        pass
    def __loadsSimpleType(self):
        pass
    def __loadsCore(self):
        pass

    def loads(self, s):
        result_dict = {}

        return result_dict
        pass

    ## ================压缩================
    def dumpComp(self, obj):
        pass

    ## ================解压================
    def loadComp(self, s):
        pass


parser = ProtoParser()
parser.buildDesc("a.proto")
print(parser.proto_dict)
obj = {
    "name": "骨精灵",
    "id": 5201314,
    "married": False,
    "friends": (5201315, 244578811),
    "position": (134.5, 0.0, 23.41),
    "pet": {
        "name": "骨精灵的小可爱",
        "skill": (
            {
                "id": 1,
            },
            {
                "id": 2,
            })
    }
}

serialize_str = parser.dumps(obj)
print(serialize_str)