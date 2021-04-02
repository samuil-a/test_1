# -*- coding: utf-8 -*-
class Car:
    _speed = None
    _color = None
    _name = None
    _is_police = None

    def __init__(self, s, c, n, p=False):
        self._speed = s
        self._color = c
        self._name = n
        if type(p) == bool:
            self._is_police = p
        else:
            self._is_police = False

    def go(self):
        if self._speed == 0:
            print('Машина поехала')
            self._speed = 1
        else:
            self._speed += 10
        self.show_speed()

    def stop(self):
        if self._speed != 0:
            print('Машина остановилась')
            self._speed = 0
        else:
            print('Машина и так стоит')

    def turn(self, direction):
        if self._speed == 0:
            print("Сначала нужно тронуться")
            return
        way = 'назад'
        if direction == 'a':
            way = 'налево'
        elif direction == 'd':
            way = 'направо'
        print(f'Машина повернула {way}')

    def show_speed(self):
        print(f'Скорость={self._speed}')

    def color(self):
        return self._color

    def name(self):
        return self._name

    def is_police(self):
        return self._is_police


class TownCar(Car):
    def __init__(self, c):
        Car.__init__(self, 0, c, 'Малолитражка', False)

    def show_speed(self):
        Car.show_speed(self)
        if self._speed > 60:
            print(f'{self.name()} превысила скорость')


class WorkCar(Car):
    def __init__(self, c):
        Car.__init__(self, 0, c, 'Газелька', False)

    def show_speed(self):
        Car.show_speed()
        if self._speed > 40:
            print(f'{self.name()} превысила скорость')


class SportCar(Car):
    def __init__(self, c):
        Car.__init__(self, 0, c, 'Ферари', False)


class PoliceCar(Car):
    def __init__(self, c):
        Car.__init__(self, 0, c, 'Бобик', True)


print('Симулятор езды')
while True:
    color = input('Какого цвета хотите машину? :')
    if len(color) == 0 or len(color) > 10:
        color = 'черная'
    print(f'Так и знал что {color}')

    # print(f'{name} - хорошее имя для машины')
    type_car = input('Выберите машину: 1-Малитражка, 2-Спорткар, 3-Газелька, 4-Полиция :')
    if type_car == '1':
        typeCar = TownCar(color)
    elif type_car == '2':
        typeCar = SportCar(color)
    elif type_car == '3':
        typeCar = WorkCar(color)
    elif type_car == '4':
        typeCar = PoliceCar(color)
    else:
        typeCar = TownCar(color)
    print(f'В городе новый автомобиль {typeCar.color()} {typeCar.name()}')
    print(f'Мы {"" if typeCar.is_police() is True else "не "}едем блюсти порядок')
    print(f'Управление: w-прибавить скорости, s-стоп, a-налево, d-направо, остальное отмена')
    print('ПОехали, жми кнопки')
    while True:
        cmd = input('Действие:')
        if len(cmd) == 0:
            print('Ты выпрыгнул из машины на ходу, идешь в гараж')
            break
        cmd = cmd[0]
        if cmd == 'w':
            typeCar.go()
        elif cmd in ['a', 'd']:
            typeCar.turn(cmd)
        elif cmd == 's':
            typeCar.stop()
        else:
            print('Ты выпрыгнул из машины на ходу, идешь в гараж')
            break
    ex = input('Катаемся дальше? ( Да - y ):')
    if ex != 'y':
        break
print('Конец программы')
