class Stationery:
    def __init__(self):
        self._title = ''

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
        Stationery.__init__(self)

    def draw(self):
        print('Рисую, только бы чернила не высохли')


class Pencil(Stationery):
    def __init__(self):
        Stationery.__init__(self)

    def draw(self):
        print('Рисую даже в космосе')


class Handle(Stationery):
    def __init__(self):
        Stationery.__init__(self)

    def draw(self):
        print('Выделяю все что написано ручкой')


obj = Stationery()
obj.draw()
obj = Pen()
obj.draw()
obj = Pencil()
obj.draw()
obj = Handle()
obj.draw()