from math import fsum
try:
    tmp = {}
    with open('task_3.txt', encoding='utf-8') as file:
        for line in file:
            items = line.split()
            tmp[items[0]] = int(items[1])
        lv = tmp.values()
        workers = list(filter(lambda i: tmp[i] < 20, tmp.keys()))
        print('Средняя зарплата {}'.format(fsum(lv)/len(lv)))
        print('Зарплата меньше 20 у сотрудников: {}'.format(', '.join(workers)))
except IOError:
    print('IOError')
