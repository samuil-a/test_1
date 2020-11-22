n_t = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыри'}
try:
    with open('task_4.txt', encoding='utf-8') as file:
        data = file.read()
        # удаляю симвом кодирования, почему он добавился?
        data = data[1:]
        for key in n_t:
            data = data.replace(key, n_t[key])
        with open('task_4_w.txt', 'w', encoding='utf-8') as file_w:
            file_w.write(data)
except IOError:
    print('IOError')
