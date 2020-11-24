class Worker:
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, *args):
        self.name, self.surname, self.position, self._income['wage'], self._income['bonus'] = args


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


while True:
    try:
        print('Заполнение анкет сотрудников')
        name = input('Имя')
        if len(name) == 0:
            break
        sur = input('Фамилия')
        if len(sur) == 0:
            break
        pos = input('Должность')
        if len(pos) == 0:
            break
        wage = int(input('Оклад'))
        bonus = int(input('Премия'))
        p = Position(name, sur, pos, wage, bonus)
        print(f'Зарплата {p.get_full_name()} = {p.get_total_income()}')
    except ValueError:
        break
print("Введены некорректные данные, выход из программы")
