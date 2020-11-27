# с лябдой не заладилось
def convert(s):
    return 0 if s.find('(') == -1 else int(s[:s.find('(')])


try:
    with open('task_6.txt', encoding='utf-8') as file:
        data = file.readlines()
        data[0] = data[0][1:]
        lessons = {}
        for s_data in data:
            items = s_data.split()
            lessons[items[0][:-1]] = sum([convert(i) for i in items[1:]])
        print(lessons)
except IOError:
    print('IOError')
