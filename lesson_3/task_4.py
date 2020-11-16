def my_func1(x, y):
    return x ** y


def my_func2(x, y):
    rez = 1.
    for i in range(y, 0):
        rez /= x
    return rez


print('программа расчета')
while True:
    try:
        val1 = float(input('\nВведите действительное число:'))
        val2 = int(input('Введите целое отрицательное число:'))
        if val2 >= 0:
            print('Второе число не соответствует требованиям\n')
            continue
        print(f'результат вычисления 1-й функцией {my_func1(val1, val2)}')
        print(f'результат вычисления 2-й функцией {my_func2(val1, val2)}')
    except ValueError:
        print("Введены некорректные данные")
        if input('Выйти из программы (да - Y(y))? :') in ('y', 'Y'):
            break
