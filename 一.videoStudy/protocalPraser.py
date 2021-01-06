# !/usr/bin/env Python2
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : protocalPraser.py
# @Time     : 2020/12/21 9:24
# @Software : PyCharm
# @Introduce: This is

import struct
import sys

# 将 ascii 编码改为 utf-8
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


# 哈夫曼编码
class TreeNode(object):
    def __init__(self, char=None, count=None):
        self.char = char
        self.count = count
        self.left = None
        self.right = None

    pass


class HuffmanTree(object):
    def __init__(self, char_count_dict):
        # 生成树的所有叶子结点
        self.leaves = [TreeNode(key, val) for key, val in char_count_dict.items()]
        while len(self.leaves) != 1:
            # 对叶子进行排序（按数量降序）
            self.leaves.sort(key=lambda node: node.count, reverse=True)
            # 对数量最小和次小的叶子进行合并为新树
            new_child_tree = TreeNode(count=self.leaves[-1].count +
                                            self.leaves[-2].count)
            new_child_tree.left = self.leaves.pop(-1)
            new_child_tree.right = self.leaves.pop(-1)
            self.leaves.append(new_child_tree)
        self.root = self.leaves[0]
        # path_codings  存放每条路径段的编码值（在递归生成叶子编码时使用）
        self.path_codings = range(16)
        self.char_codings = {}
        self.coding_chars = {}
        # 生成叶子编码 将 char-coding信息存入 self.char_codings self.coding_chars 中
        self.__generateLeavesCode(self.root, 0)
        pass

    def __generateLeavesCode(self, root_node, length):
        tmp_node = root_node
        if not tmp_node:
            return
        elif tmp_node.char:
            tmp_code = ""
            for i in range(length):
                tmp_code += self.path_codings[i]
            self.char_codings[tmp_node.char] = tmp_code
            self.coding_chars[tmp_code] = tmp_node.char
            return
        self.path_codings[length] = "0"
        self.__generateLeavesCode(tmp_node.left, length + 1)
        self.path_codings[length] = "1"
        self.__generateLeavesCode(tmp_node.right, length + 1)
        pass

    pass


# 协议解析器
class ProtoParser(object):
    # proto_sequence_list : 存放文本协议的所有变量名（有序）, 元素类型 （var_name, child）
    # var_name 是嵌套类型时，child是一个[],存放其子变量名字,否则为 -1
    __proto_sequence_list = []

    @property
    def proto_sequence_list(self):
        return self.__proto_sequence_list

    # proto_info_dict: 存放文本协议的所有变量信息（无序） 元素类型 key: var_name  value: (var_type, var_count, is_tuple)
    # var_type 是变量的类型，var_name 是嵌套类型时 var_type 为 dict, 存放了其 child变量信息
    # var_count 表示变量的数量，非数组就为 1，可变长数组为 -1（不确定），定长数组为 数组的大小
    # is_tuple: 是否是tuple （因为 [0] 与 [1]同样是数组）
    __proto_info_dict = {}

    @property
    def proto_info_dict(self):
        return self.__proto_info_dict

    # type_info_dict: 存放基本类型信息(无序) 元素类型 key: var_type   value: (byte_len, format_ch)
    # byte_len: 代表该类型所占字节数
    # format_ch: 代表使用struct模块处理类型的二进制时的格式符
    __type_info_dict = {"int8": (1, "b"),
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

    @property
    def type_info_dict(self):
        return self.__type_info_dict

    @staticmethod
    def __buildDescCore(proto_text):
        """
        建立对文本协议的描述存入 proto_sequence_list（存变量顺序）, proto_info_dict（存变量信息）
        注意：当检测到某个变量区块为嵌套类型时，会进行递归
        :param proto_text: 协议文本内容，遇到嵌套类型时会截取其嵌套类型块并进行递归
        :return: 返回一个  list,dict,end_pos 表示由该 proto_text 建立的 变量顺序与变量信息，
                 end_pos 用于嵌套类型块的文本建立描述完毕后回到函数入口时进行对原文本的位置的更改
        """
        result_list = []
        result_dict = {}

        proto_text = proto_text.strip()
        beg_pos = 1
        end_pos = len(proto_text)
        auxiliary_pos = 1

        while beg_pos != end_pos:
            # 检测到遍历位置为 { 时，表明为嵌套类型，需要递归
            if proto_text[beg_pos] == "{":
                result = ProtoParser.__buildDescCore(proto_text[beg_pos:end_pos:])
                beg_pos += result[2]

                auxiliary_pos = beg_pos
                var_count = 1
                is_tuple = False
                if proto_text[beg_pos] == "[":
                    is_tuple = True
                    while proto_text[beg_pos] != "]":
                        beg_pos += 1
                    var_count = -1 if auxiliary_pos + 1 == beg_pos else int(proto_text[auxiliary_pos + 1:beg_pos:])
                    beg_pos += 1
                    auxiliary_pos = beg_pos
                    pass

                while proto_text[beg_pos] != ";":
                    beg_pos += 1
                    pass
                var_name = proto_text[auxiliary_pos:beg_pos:].strip()
                result_list.append((var_name, result[0]))
                result_dict[var_name] = (result[1], var_count, is_tuple)
                beg_pos += 1
                auxiliary_pos = beg_pos
                pass
            # 检测到该位置为 } ，则需要返回
            elif proto_text[beg_pos] == "}":
                return result_list, result_dict, beg_pos + 1
                pass
            # 检测到该位置为 ;  ，则根据 auxiliary_pos 与 beg_pos 取出一个变量的信息并添加
            elif proto_text[beg_pos] == ";":
                variable_info = proto_text[auxiliary_pos:beg_pos:]
                variable_info = variable_info.strip()
                if variable_info.find(" ") != -1:
                    info_list = variable_info.split(" ", 1)
                else:
                    info_list = variable_info.split("]", 1)
                    info_list[0] += "]"
                info_list[0] = info_list[0].strip()
                info_list[1] = info_list[1].strip()
                var_count = 1
                is_tuple = False
                if info_list[0][-1::] == "]":
                    is_tuple = True
                    var_count = -1 if info_list[0][-2:-1] == "[" else int(info_list[0][-2:-1:])
                    if var_count == -1:
                        info_list[0] = info_list[0][0:-2]
                    else:
                        info_list[0] = info_list[0][0:-3]

                result_list.append((info_list[1], -1))
                result_dict[info_list[1]] = (info_list[0], var_count, is_tuple)
                beg_pos += 1
                auxiliary_pos = beg_pos
                pass
            else:
                beg_pos += 1
            pass
        return result_list, result_dict, end_pos

    def buildDesc(self, filename):
        """
        根据文件名得到协议文本，并建立对其协议的描述
        :param filename: 文件名
        :return: None
        """
        ProtoParser.__proto_sequence_list = []
        ProtoParser.__proto_info_dict = {}
        with open(filename, "rb") as file_obj:
            proto_text = file_obj.read()
        proto_text = proto_text.replace("\n", "").replace("\t", "")

        result = self.__buildDescCore(proto_text)

        ProtoParser.__proto_sequence_list = result[0]
        ProtoParser.__proto_info_dict = result[1]
        pass

    @staticmethod
    def dataPack(format_ch, pack_val):
        """
        打包后返回字符串
        :param pack_val: 打包的值
        :param format_ch: 值的格式化符
        :return: 返回打包后的结果 str
        """
        format_str = "<" + format_ch
        s = struct.Struct(format_str)
        return s.pack(pack_val)

    @staticmethod
    def dataUnpack(format_ch, unpack_str):
        """
        根据 pack_str 返回其数据结果
        :param format_ch: 解包值时的格式化符
        :param unpack_str: 需要解包的 str
        :return: 解包后的结果
        """
        s = struct.Struct("<" + format_ch)
        return s.unpack(unpack_str)[0]

    ## ================序列化================
    def __dumpsLen(self, len):
        """
        转存储长度（数组 or 字符串）
        :param len: 长度值
        :return: 16进制字符串
        """
        format_ch = self.type_info_dict["uint16"][1]
        packed_data = ProtoParser.dataPack(format_ch, len)
        return packed_data.encode("hex")

    def __dumpsSimpleType(self, var_name, var_value, proto_info_dict):
        """
        转储简单的基本类型（非组合，非数组）类型的数据
        :param var_name: 变量名
        :param var_value: 变量值
        :param proto_info_dict: 协议信息描述的 dict
        :return: 返回转储的字符串
        """
        dumps_len_str = ""
        format_ch = ""
        if type(var_value) == str:
            dumps_len = len(var_value)
            format_ch += str(dumps_len)
            dumps_len_str = self.__dumpsLen(dumps_len)

        format_ch += self.__type_info_dict[proto_info_dict[var_name][0]][1]
        packed_data = ProtoParser.dataPack(format_ch, var_value)
        dumps_data_str = packed_data.encode("hex")
        return dumps_len_str + dumps_data_str

    def __dumpsCore(self, data_dict, proto_sequence_list, proto_info_dict):
        """
        转储符合 协议 的数据，将其转换为 16进制字符串
        :param data_dict: 数据
        :param proto_sequence_list: 协议中变量的顺序列表（用于遍历）
        :param proto_info_dict: 协议信息描述的 dict
        :return: 返回转换后的 16进制字符串
        """
        result_str = ""
        for var_item in proto_sequence_list:
            var_name = var_item[0]
            var_value = data_dict[var_name]
            # 基本类型且单数的情况 获取pack的占位符，再获取val,字符串先打包进去一个uint16的长度
            if proto_info_dict[var_name][2]:
                is_fixed_length = False if proto_info_dict[var_name][1] == -1 else True
                # 可变长数组存储其长度
                if not is_fixed_length:
                    result_str += self.__dumpsLen(len(var_value))
                # 遍历数组取其元素并存储
                for elem in var_value:
                    if type(elem) == dict:
                        result_str += self.__dumpsCore(elem, var_item[1], proto_info_dict[var_name][0])
                    else:
                        result_str += self.__dumpsSimpleType(var_name, elem, proto_info_dict)
                pass
            elif type(var_value) == dict:
                result_str += self.__dumpsCore(var_value, var_item[1], proto_info_dict[var_name][0])
            else:
                result_str += self.__dumpsSimpleType(var_name, var_value, proto_info_dict)
            pass
        return result_str

    def dumps(self, d):
        return self.__dumpsCore(d, self.__proto_sequence_list, self.__proto_info_dict)

    ## ================反序列化================

    def __loadsLen(self, data_str):
        """
        将16进制字符串转换为长度
        :param data_str: 数据字符串（会进行截取需要转换为长度的部分，剩余部分返回）
        :return: result_len, result_data_str: 返回转换后的长度，与截取后剩余的字符串
        """
        len_info = self.type_info_dict["uint16"]
        len_data_str_len = len_info[0] * 2
        len_data_str = data_str[0:len_data_str_len:]
        result_data_str = data_str[len_data_str_len::]
        result_len = self.dataUnpack(len_info[1], len_data_str.decode("hex"))
        return result_len, result_data_str

    def __loadsSimpleType(self, var_name, data_str, proto_info_dict):
        """
        将16进制字符串转换为基本类型数据
        :param var_name: 变量名
        :param data_str: 16进制字符串
        :param proto_info_dict: 协议信息描述的 dcit
        :return: 结果数据
        """
        var_info = proto_info_dict[var_name]
        var_type_info = self.__type_info_dict[var_info[0]]
        content_len = var_type_info[0] * 2
        format_ch = var_type_info[1]
        if content_len == -1 * 2:  # 字符串
            result = self.__loadsLen(data_str)
            content_len = result[0] * 2
            data_str = result[1]
            format_ch = str(result[0]) + format_ch

        content_data_str = data_str[0:content_len:]
        result_data_str = data_str[content_len::]

        result_content = self.dataUnpack(format_ch,
                                         content_data_str.decode("hex"))
        return result_content, result_data_str

    def __loadsCore(self, data_str, proto_sequence_list, proto_info_dict):
        """
        从 16进制字符串中加载数据并存入 dict 中
        :param data_str: 16进制字符串
        :param proto_sequence_list: 协议序列列表
        :param proto_info_dict: 协议信息描述的 dict
        :return: 存放了数据的 dict （匹配proto_info_dict）
        """
        result_dict = {}
        for var_item in proto_sequence_list:
            var_name = var_item[0]
            var_info = proto_info_dict[var_name]
            var_count = var_info[1]
            if var_info[2]:
                if var_count == -1:
                    result = self.__loadsLen(data_str)
                    var_count = result[0]
                    data_str = result[1]
                    pass
                result_dict[var_name] = []
                while var_count:
                    pass
                    if type(var_info[0]) == dict:
                        result = self.__loadsCore(data_str,
                                                  var_item[1],
                                                  proto_info_dict[var_name][0])
                        result_dict[var_name].append(result[0])
                        data_str = result[1]
                    else:
                        result = self.__loadsSimpleType(var_name, data_str, proto_info_dict)
                        result_dict[var_name].append(result[0])
                        data_str = result[1]
                    var_count -= 1
                    pass
                result_dict[var_name] = tuple(result_dict[var_name])
                pass

            elif type(var_info[0]) == dict:  # 嵌套字典类型
                result = self.__loadsCore(data_str,
                                          var_item[1],
                                          proto_info_dict[var_name][0])
                result_dict[var_name] = result[0]
                data_str = result[1]
                pass
            else:  # 基本类型（string 与其他）
                result = self.__loadsSimpleType(var_name, data_str, proto_info_dict)
                result_dict[var_name] = result[0]
                data_str = result[1]
                pass

        return result_dict, data_str

    def loads(self, s):
        """
        通过 字符串 转换数据 dict, 按照规定协议去截取16进制字符串转换为数据并存入dict中
        :param s:
        :return:
        """
        return self.__loadsCore(s, self.__proto_sequence_list, self.__proto_info_dict)[0]
        pass

    ## ================压缩================
    def dumpComp(self, obj):
        """
        1.先得到16进制字符串，之后建立哈夫曼树（生成编码表与解析表），对16进制字符串进行编码
        2. 将编码后的二进制字符串与 头部（哈夫曼解析表）一起返回
        :param obj:
        :return: 哈夫曼解析表 与 编码二进制字符串
        """
        hex_str = self.dumps(obj)
        ch_count_dict = {}

        for ch in hex_str:
            if not (ch in ch_count_dict):
                ch_count_dict[ch] = 1
            else:
                ch_count_dict[ch] += 1
            pass
        huffman_tree = HuffmanTree(ch_count_dict)

        bin_str = ""
        for ch in hex_str:
            bin_str += huffman_tree.char_codings[ch]
            pass

        parser_dict_str = str(huffman_tree.coding_chars).replace(" ", "")

        return parser_dict_str + bin_str

    ## ================解压================
    def loadComp(self, s):
        """
        1. 拆分解析表与二进制数据字符串
        2. 利用解析表对二进制字符串进行解析为 16进制字符串
        3. 交予 self.loads 返回 dict
        :param s: parser_dict_str + bin_str
        :return: dict
        """
        end = s.find("}")
        parser_dict = eval(s[:end + 1:])
        bin_str = s[end + 1::]

        hex_str = ""
        tmp_str = ""
        for ch in bin_str:
            tmp_str += ch
            if tmp_str in parser_dict:
                hex_str += parser_dict[tmp_str]
                tmp_str = ""

        return self.loads(hex_str)


filename = "a.proto"
a1 = ProtoParser()
a1.buildDesc(filename)
print a1.proto_info_dict
print a1.proto_sequence_list
obj = {
    "name": "handling",
    "id": 646,
    "level": 32,
    "pet": ({

                "id": 111,
                "name": "zhuchunyu"
            },
            {

                "id": 111,
                "name": "zhuchunyu"
            }
    ),
    "x": (11, 12),
    "skill": ("hzj", "zcy")
}
binstr = a1.dumps(obj)
comp_bin_str = a1.dumpComp(obj)
print binstr
print comp_bin_str

a2 = ProtoParser()
a2.buildDesc(filename)
load_dict = a2.loads(binstr)
comp_load_dict = a2.loadComp(comp_bin_str)
