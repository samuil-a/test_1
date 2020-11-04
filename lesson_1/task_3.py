while 1:
    val = input('введите число >')
    if val.isdigit():
        if not 0 < int(val) < 10:
            break
    else:
        break
    out_str = f'считаем конечное число: {val}+{val*2}+{val*3}={int(val)+int(val*2)+int(val*3)}'
    print(out_str)
print("конец программы")
