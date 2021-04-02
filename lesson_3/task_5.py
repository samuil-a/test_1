def convert(arg):
    for num, i in enumerate(arg):
        try:
            arg[num] = float(i)
        except ValueError:
            return [0]
    return arg


end = 'q'
summ = 0
str = ''
print(f'программа расчета, завершается при вводе {end}')
while end not in str:
    str = input('Введите числа через пробел:')
    mas = str.split(end)[0]
    mas = mas.split()
    mas = convert(mas)
    summ += sum(mas)
    print(summ)
