print('Укажите в фирме "Рога и копыта"')
val1 = float(input('выручку >'))
val2 = float(input('издержки >'))
rez = 'Фирма работает '
if val1 > val2:
    print('Фирма работает с прибылью')
    val2 = int(input('введите количество сотрудников >'))
    print(f'Прибыль составила {val1/val2} рублей на сотрудника')
elif val1 < val2:
    print('Фирма работает в убыток')
else:
    print('Фирма работает в ноль')
