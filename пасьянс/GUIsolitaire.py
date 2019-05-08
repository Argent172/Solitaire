import os
from model import *
from view import *
import copy
import sys
from PyQt5 import QtWidgets,uic
import ctypes
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *

class Main(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.ui = uic.loadUi("solit.ui")
        self.user32 = ctypes.windll.user32
        self.width = self.user32.GetSystemMetrics(0)
        self.height = self.user32.GetSystemMetrics(1)
        self.width = int(self.width / 21.3)
        self.height = int(self.height / 8)
        self.selected = False
        self.ui.Openmenubtn.clicked.connect(self.wasclicked)
        self.ui.Newgamebtn.clicked.connect(self.wasclicked)
        self.ui.Savegamebtn.clicked.connect(self.wasclicked)
        self.ui.Settingsbtn.clicked.connect(self.wasclicked)
        self.ui.Exitbtn.clicked.connect(self.wasclicked)
        self.ui.Cmpbtn.clicked.connect(self.wasclicked)
        self.ui.Mexitbtn.clicked.connect(self.wasclicked)
        self.ui.Swapbtn.clicked.connect(self.wasclicked)
        self.ui.Settingsbtn.clicked.connect(self.wasclicked)
        self.ui.Updbtn.clicked.connect(self.wasclicked)
        self.checked()
        self.ui.clickchbox.stateChanged.connect(self.checked)
        self.ui.dndchbox.stateChanged.connect(self.checked)


        if self.ui.label_00.text() == '00':
            self.ui.Cmpbtn.hide()
            self.ui.Savegamebtn.hide()
        self.style = """
                    QWidget {
                    background-color: rgb(39, 39, 39);}

                    QPushButton {
                    background-color: rgba(39, 39, 39);
                    background-color: black;
                    color: rgb(170, 170, 170);
                    border-style: outset;
                    border-width: 0.5px;
                    border-radius: 15px;
                    border-color: red;
                    font: bold 16px;
                    padding: 6px;
                    min-height: 55px;
                    min-width: 25em;}
                    
                    QPushButton:pressed {
                    background-color: rgba(39, 39, 39);
                    border-style: inset;
                    }

                    QLabel {
                    background-color: none;
                    border-radius: 7px;
                    }"""
        self.swapstyle = """
        QPushButton {min-height: 50px;
                    min-width: 50px;
                    max-width: 50px;
                    max-height: 50px;
        }"""
        self.ui.setStyleSheet(self.style)
        self.ui.Swapbtn.setStyleSheet(self.swapstyle)
        self.ui.showFullScreen()

    def checked(self):
        if self.ui.clickchbox.isChecked() and self.ui.dndchbox.isChecked() == False:
            print('1')
            self.ui.clickchbox.setDisabled(True)
            self.ui.dndchbox.setDisabled(False)
        elif self.ui.clickchbox.isChecked() == False and self.ui.dndchbox.isChecked():
            self.ui.dndchbox.setDisabled(True)
            self.ui.clickchbox.setDisabled(False)
        else:
            self.ui.dndchbox.setDisabled(False)
            self.ui.clickchbox.setDisabled(False)
    def wasclicked(self):
        print(self.sender().text(), 'clicked')
        if self.sender() == self.ui.Openmenubtn:
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.Cmpbtn.show()
            self.ui.Savegamebtn.show()
        elif self.sender() == self.ui.Cmpbtn:
            self.ui.stackedWidget.setCurrentIndex(0)
        elif self.sender() == self.ui.Exitbtn or self.sender() == self.ui.Mexitbtn:
            sys.exit(app.exec())
        elif self.sender() == self.ui.Newgamebtn:
            self.game = Game()
            self.ui.Previouscard.clear()
            self.ui.Previouscard.hide()

            self.table = self.game.gettable()
            self.ptable = []

            self.hand = self.game.getchand()
            size = QPixmap('Карты\\'+self.hand.getcurrent().getfullcard()+'.png').scaled(self.width, self.height, Qt.KeepAspectRatio)
            self.ui.Currentcard.installEventFilter(self)
            self.ui.Previouscard.installEventFilter(self)
            self.ui.Currentcard.setPixmap(size)


            self.availables = self.game.getavailables()


            self.lblname = [[self.ui.label_00],[self.ui.label_10, self.ui.label_11],[self.ui.label_20,self.ui.label_21,self.ui.label_22],
                            [self.ui.label_30,self.ui.label_31,self.ui.label_32,self.ui.label_33],[self.ui.label_40,self.ui.label_41,
                            self.ui.label_42,self.ui.label_43,self.ui.label_44],[self.ui.label_50,self.ui.label_51,self.ui.label_52,
                            self.ui.label_53,self.ui.label_54,self.ui.label_55],[self.ui.label_60,self.ui.label_61,self.ui.label_62,
                            self.ui.label_63,self.ui.label_64,self.ui.label_65,self.ui.label_66]]

            for i in range(7):
                for j in range(i+1):
                    size = QPixmap('Карты\\'+self.table[i][j].getfullcard()+'.png').scaled(self.width, self.height,
                                                                                           Qt.KeepAspectRatio)
                    self.lblname[i][j].installEventFilter(self)
                    self.lblname[i][j].setPixmap(size)
            self.ui.stackedWidget.setCurrentIndex(0)
        elif self.sender() == self.ui.Swapbtn:
            self.ui.Previouscard.show()
            self.hand.nextcurrent()
            self.ui.Currentcard.setPixmap(
                QPixmap('Карты\\'+self.hand.getcurrent().getfullcard()+'.png').scaled(self.width, self.height,
                                                                                      Qt.KeepAspectRatio))
            self.ui.Previouscard.setPixmap(
                QPixmap('Карты\\' + self.hand.getprevious().getfullcard() + '.png').scaled(self.width,self.height,
                                                                                          Qt.KeepAspectRatio))

        elif self.sender() == self.ui.Settingsbtn:
            self.ui.stackedWidget.setCurrentIndex(2)
        elif self.sender() == self.ui.Updbtn:

            self.ui.stackedWidget.setCurrentIndex(1)

    def eventFilter(self, obj, event):
        if str(type(obj)) == "<class 'PyQt5.QtWidgets.QLabel'>" and\
            event.type() == QEvent.MouseButtonPress and QMouseEvent(event).buttons() == Qt.LeftButton:
            if obj == self.ui.Currentcard or obj == self.ui.Previouscard:
                if self.selected:
                    self.selected.setStyleSheet('border: none;')
                obj.setStyleSheet('border: 4px solid rgba(170,255,0,0.6);box-sizing: border-box;')
                self.selected = obj
            else:
                for i in range(7):
                    if obj in self.lblname[i]:
                        self.chosedcard = [i,self.lblname[i].index(obj)]
                if self.table[self.chosedcard[0]][self.chosedcard[1]] in self.availables:
                    if self.selected:
                        self.selected.setStyleSheet('border: none;')
                    obj.setStyleSheet('border: 4px solid rgba(170,255,0,0.6);box-sizing: border-box;')
                    self.selected = obj

        return QWidget.eventFilter(self, obj, event)





def my_excepthook(type,value,tback):
    QtWidgets.QMessageBox.critical(
        window,"CRITICAL ERROR",str(value),
        QtWidgets.QMessageBox.Cancel)
    sys.excepthook(type,value,tback)


sys.excepthook = my_excepthook

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec())