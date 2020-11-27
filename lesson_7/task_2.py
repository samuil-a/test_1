from abc import ABC, abstractmethod
from math import ceil


class Clothes(ABC):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def material(self):
        pass

    @staticmethod
    def suf(val):

        if val > 4:
            return 'ов'
        elif val > 1:
            return 'а'
        else:
            return ''

class Coat(Clothes):
    def __init__(self, size):
        Clothes.__init__(self, 'Пальто')
        self._size = size

    @property
    def size(self):
        return self._size

    def material(self):
        return ceil(self._size / 6.5 + 0.5)


class Suit(Clothes):
    def __init__(self, height):
        Clothes.__init__(self, 'Костюм')
        self._height = height

    @property
    def height(self):
        return self._height

    def material(self):
        return ceil(self._height * 2 / 100 + 0.3)


print('Расчет материала для вашего гардероба\nиспользуется российская система размеров')
while True:
    try:
        coat = Coat(int(input('Ваш размер одежды :')))
        suit = Suit(int(input('Ваш рост :')))
        print(f'Для пошива {coat.name} {coat.size} размера понадобится {coat.material()} метр{coat.suf(coat.material())} материала')
        print(f'Для пошива {suit.name} {suit.height} роста понадобится {suit.material()} метр{suit.suf(suit.material())} материала')
    except ValueError:
        print('Вы ввели некорректные значения.')
    if input('Выйти из программы у - да: ') == 'y':
        break
