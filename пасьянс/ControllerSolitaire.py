from model import *  # importing model module
from view import *  # importing view module
import sys  # importing sys library for exit()
import copy  # importing copy library for deepcopy()
import os

gamenumber = 0  # count the game for view.numberofthegame()
wincounter = 0  # count of win for view.printwin()


def session(gamenumber, wincounter):  # game start
    numberofthegame(gamenumber)  # print number of the game
    printwin(wincounter)  # print how much win you do in this session
    gamesteps = []  # list for sevegame()
    game = Game()  # start the model.Game() class
    idkc = 0  # counter for hint
    printing()  # print the rules from view.printing()

    def savegame():  # function for saving the game
        gamesteps.append(copy.deepcopy(game))  # deepcopy the model.Game() class (table and hand...)

    def printtable(availables1, difficult):  # printing the piramid
        for i in range(len(table)):
            k = []
            for j in table[i]:
                if str(type(j)) == "<class 'model.Card'>":
                    if j in availables1:
                        k.append((j.getfullcard() + '(' + str(availables1.index(j) + 1) + ')').center(7)) \
                            # printing fullcard and position of fullcard inside piramid
                    else:
                        if difficult == '2':  # if player was chose lvl 2 difficult
                            k.append('🂠'.center(8))
                        else:  # if player was chose lvl 1 difficult
                            k.append(j.getfullcard().center(7))
                else:
                    k.append(' '.center(7))
            print(''.join(k).center(50))  # printing the piramid

    def printhand():  # printing hand
        h = []
        for i in hand.gethand():
            h.append(i.getfullcard())
        return h

    input('Это помощь, её можно вызвать по команде "help"\nВведите что угодно для продолжения: ')
    astep = [1]  # creating variable for checking game status
    while not game.isgameover() and len(astep) != 0:  # checking game status

        table = game.gettable()  # get the table variable
        hand = game.getchand()  # get the hand variable
        availables = game.getavailables()  # get the availables variable
        curentpiramid()  # message
        printtable(availables, difficult)  # printing piramid
        c = hand.getcurrent()  # current hand
        p = hand.getprevious()  # previous hand
        if len(helpme(hand.gethand(), availables)) == 0:  # check the lose
            helping(False)
            printlose()  # print the lose message
            break
        if not hand.gethand():  # checking the fullness of the hand
            emptyhand()  # print the empty hand message
        elif p != '':  # checking the fullness of the previous hand
            print('Новая:',printhand()[c],'Предыдущая карта:',printhand()[p])  # printing current and previous hand
        else:
            print('Текущая карта',printhand()[c])  # printing current hand
        os.system("cls")
        inps = input('Ввод:')  # main input of the game
        os.system("cls")
        if inps == 'help':  # checking for the instruction message
            printing()  # printing the instruction from view module
        if inps.isdigit() and len(inps) == 1 and int(inps) <= len(availables):  # delete the king from piramid
            if availables[int(inps) - 1].getvalue() == 13:  # if card==king
                savegame()  # saving current status of the table before remove the card
                game.playedcard(availables[int(inps) - 1])  # remove the card from piramid
                cardwas(int(inps))  # showing the message about deleting card from piramid
                idkc = 0  # I dont know counter zeroing
            else:
                notking()  # showing the message about card!=king
        elif inps.isdigit() and len(inps) == 2 and int(inps[0]) <= len(availables) and int(inps[1]) <= len(availables):\
                # checking the input for 2 integer number and checking including to availables
            if availables[int(inps[0]) - 1].getvalue() + availables[int(inps[1]) - 1].getvalue() == 13: \
                    # checking for the sum=13
                savegame()  # save the game before deleting the card
                game.playedcard(availables[int(inps[0]) - 1])  # deleting first input card
                game.playedcard(availables[int(inps[1]) - 1])  # deleting second input card
                cardwas(int(inps[0]))  # showing the message about deleting card from piramid
                cardwas(int(inps[1]))  # showing the message about deleting card from piramid
                idkc = 0  # I dont know counter zeroing
            else:
                not13sum()  # showing the message about sum of the card != 13
        elif inps == 'c' and hand.getcard(c).getvalue() == 13:  # checking the input for 'c' for card in hand is king
            savegame()  # save the game before deleting the card
            handwas(hand.getcard(c).getfullcard())  # showing the message about the card from hand was delete
            game.playedcard(hand.getcard(c))  # deleting the king
            idkc = 0  # I dont know counter zeroing
        elif inps == 'c':  # checking the input for input='c'
            savegame()  # save the game before deleting the card
            hand.nextcurrent()  # switching the card in hand
            idkc = 0  # I dont know counter zeroing
        elif inps == 'cc' and p != '':  # checking the input and checking the previous card != empty
            if hand.getcard(c).getvalue() + hand.getcard(p).getvalue() == 13: \
                    # checking for the sum of 2 card from hand = 13
                savegame()  # save the game before deleting the card
                handwas(hand.getcard(c).getfullcard())  # showing the message about the card from hand was delete
                handwas(hand.getcard(p).getfullcard())  # showing the message about the card from hand was delete
                game.playedcard(hand.getcard(c))  # deleting the card from hand
                game.playedcard(hand.getcard(p))  # deleting the card from hand
                idkc = 0  # I dont know counter zeroing
        elif inps == 'idk':  # checking for input = 'idk' for showing hing
            astep = helpme(hand.gethand(),availables)  # getting hint from model module from helpme() function
            if len(astep) != 0:  # checking for fullness the hint list
                helping(True)  # showing hint message preview
                print(astep[idkc % len(astep)][0] + '+' + astep[idkc % len(astep)][1])  # showing the hint
                idkc += 1  # hint counter +=1 for the next lap
            if len(astep) == 0:  # checking for fullness hint list
                helping(False)  # showing message about hint list is empty
        elif not inps.isdigit() and len(inps) == 2:  # checking the input for the len=2 and not the digit
            if inps[0].isnumeric() and int(inps[0]) <= len(availables) and \
                    availables[int(inps[0]) - 1].getvalue() + hand.getcard(c).getvalue() == 13:  # checking for sum=13
                savegame()  # save the game before deleting the card
                handwas(hand.getcard(c).getfullcard())  # showing the message about the card from hand was delete
                game.playedcard(hand.getcard(c))  # deleting the card from hand
                cardwas(int(inps[0]))  # showing the message about deleting card from piramid
                game.playedcard(availables[int(inps[0]) - 1])  # deleting the card from piramid
                idkc = 0  # I dont know counter zeroing
            elif inps[1].isnumeric() and int(inps[1]) <= len(availables) and \
                    hand.getcard(c).getvalue() + availables[int(inps[1]) - 1].getvalue() == 13:  # checking for sum=13
                savegame()  # save the game before deleting the card
                handwas(hand.getcard(c).getfullcard())  # showing the message about the card from hand was delete
                game.playedcard(hand.getcard(c))  # deleting the card from hand
                cardwas(int(inps[1]))  # showing the message about deleting card from piramid
                game.playedcard(availables[int(inps[1]) - 1])  # deleting card from the piramid
                idkc = 0  # I dont know counter zeroing
        elif inps == 'Exit':  # checking input for 'Exit'
            break  # breaking the loop
        elif inps == 'back':  # checking the input for 'back'
            if gamesteps:  # checking the fullness of the gamestep list
                idkc = 0  # I dont know counter zeroing
                game = gamesteps.pop()  # rewriting the game variable
                stepback()  # showing message about stepback
            else:
                emptysave()  # showing message about the save list is empty
    if game.isgameover == True:  # checking for the win
        win()  # showing win message from view
        wincounter += 1  # adding 1 game to the wincounter
    else:
        brk()  # stopping the game


while True:  # cycle for restart the game and exit
    newgame()  # showing new game message
    inp = input('Ввод:')  # start input
    if inp == 'New':  # checking for input = 'New' as new game
        gamenumber += 1  # gamenumber counter += 1
        difficult = input('Уровень сложности от 1 до 2:')  # choosing difficult lvl
        session(gamenumber,wincounter)  # starting the game and sending info about winning game and gamecounter
    elif inp == 'Exit':  # checking the input for 'Exit'
        sys.exit(0)  # leaving from the game