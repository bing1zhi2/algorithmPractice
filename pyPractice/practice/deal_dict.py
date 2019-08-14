# -*- coding:utf-8 -*-
"""
将从网上找到的现代汉语通用字7000表转化成一行一个字的字典格式，

"""
import os

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
        f.write(i+"\n")
