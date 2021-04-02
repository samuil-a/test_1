from random import randint


class Matrix:
    def __init__(self, arg):
        self._matrix = arg

    def __str__(self):
        return '\n'.join(' '.join(str(b) for b in a) for a in self._matrix)

    @property
    def matrix(self):
        return self._matrix

    def __add__(self, other):
        if len(self._matrix) == len(other.matrix) and len(self._matrix[0]) == len(other.matrix[0]):
            return Matrix([[self._matrix[a][b]+other.matrix[a][b] for b in range(0, len(self._matrix[0]))] for a in range(0, len(self._matrix))])
        else:
            return "Нельзя складывать матрины разной размерности"


i = 0
j = 0


def create_lists():
    return [[randint(1, 100) for a in range(0, j)] for b in range(0, i)]


print('Постороение матрицы')
while True:
    sz = input('Задайте через пробел размеры (строки столбцы), напримир 2 2 :').split()
    try:
        i = int(sz[0])
        j = int(sz[1])
        values = create_lists()
        matrix1 = Matrix(values)
        print(f'Создана 1-я матрица\n{matrix1}')
        values = create_lists()
        matrix2 = Matrix(values)
        print(f'Создана 2-я матрица\n{matrix2}')
        print(f'Результат сложения \n{matrix1 + matrix2}')
        break
    except ValueError:
        print("Ошибка, указано не число")
        continue
    except IndexError:
        print('Мало параметров')
        continue

