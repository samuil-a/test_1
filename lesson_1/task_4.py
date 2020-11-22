in_val = input('введите число >')
if in_val.isdigit():
    val = int(in_val)
    big_num = 0
    while val:
        num = val % 10
        if num > big_num:
            big_num = num
        val = val // 10
    val = f' {big_num} самая большая цифра в числе {in_val}'
    print(val)
else:
    print("некорректный ввод. конец программы")


