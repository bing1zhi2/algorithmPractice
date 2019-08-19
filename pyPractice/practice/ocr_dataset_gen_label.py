# -*- coding:utf-8 -*-
import os

dict_url = "F:\\code\\other\\TextRecognitionDataGenerator\\TextRecognitionDataGenerator\\dicts"
dict_filename = os.path.join(dict_url, "cn.txt")

word_dict = {}
with open(dict_filename, "r", encoding="utf-8") as f:
    for idx, line in enumerate(f):
        word_dict[line.strip()] = idx


img_label_url = dict_url
img_fname = "labels.txt"
img_label_file= os.path.join(img_label_url, img_fname)

img_label_id_file="label_id.txt"
img_label_id_file= os.path.join(img_label_url, img_label_id_file)

label_id_writer = open(img_label_id_file, "w")

with open(img_label_file, "r", encoding="utf-8") as f:
    for strs in f:
        line_list = strs.strip().split(" ")
        fname = line_list[:1]
        label = line_list[1:]

        label_id = []
        for i in label:
            id = word_dict[i]
            label_id.append(str(id))
        print(label_id)
        fname_str = ' '.join(fname)
        label_str = ' '.join(label_id)
        writeStr = fname_str + ' ' + label_str + "\n"
        print(writeStr)
        label_id_writer.write(writeStr)

    label_id_writer.close()







