from functools import reduce


def fact(x):
    for i in range(1, x + 1):
        f = [j for j in range(1, i + 1)]
        yield reduce(lambda a, b: a * b, f)


n = int(input('Введите конечное число для расчета факториалов:'))
fact(n)
for num, el in enumerate(fact(n), 1):
    print(f'{num}! = {el}')
