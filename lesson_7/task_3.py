from math import floor


class Cell:
    def __init__(self, pieces):
        if pieces < 1:
            self._pieces = 1
            print('Даже не надейся создать дефективную клетку, создаю одноклеточного')
        else:
            self._pieces = pieces

    @property
    def pieces(self):
        return self._pieces

    def __add__(self, other):
        return Cell(self._pieces + other.pieces)

    def __sub__(self, other):
        rez = self._pieces - other.pieces
        if rez > 0:
            return Cell(rez)
        else:
            print('Разность клеток имеет не натуральное значение')

    def __mul__(self, other):
        return Cell(self._pieces * other.pieces)

    def __truediv__(self, other):
        return Cell(floor(self._pieces / other.pieces))

    def make_order(self, columns):
        if type(columns) != int:
            print('Ошибка, columns не int')
        elif columns < 1:
            print('Ошибка, columns должен быть бошьше нуля')
        else:
            self._count = -1
            self._columns = columns
            str = ''
            for el in self:
                str += el
            print(str)

    def __iter__(self):
        return self

    def __next__(self):
        self._count += 1
        if self._count < self._pieces and self._count%self._columns == 0 and self._count:
            return '\n*'
        elif self._count < self._pieces:
            return '*'
        else:
            raise StopIteration

    def __str__(self):
        return str(self._pieces)


while True:
    try:
        cell1 = Cell(int(input('Размер базовой клетки: ')))
        print(f'Размер 1 клетки = {cell1}')
        cell2 = Cell(5)
        print(f'Сумма с клеткой размером {cell2} = {cell1+cell2}')
        print(f'Разность с клеткой размером {cell2} = {cell1 - cell2}')
        print(f'Разность с клеткой размером {Cell(100)} = {cell1 - Cell(100)}')
        print(f'Умножение с клеткой размером {cell2} = {cell1 * cell2}')
        print(f'Деление на клетку размером {cell2} = {cell1 / cell2}')
        cell2 = Cell(100)
        print(f'Деление на клетку размером {cell2} = {cell1 / cell2}')
        print(f'Раскладываем клетку на молекулы')
        cell1.make_order(int(input('По сколько в рядочек? :')))
    except ValueError:
        print('Вы ввели некорректные значение.')
    if input('Выйти из программы у - да: ') == 'y':
        break
