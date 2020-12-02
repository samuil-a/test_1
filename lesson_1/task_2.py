def to_str(in_val):
    return str(in_val).rjust(2, "0")
val = input('введите время в секундах >')
if val.isdigit():
    val = int(val)
    out_str = f'Вы ввели время: {to_str(val // 3600)}:{to_str(val % 3600 // 60)}:{to_str(val % 60)}'
    print(out_str)
else:
    print("некорректный ввод. конец программы")
