my_list = []
print("Наполните список данными\nчтобы закончить нажмите <Enter>")
while True:
    val = input("Новый элемент:")
    if not len(val):
        break
    my_list.append(val)
print("Получен список")
print(my_list)
for item in range(1, len(my_list), 2):
    my_list[item - 1], my_list[item] = my_list[item], my_list[item - 1]
print("Обработанный список")
print(my_list)
