from random import randint
from math import fsum
try:
    with open('task_5.txt', 'w', encoding='utf-8') as file_w:
        src = ', '.join([str(randint(1, 1000)) for i in range(20)])
        print(src)
        file_w.write(src)
    with open('task_5.txt', encoding='utf-8') as file_r:
        #можно было через seek сместь указатель на чтение
        dst = file_r.read().split(', ')
        dst = [int(i) for i in dst]
        print(fsum(dst))
except IOError:
    print('IOError')
