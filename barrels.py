from random import randint


class Cart:
    ### класс карточки ###
    def __init__(self):
        self._cart = []
        self._sterToWin = 15
        self.__create_cart()

    def action(self, number):
        for num, i in enumerate(self._cart):
            if number in i:
                self._cart[num][i.index(number)] = '-'
                self._sterToWin -= 1
                return True
        return False

    @property
    def is_win(self):
        return self._sterToWin == 0

    def print_cart(self):
        for i in self._cart:
            a = [conv(x) for x in i]
            print('|{:^3s}|{:^4s}|{:^4s}|{:^4s}|{:^4s}|{:^4s}|{:^4s}|{:^4s}|{:^4s}|'
                  .format(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8]))

    def __create_cart(self):
        check_list = []
        for row in range(0, 3):
            line = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
            for column in range(0, 5):
                while True:
                    a = randint(1, 91)
                    pos = a // 10
                    if pos == 9:
                        pos = 8
                    if type(line[pos]) == str and a not in check_list:
                        line[pos] = a
                        check_list.append(a)
                        break
                    else:
                        continue
            self._cart.append(line)


class User(Cart):
    ### класс игрок человке ###
    def __init__(self):
        Cart.__init__(self)

    def action(self, number):
        act = input('Зачеркнуть номер - Any Key/ Пропустить - Enter :')
        act = True if len(act) else False
        return act == super().action(number)


class Comp(Cart):
    ### класс игрок компьютер ###
    def __init__(self):
        Cart.__init__(self)

    def action(self, number):
        super().action(number)
        return True


# состояния игры
list_state = {'begin': 0, 'prepare': 1, 'game': 2, 'game over': 3}


class Game:
    ### класс игрового процесса ###
    def __init__(self):
        print('Добро пожаловать в игру бочонки')
        self._list_players = {}
        # список выпавших бочонков
        self._list_barrel = []
        # текущее состояние
        self._step_game = list_state['begin']

    @property
    def step_game(self):
        return self._step_game

    @property
    def max_players(self):
        return 2

    def add_user(self, name, type_user=1):
        if list(self._list_players.keys()).count(name) == 0:
            if type_user == 1:
                self._list_players[name] = User()
            else:
                self._list_players[name] = Comp()
            return True
        return False

    def barrel(self):
        while len(self._list_barrel) < 90:
            b = randint(1, 91)
            if b in self._list_barrel:
                continue
            else:
                yield b
                self._list_barrel.append(b)

    def prepare_game(self):
        ### Подготовка. Выбор игроков, до self.max_players ###
        print(f'Выбор игроков, до {self.max_players}')
        while True:
            choise = input('Добавить: 1 - игрока, 2 - компьютер, другое - вернуться в меню\n: ')
            if choise == '1':
                name = input('Укажите имя игрока: ')
                if len(name) == 0:
                    for i in range(self.max_players):
                        def_name = 'Игрок_' + str(i)
                        if self.add_user(def_name):
                            break
                elif not self.add_user(name):
                    print(f'Игрок с именем {name} существует, игрок не добавлен')
            elif choise == '2':
                for i in range(1, 5):
                    def_name = 'Компьютер_' + str(i)
                    if self.add_user(def_name, 2):
                        break
            else:
                self._step_game = list_state['begin']
                self._list_players.clear()
                return
            if len(self._list_players) == self.max_players:
                print(f'Игра началась. Игроки {", ".join(list(self._list_players.keys()))}.')
                self._step_game = list_state['game']
                return

    def start_game(self):
        for barrel in self.barrel():
            # показать карточки и выпавший бочонок
            print(f'Выпал бочонок {barrel}')
            for player in self._list_players:
                print('Карта игрока', player)
                self._list_players[player].print_cart()
                if not self._list_players[player].action(barrel):
                    winner = list(self._list_players.keys())
                    winner.remove(player)
                    print(f'Игра окончена игрок {player} ошибся. Игрок {winner[0]} победил')
                    self._step_game = list_state['game over']
                    return
                if self._list_players[player].is_win:
                    print(f'Игра окончена. Игрок {player} победил, закрыв всю карту')
                    self._step_game = list_state['game over']
                    return

    def menu_game(self):
        ### времени не хватило на сохранение игры ###
        # self._list_saves = game.gelSaveList()
        print('1 - Начать игру')
        # has_saves = len(self._list_saves)
        # if has_saves > 0:
        #     print('2 - Загрузить игру')
        action = input(': ')
        if action == '1':
            self._step_game = list_state['prepare']
        # if has_saves > 0:
        #     if action == '2':
        #         pass

    # @staticmethod
    # def gelSaveList():
    #     return list(filter(lambda s: s.endswith('.save'), os.listdir()))


def conv(x):
    return x if type(x) == str else str(x)


game = Game()
while True:
    if game.step_game == list_state['begin']:
        game.menu_game()
    elif game.step_game == list_state['prepare']:
        game.prepare_game()
    elif game.step_game == list_state['game']:
        game.start_game()
    elif game.step_game == list_state['game over']:
        input('Конец игры. Нажмите Enter для выхода')
        break
