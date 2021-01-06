# !/usr/bin/env Python2
# -*- coding: utf-8 -*-
# @Author   : 得灵
# @FILE     : haffmanTree.py
# @Time     : 2020/12/28 18:11
# @Software : PyCharm
# @Introduce: This is 哈夫曼压缩

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
        # print self.char_codings
        # print type(eval(str(self.char_codings)))
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


hex_str = "080068616e646c696e6786020000200002006f00000009007a68756368756e79756f00000009007a68756368756e79750b000c0002000300687a6a03007a6379"

tmp_dict = {}
for ch in hex_str:
    if not (ch in tmp_dict):
        tmp_dict[ch] = 1
    else:
        tmp_dict[ch] += 1
ch_count_list = [(key, val) for key, val in tmp_dict.items()]
print ch_count_list
huffman_tree = HuffmanTree(ch_count_list)
