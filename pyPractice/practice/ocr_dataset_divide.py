# -*- coding:utf-8 -*-
import os
import random

import numpy as np
from sklearn.model_selection import train_test_split


def divide_arr(data, train_percent, val_percent):
    """
    divide dataset to train set,val set, test set,
    test_percent = 1 - train_percent - val_percent
    :param data: numpy arr to divide
    :param train_percent: train set percent
    :param val_percent:
    :return: train set,val set, test set
    """
    data_size = len(data)
    data = np.array(data)

    divide_index_train = int(round(data_size * train_percent))
    print(divide_index_train)
    divide_index_val = int(divide_index_train + round(data_size * val_percent))
    print(divide_index_val)

    indexes = np.array(range(0, data_size))

    random.shuffle(indexes)

    label_train = indexes[:divide_index_train]
    label_val = indexes[divide_index_train:divide_index_val]
    label_test = indexes[divide_index_val:data_size]

    return data[label_train], data[label_val], data[label_test]


def write_arr_to_file(data, dest_file_dir, dest_file_name="result.txt"):
    if os.path.isdir(dest_file_dir):
        with open(os.path.join(dest_file_dir, dest_file_name), "w", encoding="utf-8") as f:
            for i in data:
                f.write(i + "\n")
    else:
        print("dest dir is not dir")


dict_url = "F:\\code\\other\\TextRecognitionDataGenerator\\TextRecognitionDataGenerator\\dicts"
img_label_id_file = "label_id.txt"

data_list = []
with open(os.path.join(dict_url, img_label_id_file), "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        data_list.append(line)

data_list = np.array(data_list)

print(data_list)

label_train, label_val, label_test = divide_arr(data_list, 0.8, 0.1)

write_arr_to_file(label_train, dict_url, "label_train.txt")
write_arr_to_file(label_val, dict_url, "label_val.txt")
write_arr_to_file(label_test, dict_url, "label_test.txt")
