with open('task_1.txt', 'w', encoding='utf-8') as file:
    data = []
    while True:
        s = input('ВВедите текст:')
        if len(s) == 0:
            break
        data.append(s)
    file.writelines('\n'.join(data))
