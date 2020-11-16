def div(arg1, arg2):
    return arg1/arg2


print("Программа деления.")
while True:
    try:
        val1 = float(input("\nВведите делимое:"))
        val2 = float(input("Введите делимое:"))
        print(f'Результат деления:{val1 / val2}')
    except ValueError:
        print("Некорректные данные, расчет невозможен")
        if input("Выйти из программы (да - Y(y))? :") in ('y', 'Y'):
            break
        continue
    except ZeroDivisionError:
        print("Деление на ноль невозможно")
print('\nКонец программы')
