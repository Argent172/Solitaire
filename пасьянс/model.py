from random import randint


def helpme(hand, availables):
    astep = []
    for i in range(len(hand)):
        for j in range(len(availables)):
            if hand[i].getvalue() + availables[j].getvalue() == 13 and \
                    ([hand[i].getfullcard(), availables[j].getfullcard()] not in astep):
                astep.append([hand[i].getfullcard() + 'h', availables[j].getfullcard() + 'p'])
            if availables[j].getvalue == 13 and [availables[j].getfullcard()] not in astep:
                astep.append([availables[j].getfullcard() + 'p'])
    for i in range(len(availables)):
        for j in range(len(availables)):
            if availables[i].getvalue() + availables[j].getvalue() == 13 and \
                    ([availables[i].getfullcard(), availables[j].getfullcard()]) not in astep:
                astep.append([availables[i].getfullcard() + 'p', availables[j].getfullcard() + 'p'])
    return astep


class Game:

    def __init__(self):
        self.masti = ['♥', '♦', '♠', '♣']
        self.stash = [i for i in range(52)]
        self.gamesteps = []
        self.availables = []
        self.table = [[] for i in range(7)]
        self.hand = Hand()
        self.razdacha()


    def razdacha(self):
        for i in range(7):
            for j in range(i+1):
                randstash = self.stash.pop(randint(0, len(self.stash)-1))
                self.table[i].append(Card(randstash % 13+1, self.masti[randstash//13], i, j))
        for i in range(len(self.stash)):
            randstash = self.stash.pop(randint(0, len(self.stash)-1))
            self.hand.add(Card(randstash % 13+1, self.masti[randstash//13]))
        self.setavailables()

    def setavailables(self):
        availables = [0*i for i in range(7)]
        table = self.table
        for i in range(1, 7):
            for j in range(i):
                if table[i][j] == ' ' and table[i][j + 1] == ' ' and table[i - 1][j] != ' ':
                    availables[j] = table[i - 1][j]
        for j in range(len(table)):
            if table[6][j] != ' ':
                availables[j] = table[6][j]
        self.availables = [i for i in availables if i != 0]
    
    def getavailables(self):
        return self.availables

    def gethand(self):
        return self.hand.gethand()

    def getchand(self):
        return self.hand
    
    def gettable(self):
        return self.table
    
    def playedcard(self, card):
        if card in self.gethand():
            self.hand.remove(card)
        if card.geti() != '':
            self.table[card.geti()][card.getj()] = ' '
            card.getoutoftable()
            self.setavailables()
            
    def isgameover(self):
        return self.table[0][0] == ' '


class Card:
    value = 0
    mast = ''
    i = ''
    j = ''
    
    def __init__(self, value, mast, i='', j=''):
        self.value = value
        self.mast = mast
        if i != '' and j != '':
            self.i = i
            self.j = j
           
    def getvalue(self):
        return self.value

    def getmast(self):
        return self.mast
    
    def geti(self):
        return self.i
    
    def getj(self):
        return self.j
    
    def getfullcard(self):
        return str(self.value)+self.mast

    def getoutoftable(self):
        self.i = ''
        self.j = ''


class Hand:
    def __init__(self):
        self.hand = []
        self.current = 0
        self.isEmp = False
        self.first = True
        self.firstLap = True

    def nextcurrent(self):
        self.current += 1
        if self.current >= len(self.hand):
            self.current = 0
            self.firstLap = False
        self.first = False

    def getcurrent(self):
        return self.hand[self.current]

    def getprevious(self):
        if self.first:
            return ''
        elif self.firstLap and self.current == 0:
            return 0
        else:
            return self.hand[self.current-1]

    def add(self, card):
        self.hand.append(card)

    def getcard(self, index):
        if index >= len(self.hand):
            return None
        if not self.isEmp:
            return self.hand[index]

    def gethand(self):
        return self.hand

    def remove(self, card):
        if not self.isEmp:
            self.hand.pop(self.hand.index(card))
            self.current -= 1
            if len(self.hand) == 0:
                self.isEmp = True
            if self.current >= len(self.hand) or self.current < 0:
                self.current = 0
            return ''