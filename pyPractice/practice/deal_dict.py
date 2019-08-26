# -*- coding:utf-8 -*-
"""
将从网上找到的现代汉语通用字7000表转化成一行一个字的字典格式，

"""
import os
import collections


def change():
    fileName = os.path.join("F:\\", "dict.txt")

    result = []
    with open(fileName, "r", encoding="utf-8") as f:
        line = f.readline()
        for i in line:
            result.append(i)
        print(line)

    # result.sort()

    fileName2 = os.path.join("F:\\", "dict_order.txt")

    with open(fileName2, "w", encoding="utf-8") as f:
        for i in result:
            f.write(i + "\n")


def merge_dict():
    fileName2 = os.path.join("/media/chenhao/study", "dict.txt")
    fileName3 = os.path.join("/media/chenhao/study", "char_std_5990.txt")

    result = []

    with open(fileName2, "r", encoding="utf-8") as f:
        line = f.readline()
        for i in line:
            result.append(i)

    obj = collections.Counter(result)
    print(len(obj.keys()))

    original_charlist = []
    with open(fileName3, "r", encoding="utf-8") as f:
        for i in f:
            original_charlist.append(i.strip())

    obj.update(original_charlist)

    print(obj.keys())
    print(len(obj.keys()))
    all_words = list(obj.keys())

    fileName4 = os.path.join("/media/chenhao/study", "char_7476.txt")

    all_words.sort()
    print(all_words)

    with open(fileName4, "w", encoding="utf-8") as f:
        for li in all_words:
            f.write(str(li) + "\n")


merge_dict()
