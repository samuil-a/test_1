# словари
seasons = {1: "зима", 2: "весна", 3: "лето", 4: "осень"}
months = {1: 1, 2: 1, 3: 2, 4: 2, 5: 2, 6: 3, 7: 3, 8: 3, 9: 4, 10: 4, 11: 4, 12: 1}
val = None

while True:
    val = input("введите номер месяца:")
    if not val.isdigit():
        print("Ошибка. Вы ввели не число")
        continue
    val = int(val)
    if val < 1 or 12 < val:
        print("Ошибка. Введено недопустимое значение, допустимы значения от 1 до 12")
        continue
    break
print(f"указаный месяц относится к периоду {seasons[months[val]]}")

# списки
seasons_list = ("зима", "весна", "лето", "осень")
months_list = (0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 0)

while True:
    val = input("введите номер месяца:")
    if not val.isdigit():
        print("Ошибка. Вы ввели не число")
        continue
    val = int(val)
    if val < 1 or 12 < val:
        print("Ошибка. Введено недопустимое значение, допустимы значения от 1 до 12")
        continue
    break
val -= 1
print(f"указаный месяц относится к периоду {seasons_list[months_list[val]]}")
