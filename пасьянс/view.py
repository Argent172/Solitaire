def newgame():
    print('Начать новую игру?Ввод "New"')
    print('Выход?Ввод "Exit"')

def numberofthegame(numbergame):
    print(('Игра №:' + str(numbergame)).center(50))

def printwin(wincount):
    print(('Побед в этой сессии: '+str(wincount)).center(50))

def printlose():
    print('Поражение(')

def curentpiramid():
    print('Текущий вид пирамиды:')


def helping(bools):
    if bools:
        print('Возможный ход:')
    else:
        print('Ходов больше нет!')


def emptyhand():
    print('Карты в руке закончились')


def curenthand():
    print('Новая и предыдущая карты руки:')


def printing():
    print('Инструкция:'.center(51))
    print('1.Выбор 2 карт из пирамиды?"2 номера"'.center(50))
    print('2.Выбор карты из пирамиды? "номер"'.center(45))
    print('3.Выбор карты из пирамиды + из руки? "номер+c"'.center(57))
    print('4.Объединение двух карт в руке(текущей и предыдущей)?"cc"'.center(69))
    print('5.Для смены карты в руке введите "c"'.center(48))
    print('6.Для вывода этого мануала введите "help"'.center(53))
    print('7.Начать новую игру?"New"'.center(37))
    print('8.Выход? "Exit"'.center(27))
    print('9.Отмена хода "back"'.center(31))
    print('10.Нужна подсказка?"idk"'.center(35))

def stepback():
    print('Действие отменено!')

def emptysave():
    print('Сохранения отсутствуют!')

def cardwas(inp):
    print('Карта №', inp, 'удалена')


def handwas(hand):
    print('Карта руки ', hand, ' удалена')


def not13sum():
    print('Сумма ценностей выбраных карт не равна 13!')


def notking():
    print('Выбраная карта не король!')


def brk():
    print('Вы успешно вышли из текущей игры')


def win():
    print('Congratulation!You WON!!!')
