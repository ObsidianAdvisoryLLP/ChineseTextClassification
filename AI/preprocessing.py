import json
import pandas as pd
import numpy as np

result_dict = {}

def combine_data():
    result = []
    for i in range(1,9):
        file_name = 'Status_Data'+str(i)+'.json'
        with open('./AI/data/ubs/UBS Weibo Data/weibo/'+file_name, "rb") as infile:
            result += json.load(infile)
    global result_dict
    for status in result:
        result_dict[status['id']] = status

labeled_data = []
def read_labels():
    global labeled_data
    with open('./AI/data/ubs/UBS Weibo Data/weibo/train_label.txt','r') as source:
        count = 0
        for line in source:
            fields = line.split('\t\t')
            if count == 0:
                sid = fields[0].split('\ufeff')[1]
                count += 1
            else:
                sid = fields[0]
            label = fields[1].split('\n')[0]
            status = result_dict[sid]
            del result_dict[sid]
            status['label'] = label
            labeled_data.append(status)

def shuffle_save_labeled_data():
    from random import shuffle
    for i in range(10):
        shuffle(labeled_data)

    total = len(labeled_data)
    train = int(total * 0.7)
    val = int(total * 0.1)
    test = total - train - val

    file = open('./AI/data/processed/ubs_train.txt', 'w')
    for status in labeled_data[:train]:
      line = str(status['label']) + '\t' + status['text'].replace('\u200b', '') + '\n'
      file.write(line)

    file = open('./AI/data/processed/ubs_test.txt', 'w')
    for status in labeled_data[train:train+test]:
      line = str(status['label']) + '\t' + status['text'].replace('\u200b', '') + '\n'
      file.write(line)

    file = open('./AI/data/processed/ubs_val.txt', 'w')
    for status in labeled_data[train+test:]:
      line = str(status['label']) + '\t' + status['text'].replace('\u200b', '') + '\n'
      file.write(line)

def get_labeled_unlabeled_data():
    combine_data()
    read_labels()
    unlabeled_data = []
    for key, value in result_dict.items():
        unlabeled_data.append(value)
    return labeled_data, unlabeled_data
