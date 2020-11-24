keys = ('название', 'цена', 'количество', 'ед')
items = []
about = {}
out_information = {}
val = 0

print("Ввод товаров")
while val is not None:
    print("Новый товар")
    for num, key in enumerate(keys, 1):
        val = input(f'{key.title()}:')
        if len(val) == 0:
            val = None
            break
        # цена или количество
        if num & 2:
            val = int(val)
        about[key] = val
    else:
        items.append((len(items) + 1, about.copy()))
print("Информация о товарах")
tmp_list = []
for it in keys:
    tmp_list.clear()
    for i in items:
        tmp_list.append(dict(i[1])[it])
    out_information[it] = tmp_list.copy()
for i in out_information:
    print(f'{i}: {out_information[i]}')
