# -*- coding:UTF-8 -*-
import os
import sys

# print(os.listdir('G:/ml'))
# src_path, _ = os.path.split(os.path.realpath(__file__))
# print(src_path, _)
# print(' '.join(sys.argv))
#
# path_exp = os.path.expanduser('G:/ML/dataset/lfw/raw')
# print('path_exp: ',path_exp)
# classes = os.listdir(path_exp)
# print(classes)
# classes.sort()
# nrof_classes = len(classes)
# for i in range(nrof_classes):
#     class_name = classes[i]
#     facedir = os.path.join(path_exp, class_name)
#     print(facedir)

s_path= 'G:/dataset/train_celebrity/celebrity_mtcnnpy_182\\10000207\\1517662845,2845745492_align.png'
ss=os.path.split(s_path)
print(ss)