from itertools import cycle
import time


class TrafficLight:
    __color = None

    def __init__(self):
        self.__list_colors = {'красный': 7, 'желтый': 2, 'зеленый': 5}
        self.__iter = cycle(self.__list_colors)

    @staticmethod
    def __stime():
        return time.strftime("%H:%M:%S", time.localtime())

    def running(self):
        self.__color = next(self.__iter)
        print(f'{self.__stime()} установлен цвет {self.__color}')
        time.sleep(self.__list_colors[self.__color])


a = TrafficLight()
for i in range(1, 10):
    a.running()
