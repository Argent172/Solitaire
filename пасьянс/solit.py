# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'solit.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1629, 985)
        Form.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.Openmenubtn = QtWidgets.QPushButton(self.page)
        self.Openmenubtn.setStyleSheet("")
        self.Openmenubtn.setObjectName("Openmenubtn")
        self.horizontalLayout_15.addWidget(self.Openmenubtn)
        self.Hintbtn = QtWidgets.QPushButton(self.page)
        self.Hintbtn.setStyleSheet("")
        self.Hintbtn.setObjectName("Hintbtn")
        self.horizontalLayout_15.addWidget(self.Hintbtn)
        self.Backbtn = QtWidgets.QPushButton(self.page)
        self.Backbtn.setStyleSheet("")
        self.Backbtn.setObjectName("Backbtn")
        self.horizontalLayout_15.addWidget(self.Backbtn)
        self.Exitbtn = QtWidgets.QPushButton(self.page)
        self.Exitbtn.setStyleSheet("")
        self.Exitbtn.setObjectName("Exitbtn")
        self.horizontalLayout_15.addWidget(self.Exitbtn)
        self.gridLayout_2.addLayout(self.horizontalLayout_15, 2, 1, 1, 1)


        self.Currentcard = QtWidgets.QLabel(self.page)
        self.Currentcard.setMinimumSize(QtCore.QSize(80, 120))
        self.Currentcard.setObjectName("Currentcard")
        self.gridLayout_2.addWidget(self.Currentcard, 1, 4, 1, 1, QtCore.Qt.AlignTop)
        self.previouscard = QtWidgets.QLabel(self.page)
        self.previouscard.setMinimumSize(QtCore.QSize(80, 120))
        self.previouscard.setObjectName("previouscard")
        self.gridLayout_2.addWidget(self.previouscard, 1, 2, 1, 1, QtCore.Qt.AlignTop)



        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 3, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_8.setSpacing(30)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.label_00 = QtWidgets.QLabel(self.page)
        self.label_00.setMinimumSize(QtCore.QSize(0, 0))
        self.label_00.setMaximumSize(QtCore.QSize(120, 180))
        self.label_00.setAlignment(QtCore.Qt.AlignCenter)
        self.label_00.setObjectName("label_00")
        self.horizontalLayout_8.addWidget(self.label_00)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_9.setSpacing(31)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.label_10 = QtWidgets.QLabel(self.page)
        self.label_10.setMinimumSize(QtCore.QSize(0, 0))
        self.label_10.setMaximumSize(QtCore.QSize(120, 180))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.page)
        self.label_11.setMinimumSize(QtCore.QSize(0, 0))
        self.label_11.setMaximumSize(QtCore.QSize(120, 180))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_10.setSpacing(32)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.label_20 = QtWidgets.QLabel(self.page)
        self.label_20.setMinimumSize(QtCore.QSize(0, 0))
        self.label_20.setMaximumSize(QtCore.QSize(120, 180))
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_10.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.page)
        self.label_21.setMinimumSize(QtCore.QSize(0, 0))
        self.label_21.setMaximumSize(QtCore.QSize(120, 180))
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_10.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.page)
        self.label_22.setMinimumSize(QtCore.QSize(0, 0))
        self.label_22.setMaximumSize(QtCore.QSize(120, 180))
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_10.addWidget(self.label_22)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_11.setSpacing(33)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem7)
        self.label_30 = QtWidgets.QLabel(self.page)
        self.label_30.setMinimumSize(QtCore.QSize(0, 0))
        self.label_30.setMaximumSize(QtCore.QSize(120, 180))
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_11.addWidget(self.label_30)
        self.label_31 = QtWidgets.QLabel(self.page)
        self.label_31.setMinimumSize(QtCore.QSize(0, 0))
        self.label_31.setMaximumSize(QtCore.QSize(120, 180))
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_11.addWidget(self.label_31)
        self.label_32 = QtWidgets.QLabel(self.page)
        self.label_32.setMinimumSize(QtCore.QSize(0, 0))
        self.label_32.setMaximumSize(QtCore.QSize(120, 180))
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_11.addWidget(self.label_32)
        self.label_33 = QtWidgets.QLabel(self.page)
        self.label_33.setMinimumSize(QtCore.QSize(0, 0))
        self.label_33.setMaximumSize(QtCore.QSize(120, 180))
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_11.addWidget(self.label_33)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_12.setSpacing(34)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem9)
        self.label_40 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy)
        self.label_40.setMinimumSize(QtCore.QSize(0, 0))
        self.label_40.setMaximumSize(QtCore.QSize(120, 180))
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_12.addWidget(self.label_40)
        self.label_41 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy)
        self.label_41.setMinimumSize(QtCore.QSize(0, 0))
        self.label_41.setMaximumSize(QtCore.QSize(120, 180))
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.horizontalLayout_12.addWidget(self.label_41)
        self.label_42 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy)
        self.label_42.setMinimumSize(QtCore.QSize(0, 0))
        self.label_42.setMaximumSize(QtCore.QSize(120, 180))
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.horizontalLayout_12.addWidget(self.label_42)
        self.label_43 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy)
        self.label_43.setMinimumSize(QtCore.QSize(0, 0))
        self.label_43.setMaximumSize(QtCore.QSize(120, 180))
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.horizontalLayout_12.addWidget(self.label_43)
        self.label_44 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy)
        self.label_44.setMinimumSize(QtCore.QSize(0, 0))
        self.label_44.setMaximumSize(QtCore.QSize(120, 180))
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.horizontalLayout_12.addWidget(self.label_44)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_13.setSpacing(35)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem11)
        self.label_50 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy)
        self.label_50.setMinimumSize(QtCore.QSize(0, 0))
        self.label_50.setMaximumSize(QtCore.QSize(120, 180))
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.horizontalLayout_13.addWidget(self.label_50)
        self.label_51 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy)
        self.label_51.setMinimumSize(QtCore.QSize(0, 0))
        self.label_51.setMaximumSize(QtCore.QSize(120, 180))
        self.label_51.setAlignment(QtCore.Qt.AlignCenter)
        self.label_51.setObjectName("label_51")
        self.horizontalLayout_13.addWidget(self.label_51)
        self.label_52 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy)
        self.label_52.setMinimumSize(QtCore.QSize(0, 0))
        self.label_52.setMaximumSize(QtCore.QSize(120, 180))
        self.label_52.setAlignment(QtCore.Qt.AlignCenter)
        self.label_52.setObjectName("label_52")
        self.horizontalLayout_13.addWidget(self.label_52)
        self.label_53 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy)
        self.label_53.setMinimumSize(QtCore.QSize(0, 0))
        self.label_53.setMaximumSize(QtCore.QSize(120, 180))
        self.label_53.setAlignment(QtCore.Qt.AlignCenter)
        self.label_53.setObjectName("label_53")
        self.horizontalLayout_13.addWidget(self.label_53)
        self.label_54 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy)
        self.label_54.setMinimumSize(QtCore.QSize(0, 0))
        self.label_54.setMaximumSize(QtCore.QSize(120, 180))
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setObjectName("label_54")
        self.horizontalLayout_13.addWidget(self.label_54)
        self.label_55 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy)
        self.label_55.setMinimumSize(QtCore.QSize(0, 0))
        self.label_55.setMaximumSize(QtCore.QSize(120, 180))
        self.label_55.setAlignment(QtCore.Qt.AlignCenter)
        self.label_55.setObjectName("label_55")
        self.horizontalLayout_13.addWidget(self.label_55)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_14.setSpacing(40)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem13)
        self.label_60 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy)
        self.label_60.setMinimumSize(QtCore.QSize(0, 0))
        self.label_60.setMaximumSize(QtCore.QSize(120, 180))
        self.label_60.setAlignment(QtCore.Qt.AlignCenter)
        self.label_60.setObjectName("label_60")
        self.horizontalLayout_14.addWidget(self.label_60)
        self.label_61 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy)
        self.label_61.setMinimumSize(QtCore.QSize(0, 0))
        self.label_61.setMaximumSize(QtCore.QSize(120, 180))
        self.label_61.setAlignment(QtCore.Qt.AlignCenter)
        self.label_61.setObjectName("label_61")
        self.horizontalLayout_14.addWidget(self.label_61)
        self.label_62 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_62.sizePolicy().hasHeightForWidth())
        self.label_62.setSizePolicy(sizePolicy)
        self.label_62.setMinimumSize(QtCore.QSize(0, 0))
        self.label_62.setMaximumSize(QtCore.QSize(120, 180))
        self.label_62.setAlignment(QtCore.Qt.AlignCenter)
        self.label_62.setObjectName("label_62")
        self.horizontalLayout_14.addWidget(self.label_62)
        self.label_63 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy)
        self.label_63.setMinimumSize(QtCore.QSize(0, 0))
        self.label_63.setMaximumSize(QtCore.QSize(120, 180))
        self.label_63.setAlignment(QtCore.Qt.AlignCenter)
        self.label_63.setObjectName("label_63")
        self.horizontalLayout_14.addWidget(self.label_63)
        self.label_64 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_64.sizePolicy().hasHeightForWidth())
        self.label_64.setSizePolicy(sizePolicy)
        self.label_64.setMinimumSize(QtCore.QSize(0, 0))
        self.label_64.setMaximumSize(QtCore.QSize(120, 180))
        self.label_64.setAlignment(QtCore.Qt.AlignCenter)
        self.label_64.setObjectName("label_64")
        self.horizontalLayout_14.addWidget(self.label_64)
        self.label_65 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_65.sizePolicy().hasHeightForWidth())
        self.label_65.setSizePolicy(sizePolicy)
        self.label_65.setMinimumSize(QtCore.QSize(0, 0))
        self.label_65.setMaximumSize(QtCore.QSize(120, 180))
        self.label_65.setAlignment(QtCore.Qt.AlignCenter)
        self.label_65.setObjectName("label_65")
        self.horizontalLayout_14.addWidget(self.label_65)
        self.label_66 = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_66.sizePolicy().hasHeightForWidth())
        self.label_66.setSizePolicy(sizePolicy)
        self.label_66.setMinimumSize(QtCore.QSize(0, 0))
        self.label_66.setMaximumSize(QtCore.QSize(120, 180))
        self.label_66.setAlignment(QtCore.Qt.AlignCenter)
        self.label_66.setObjectName("label_66")
        self.horizontalLayout_14.addWidget(self.label_66)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem14)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Newgamebtn = QtWidgets.QPushButton(self.page_2)
        self.Newgamebtn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Newgamebtn.sizePolicy().hasHeightForWidth())
        self.Newgamebtn.setSizePolicy(sizePolicy)
        self.Newgamebtn.setMinimumSize(QtCore.QSize(0, 0))
        self.Newgamebtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Newgamebtn.setStyleSheet("")
        self.Newgamebtn.setObjectName("Newgamebtn")
        self.verticalLayout_3.addWidget(self.Newgamebtn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.Savegamebtn = QtWidgets.QPushButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Savegamebtn.sizePolicy().hasHeightForWidth())
        self.Savegamebtn.setSizePolicy(sizePolicy)
        self.Savegamebtn.setMinimumSize(QtCore.QSize(0, 0))
        self.Savegamebtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Savegamebtn.setObjectName("Savegamebtn")
        self.verticalLayout_3.addWidget(self.Savegamebtn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.Loadbtn = QtWidgets.QPushButton(self.page_2)
        self.Loadbtn.setObjectName("Loadbtn")
        self.verticalLayout_3.addWidget(self.Loadbtn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.Settingsbtn = QtWidgets.QPushButton(self.page_2)
        self.Settingsbtn.setMinimumSize(QtCore.QSize(0, 0))
        self.Settingsbtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Settingsbtn.setObjectName("Settingsbtn")
        self.verticalLayout_3.addWidget(self.Settingsbtn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.Cmpbtn = QtWidgets.QPushButton(self.page_2)
        self.Cmpbtn.setMinimumSize(QtCore.QSize(0, 0))
        self.Cmpbtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Cmpbtn.setStyleSheet("")
        self.Cmpbtn.setObjectName("Cmpbtn")
        self.verticalLayout_3.addWidget(self.Cmpbtn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.Mexitbtn = QtWidgets.QPushButton(self.page_2)
        self.Mexitbtn.setObjectName("Mexitbtn")
        self.verticalLayout_3.addWidget(self.Mexitbtn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Openmenubtn.setText(_translate("Form", "Меню"))
        self.Hintbtn.setText(_translate("Form", "Подсказка"))
        self.Backbtn.setText(_translate("Form", "Отмена"))
        self.Exitbtn.setText(_translate("Form", "Выход"))
        self.Currentcard.setText(_translate("Form", "Текущая"))
        self.previouscard.setText(_translate("Form", "Предыдущая карта"))
        self.label_00.setText(_translate("Form", "00"))
        self.label_10.setText(_translate("Form", "10"))
        self.label_11.setText(_translate("Form", "11"))
        self.label_20.setText(_translate("Form", "20"))
        self.label_21.setText(_translate("Form", "21"))
        self.label_22.setText(_translate("Form", "22"))
        self.label_30.setText(_translate("Form", "30"))
        self.label_31.setText(_translate("Form", "31"))
        self.label_32.setText(_translate("Form", "32"))
        self.label_33.setText(_translate("Form", "33"))
        self.label_40.setText(_translate("Form", "40"))
        self.label_41.setText(_translate("Form", "41"))
        self.label_42.setText(_translate("Form", "42"))
        self.label_43.setText(_translate("Form", "43"))
        self.label_44.setText(_translate("Form", "44"))
        self.label_50.setText(_translate("Form", "50"))
        self.label_51.setText(_translate("Form", "51"))
        self.label_52.setText(_translate("Form", "52"))
        self.label_53.setText(_translate("Form", "53"))
        self.label_54.setText(_translate("Form", "54"))
        self.label_55.setText(_translate("Form", "55"))
        self.label_60.setText(_translate("Form", "60"))
        self.label_61.setText(_translate("Form", "61"))
        self.label_62.setText(_translate("Form", "62"))
        self.label_63.setText(_translate("Form", "63"))
        self.label_64.setText(_translate("Form", "64"))
        self.label_65.setText(_translate("Form", "65"))
        self.label_66.setText(_translate("Form", "66"))
        self.Newgamebtn.setText(_translate("Form", "Новая игра"))
        self.Savegamebtn.setText(_translate("Form", "Сохранить"))
        self.Loadbtn.setText(_translate("Form", "Загрузить"))
        self.Settingsbtn.setText(_translate("Form", "Настройки"))
        self.Cmpbtn.setText(_translate("Form", "Вернуться к игре"))
        self.Mexitbtn.setText(_translate("Form", "Выход"))

