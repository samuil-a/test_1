var = float(input("введите вещественное число >"))
out_val = "число с точкой: %.3f теперь строка %s" % (var, repr(var))
print(out_val)

var = int(input("введите целое число >"))
out_val = 'чивло в 10-й системе %d и в 16-й системе %x' % (var, var)
print(out_val)

var = input("введите строку >")
if len(var):
    out_str = 'буквы {1} и {2} является частью строки {0}'.format(var, var[0], var[-1])
    print(out_str)
else:
    print("увы строка пуста")
