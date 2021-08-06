# -*- coding:UTF-8 -*-
import os
import sys
import json
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

# s_path= 'G:/dataset/train_celebrity/a.png'
# ss=os.path.split(s_path)
# ss= os.path.basename(s_path)
# bb= ss.split('.')[0]
# print(ss,bb)

aaa = {}
aaa["req_id"] ="123123"
aaa["img_str"] ="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
aaa["algo_type"] ="1700000"

sss = json.dumps(aaa)
print(sss)

'''
req_id | string | 请求流水号
algo_type | string | 算法类型
code | string | 200 成功，其他失败
msg | string | 失败消息描述
label | string | 标签描述
socre | int | 得分
'''
bbb ={}
bbb["req_id"] ="123123"
bbb["algo_type"] ="1700000"
bbb["code"] ="200"
bbb["msg"] =""
bbb["label"] ="公文"
bbb["socre"] =99

sss = json.dumps(bbb)
print(sss)
