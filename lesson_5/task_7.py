# coding: utf-8
from math import fsum
import json

try:
    with open('task_7.txt', encoding='utf-8') as file:
        data = file.readlines()
        data[0] = data[0][1:]
        firms = {}
        for s_data in data:
            items = s_data.split()
            tmp = int(items[2]) - int(items[3])
            if tmp < 9:
                continue
            firms[items[0]] = tmp
        aver = {'average_profit': int(fsum(firms.values()) / len(firms))}
        with open('task_7_json.txt', 'w', encoding='utf-8') as file_j:
            json.dump([firms, aver], file_j)
except IOError:
    print('IOError')
