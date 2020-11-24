f_name = 'task_2.txt'
try:
    with open(f_name, encoding='utf-8') as file:
        for line in file:
            print(len(line.split()))
except IOError:
    print('Ошибка чтения файла{}'.format(f_name))
