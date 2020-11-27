# скрипт с использование count
from itertools import count
from sys import argv

if len(argv) >= 2:
    arg_start = argv[1]
    if not arg_start.isdigit():
        arg_start = 0
    else:
        arg_start = int(arg_start)
    for i in count(arg_start):
        print(i)
        if i > arg_start+20:
            break
