print('Построение рейтинга\nдля завершения ввода данных введите не вещественное число')
rate_list = []
while True:
    val = input('Добавить рейтинг:')
    if not val.isdigit():
        break
    val = int(val)
    if val < 1:
        print(f'{val} - не корректное значение')
    try:
        pos = rate_list.index(val, -1)
        pos += 1
        print(f'добавляем в позицию {pos}')
        rate_list.insert(pos, val)
    except ValueError:
        if len(rate_list) != 0:
            for i in range(0,len(rate_list)):
                if val > rate_list[i]:
                    rate_list.insert(i, val)
                    break
            else:
                rate_list.append(val)
        else:
            rate_list.append(val)
        # rate_list.append(val)
        # rate_list.sort(reverse=True)
    print(f'рейтинг {rate_list}')
print('Конец программы')
