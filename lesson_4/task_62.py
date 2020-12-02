# скрипт с использование cycle
from itertools import cycle
from sys import argv

if len(argv) >= 2:
    in_list = argv[1:]
    for num, i in enumerate(cycle(in_list)):
        print(i)
        if num > len(in_list) * 5:
            break
