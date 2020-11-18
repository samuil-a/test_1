
val1 = int(input('Сколько спортсмен пробежал в 1 день? >'))
val2 = int(input('К какому результату он стремится? >'))
day = 1
while 1:
    out_str = '%d-й день: %.2f' % (day, val1)
    print(out_str)
    if val1 > val2:
        break
    val1 *= 1.1
    day += 1
print(f'Ответ: на {day}-й день спортсмен достиг результата — не менее {val2} км')

