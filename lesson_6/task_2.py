class Road:
    __weight = 25
    __thick = 2

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calc(self):
        return self.__length * self.__width * self.__weight * self.__thick


try:
    road = Road(int(input('Длинна дороги:')), int(input('Ширина дороги:')))
    print(f'Масса дорожного полотна ровна {road.calc()}')
except ValueError:
    print('Введены некорректные данные')
