def my_func(val1, val2, val3):
    if val1 > val2:
        val1 += val2 if val2 > val3 else val3
        return val1
    else:
        val2 += val1 if val1 > val3 else val3
        return val2


print('программа расчета')
while True:
    try:
        arg1 = int(input('Введите 1-й аргумент:'))
        arg2 = int(input('Введите 2-й аргумент:'))
        arg3 = int(input('Введите 3-й аргумент:'))
        print(f'Результат: {my_func(arg1, arg2, arg3)}')
    except ValueError:
        print("Введены некорректные данные")
        if input('Выйти из программы (да - Y(y))? :') in ('y', 'Y'):
            break
