# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/showDoctor.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from appointment import viewDokter as vd
from PyQt5 import QtCore, QtGui, QtWidgets
from room_ui import RoomPage

class AppoinmentPage(QtWidgets.QMainWindow):
    def __init__(self, window=None, parent=None):
        super(AppoinmentPage, self).__init__(parent)
        self.MainWindow = window
        self.data = vd(["","","",""])
        remains = 9 - len(self.data) % 9
        for i in range(remains):
            self.data.append("")
        self.Page = 0
        self.MaxPage = len(self.data)
        self.Parent = parent
        self.RoomPage = RoomPage(self.MainWindow, self.Parent, self)

    def toLoginPage(self):
        self.Parent.setupUi(self.MainWindow)
        self.MainWindow.show()

    def toRoomPage(self):
        self.RoomPage.setupUi(self.MainWindow)
        self.MainWindow.show()

    def nextPageFunction(self):
        if self.Page + 9 < self.MaxPage:
            self.Page += 9
        self.findDoctor()

    def prevPageFunction(self):
        if self.Page - 9 >= 0:
            self.Page -= 9
        self.findDoctor()
        
    def updateDoctor(self):
        query = self.searchQuery.toPlainText()
        query = query.split(";")
        # Search By Name;Date;Time
        self.data = vd([query[0], "", query[1], query[2]])
        remains = 9 - len(self.data) % 9
        for _ in range(remains):
            self.data.append('')
        self.findDoctor()

    def checkString(self, string):
        if string != '':
            return True
        else:
            return False

    def findDoctor(self):
        _translate = QtCore.QCoreApplication.translate
        data = self.data

        if (self.checkString(data[self.Page])):
            self.doctorName1.setText("Dr. " + data[self.Page])
            self.card1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Make An Appointment</span></p></body></html>"))
        else:
            self.doctorName1.setText("")
            self.card1.setText("")
        
        if (self.checkString(data[self.Page + 1])):
            self.doctorName2.setText("Dr. " + data[self.Page + 1])
            self.card2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Make An Appointment</span></p></body></html>"))
        else:
            self.doctorName2.setText("")
            self.card2.setText("")

        if (self.checkString(data[self.Page + 2])):
            self.doctorName3.setText("Dr. " + data[self.Page + 2])
            self.card3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Make An Appointment</span></p></body></html>"))
        else:
            self.doctorName3.setText("")
            self.card3.setText("")

        if (self.checkString(data[self.Page + 3])):
            self.doctorName4.setText("Dr. " + data[self.Page + 3])
            self.card4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Make An Appointment</span></p></body></html>"))
        else:
            self.doctorName4.setText("")
            self.card4.setText("")

        if (self.checkString(data[self.Page + 4])):
            self.doctorName5.setText("Dr. " + data[self.Page + 4])
            self.card5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Make An Appointment</span></p></body></html>"))
        else:
            self.doctorName5.setText("")
            self.card5.setText("")

        if (self.checkString(data[self.Page + 5])):
            self.doctorName6.setText("Dr. " + data[self.Page + 5])
            self.card6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Make An Appointment</span></p></body></html>"))
        else:
            self.doctorName6.setText("")
            self.card6.setText("")

        if (self.checkString(data[self.Page + 6])):
            self.doctorName7.setText("Dr. " + data[self.Page + 6])
            self.card7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Make An Appointment</span></p></body></html>"))
        else:
            self.doctorName7.setText("")
            self.card7.setText("")

        if (self.checkString(data[self.Page + 7])):
            self.doctorName8.setText("Dr. " + data[self.Page + 7])
            self.card8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Make An Appointment</span></p></body></html>"))
        else:
            self.doctorName8.setText("")
            self.card8.setText("")

        if (self.checkString(data[self.Page + 8])):
            self.doctorName9.setText("Dr. " + data[self.Page + 8])
            self.card9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Make An Appointment</span></p></body></html>"))
        else:
            self.doctorName9.setText("")
            self.card9.setText("")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 630)
        MainWindow.setMinimumSize(QtCore.QSize(1120, 630))
        MainWindow.setMaximumSize(QtCore.QSize(1120, 630))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(-10, -10, 211, 671))
        self.frame_2.setStyleSheet("background-color: white;\n"
"border: 0px;\n"
"color: #6A6E83;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 161, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setStyleSheet("text-align:center;\n"
"color: rgb(106, 110, 131);\n"
"font: 25px;\n"
"font-weight: bold;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setStyleSheet("text-align:center;\n"
"color: #1CA8FF;\n"
"font: 25px;\n"
"font-weight: bold;")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 100, 131, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_8.setStyleSheet("text-align:center;\n"
"color: #1CA8FF;\n"
"font: 15px;\n"
"font-weight: bold;")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 180, 131, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.label_9.setStyleSheet("text-align:left;\n"
"color: rgb(106, 110, 131);\n"
"font: 15px;\n"
"font-weight: bold;")
        self.label_9.setObjectName("label_9")
        self.label_9.clicked.connect(self.toRoomPage)
        self.horizontalLayout_4.addWidget(self.label_9)
        self.signOutButton = QtWidgets.QPushButton(self.frame_2)
        self.signOutButton.setGeometry(QtCore.QRect(50, 570, 100, 40))
        self.signOutButton.setMinimumSize(QtCore.QSize(100, 40))
        self.signOutButton.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(True)
        font.setWeight(75)
        self.signOutButton.setFont(font)
        self.signOutButton.setStyleSheet("""
        QPushButton {
            background-color: rgb(28, 168, 255);\n
            color: white;
            border: 0px;
            border-radius: 10px;
            padding: 10px;
        }
        QPushButton:hover {
            color: rgb(28, 168, 255);
            background-color: white;
        }
        """)
        self.signOutButton.setObjectName("signOutButton")
        self.signOutButton.clicked.connect(self.toLoginPage)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(230, 90, 861, 511))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_8 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame_8.setMinimumSize(QtCore.QSize(269, 161))
        self.frame_8.setMaximumSize(QtCore.QSize(269, 161))
        self.frame_8.setStyleSheet("background-color: #FFFFFF;\n"
"border-radius: 20px;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(self.frame_8)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(0, 20, 271, 141))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        spacerItem1 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem1)
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.doctorName6 = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.doctorName6.setFont(font)
        self.doctorName6.setStyleSheet("color : black;\n"
"font-size: 20px;\n"
"")
        self.doctorName6.setObjectName("doctorName6")
        self.verticalLayout_30.addWidget(self.doctorName6)
        self.horizontalLayout_21.addLayout(self.verticalLayout_30)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem2)
        self.verticalLayout_28.addLayout(self.horizontalLayout_21)
        self.label_53 = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        self.label_53.setMinimumSize(QtCore.QSize(0, 2))
        self.label_53.setMaximumSize(QtCore.QSize(16777215, 2))
        self.label_53.setStyleSheet("background-color: #D1D1D1;")
        self.label_53.setText("")
        self.label_53.setObjectName("label_53")
        self.verticalLayout_28.addWidget(self.label_53)
        self.card6 = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.card6.setFont(font)
        self.card6.setStyleSheet("color : #1CA8FF;\n"
"font-size: 15px;")
        self.card6.setObjectName("card6")
        self.verticalLayout_28.addWidget(self.card6)
        self.gridLayout.addWidget(self.frame_8, 2, 4, 1, 1)
        self.frame_11 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame_11.setMinimumSize(QtCore.QSize(269, 161))
        self.frame_11.setMaximumSize(QtCore.QSize(269, 161))
        self.frame_11.setStyleSheet("background-color: #FFFFFF;\n"
"border-radius: 20px;")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayoutWidget_15 = QtWidgets.QWidget(self.frame_11)
        self.verticalLayoutWidget_15.setGeometry(QtCore.QRect(0, 20, 271, 141))
        self.verticalLayoutWidget_15.setObjectName("verticalLayoutWidget_15")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_15)
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        spacerItem3 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem3)
        self.verticalLayout_39 = QtWidgets.QVBoxLayout()
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.doctorName9 = QtWidgets.QLabel(self.verticalLayoutWidget_15)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.doctorName9.setFont(font)
        self.doctorName9.setStyleSheet("color : black;\n"
"font-size: 20px;\n"
"")
        self.doctorName9.setObjectName("doctorName9")
        self.verticalLayout_39.addWidget(self.doctorName9)
        self.horizontalLayout_24.addLayout(self.verticalLayout_39)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem4)
        self.verticalLayout_37.addLayout(self.horizontalLayout_24)
        self.label_69 = QtWidgets.QLabel(self.verticalLayoutWidget_15)
        self.label_69.setMinimumSize(QtCore.QSize(0, 2))
        self.label_69.setMaximumSize(QtCore.QSize(16777215, 2))
        self.label_69.setStyleSheet("background-color: #D1D1D1;")
        self.label_69.setText("")
        self.label_69.setObjectName("label_69")
        self.verticalLayout_37.addWidget(self.label_69)
        self.card9 = QtWidgets.QLabel(self.verticalLayoutWidget_15)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.card9.setFont(font)
        self.card9.setStyleSheet("color : #1CA8FF;\n"
"font-size: 15px;")
        self.card9.setObjectName("card9")
        self.verticalLayout_37.addWidget(self.card9)
        self.gridLayout.addWidget(self.frame_11, 4, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 1, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 1, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame_5.setMinimumSize(QtCore.QSize(269, 161))
        self.frame_5.setMaximumSize(QtCore.QSize(269, 161))
        self.frame_5.setStyleSheet("background-color: #FFFFFF;\n"
"border-radius: 20px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.frame_5)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(0, 20, 271, 141))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem8 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem8)
        self.doctorName3 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.doctorName3.setFont(font)
        self.doctorName3.setStyleSheet("color : black;\n"
"font-size: 20px;\n"
"")
        self.doctorName3.setObjectName("doctorName3")
        self.horizontalLayout_18.addWidget(self.doctorName3)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem9)
        self.verticalLayout_19.addLayout(self.horizontalLayout_18)
        self.label_27 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_27.setMinimumSize(QtCore.QSize(0, 2))
        self.label_27.setMaximumSize(QtCore.QSize(16777215, 2))
        self.label_27.setStyleSheet("background-color: #D1D1D1;")
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.verticalLayout_19.addWidget(self.label_27)
        self.card3 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.card3.setFont(font)
        self.card3.setStyleSheet("color : #1CA8FF;\n"
"font-size: 15px;")
        self.card3.setObjectName("card3")
        self.verticalLayout_19.addWidget(self.card3)
        self.gridLayout.addWidget(self.frame_5, 0, 4, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame_6.setMinimumSize(QtCore.QSize(269, 161))
        self.frame_6.setMaximumSize(QtCore.QSize(269, 161))
        self.frame_6.setStyleSheet("background-color: #FFFFFF;\n"
"border-radius: 20px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.frame_6)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(0, 20, 271, 141))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem10 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem10)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.doctorName4 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.doctorName4.setFont(font)
        self.doctorName4.setStyleSheet("color : black;\n"
"font-size: 20px;\n"
"")
        self.doctorName4.setObjectName("doctorName4")
        self.verticalLayout_24.addWidget(self.doctorName4)
        self.horizontalLayout_19.addLayout(self.verticalLayout_24)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem11)
        self.verticalLayout_22.addLayout(self.horizontalLayout_19)
        self.label_43 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.label_43.setMinimumSize(QtCore.QSize(0, 2))
        self.label_43.setMaximumSize(QtCore.QSize(16777215, 2))
        self.label_43.setStyleSheet("background-color: #D1D1D1;")
        self.label_43.setText("")
        self.label_43.setObjectName("label_43")
        self.verticalLayout_22.addWidget(self.label_43)
        self.card4 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.card4.setFont(font)
        self.card4.setStyleSheet("color : #1CA8FF;\n"
"font-size: 15px;")
        self.card4.setObjectName("card4")
        self.verticalLayout_22.addWidget(self.card4)
        self.gridLayout.addWidget(self.frame_6, 2, 0, 1, 1)
        self.frame_10 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame_10.setMinimumSize(QtCore.QSize(269, 161))
        self.frame_10.setMaximumSize(QtCore.QSize(269, 161))
        self.frame_10.setStyleSheet("background-color: #FFFFFF;\n"
"border-radius: 20px;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayoutWidget_14 = QtWidgets.QWidget(self.frame_10)
        self.verticalLayoutWidget_14.setGeometry(QtCore.QRect(0, 20, 271, 141))
        self.verticalLayoutWidget_14.setObjectName("verticalLayoutWidget_14")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_14)
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        spacerItem12 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem12)
        self.verticalLayout_36 = QtWidgets.QVBoxLayout()
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.doctorName8 = QtWidgets.QLabel(self.verticalLayoutWidget_14)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.doctorName8.setFont(font)
        self.doctorName8.setStyleSheet("color : black;\n"
"font-size: 20px;\n"
"")
        self.doctorName8.setObjectName("doctorName8")
        self.verticalLayout_36.addWidget(self.doctorName8)
        self.horizontalLayout_23.addLayout(self.verticalLayout_36)
        spacerItem13 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem13)
        self.verticalLayout_34.addLayout(self.horizontalLayout_23)
        self.label_63 = QtWidgets.QLabel(self.verticalLayoutWidget_14)
        self.label_63.setMinimumSize(QtCore.QSize(0, 2))
        self.label_63.setMaximumSize(QtCore.QSize(16777215, 2))
        self.label_63.setStyleSheet("background-color: #D1D1D1;")
        self.label_63.setText("")
        self.label_63.setObjectName("label_63")
        self.verticalLayout_34.addWidget(self.label_63)
        self.card8 = QtWidgets.QLabel(self.verticalLayoutWidget_14)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.card8.setFont(font)
        self.card8.setStyleSheet("color : #1CA8FF;\n"
"font-size: 15px;")
        self.card8.setObjectName("card8")
        self.verticalLayout_34.addWidget(self.card8)
        self.gridLayout.addWidget(self.frame_10, 4, 2, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame_7.setMinimumSize(QtCore.QSize(269, 161))
        self.frame_7.setMaximumSize(QtCore.QSize(269, 161))
        self.frame_7.setStyleSheet("background-color: #FFFFFF;\n"
"border-radius: 20px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.frame_7)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(0, 20, 271, 141))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem14 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem14)
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.doctorName5 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.doctorName5.setFont(font)
        self.doctorName5.setStyleSheet("color : black;\n"
"font-size: 20px;\n"
"")
        self.doctorName5.setObjectName("doctorName5")
        self.verticalLayout_27.addWidget(self.doctorName5)
        self.horizontalLayout_20.addLayout(self.verticalLayout_27)
        spacerItem15 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem15)
        self.verticalLayout_25.addLayout(self.horizontalLayout_20)
        self.label_48 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.label_48.setMinimumSize(QtCore.QSize(0, 2))
        self.label_48.setMaximumSize(QtCore.QSize(16777215, 2))
        self.label_48.setStyleSheet("background-color: #D1D1D1;")
        self.label_48.setText("")
        self.label_48.setObjectName("label_48")
        self.verticalLayout_25.addWidget(self.label_48)
        self.card5 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.card5.setFont(font)
        self.card5.setStyleSheet("color : #1CA8FF;\n"
"font-size: 15px;")
        self.card5.setObjectName("card5")
        self.verticalLayout_25.addWidget(self.card5)
        self.gridLayout.addWidget(self.frame_7, 2, 2, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame_4.setMinimumSize(QtCore.QSize(269, 161))
        self.frame_4.setMaximumSize(QtCore.QSize(269, 161))
        self.frame_4.setStyleSheet("background-color: #FFFFFF;\n"
"border-radius: 20px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.frame_4)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(0, 20, 271, 141))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem16 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem16)
        self.doctorName2 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.doctorName2.setFont(font)
        self.doctorName2.setStyleSheet("color : black;\n"
"font-size: 20px;\n"
"")
        self.doctorName2.setObjectName("doctorName2")
        self.horizontalLayout_17.addWidget(self.doctorName2)
        spacerItem17 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem17)
        self.verticalLayout_16.addLayout(self.horizontalLayout_17)
        self.label_26 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.label_26.setMinimumSize(QtCore.QSize(0, 2))
        self.label_26.setMaximumSize(QtCore.QSize(16777215, 2))
        self.label_26.setStyleSheet("background-color: #D1D1D1;")
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.verticalLayout_16.addWidget(self.label_26)
        self.card2 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.card2.setFont(font)
        self.card2.setStyleSheet("color : #1CA8FF;\n"
"font-size: 15px;")
        self.card2.setObjectName("card2")
        self.verticalLayout_16.addWidget(self.card2)
        self.gridLayout.addWidget(self.frame_4, 0, 2, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame_3.setMinimumSize(QtCore.QSize(269, 161))
        self.frame_3.setMaximumSize(QtCore.QSize(269, 161))
        self.frame_3.setStyleSheet("background-color: #FFFFFF;\n"
"border-radius: 20px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.frame_3)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(0, 20, 271, 141))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem18 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem18)
        self.doctorName1 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.doctorName1.setFont(font)
        self.doctorName1.setStyleSheet("color : black;\n"
"font-size: 20px;\n"
"")
        self.doctorName1.setObjectName("doctorName1")
        self.horizontalLayout_16.addWidget(self.doctorName1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem19)
        self.verticalLayout_13.addLayout(self.horizontalLayout_16)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label_15.setMinimumSize(QtCore.QSize(0, 2))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 2))
        self.label_15.setStyleSheet("background-color: #D1D1D1;")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_13.addWidget(self.label_15)
        self.card1 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.card1.setFont(font)
        self.card1.setStyleSheet("color : #1CA8FF;\n"
"font-size: 15px;")
        self.card1.setObjectName("card1")
        self.verticalLayout_13.addWidget(self.card1)
        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)
        self.frame_9 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame_9.setMinimumSize(QtCore.QSize(269, 161))
        self.frame_9.setMaximumSize(QtCore.QSize(269, 161))
        self.frame_9.setStyleSheet("background-color: #FFFFFF;\n"
"border-radius: 20px;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayoutWidget_13 = QtWidgets.QWidget(self.frame_9)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(0, 20, 271, 141))
        self.verticalLayoutWidget_13.setObjectName("verticalLayoutWidget_13")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        spacerItem20 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem20)
        self.verticalLayout_33 = QtWidgets.QVBoxLayout()
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.doctorName7 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.doctorName7.setFont(font)
        self.doctorName7.setStyleSheet("color : black;\n"
"font-size: 20px;\n"
"")
        self.doctorName7.setObjectName("doctorName7")
        self.verticalLayout_33.addWidget(self.doctorName7)
        self.horizontalLayout_22.addLayout(self.verticalLayout_33)
        spacerItem21 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem21)
        self.verticalLayout_31.addLayout(self.horizontalLayout_22)
        self.label_58 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_58.setMinimumSize(QtCore.QSize(0, 2))
        self.label_58.setMaximumSize(QtCore.QSize(16777215, 2))
        self.label_58.setStyleSheet("background-color: #D1D1D1;")
        self.label_58.setText("")
        self.label_58.setObjectName("label_58")
        self.verticalLayout_31.addWidget(self.label_58)
        self.card7 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.card7.setFont(font)
        self.card7.setStyleSheet("color : #1CA8FF;\n"
"font-size: 15px;")
        self.card7.setObjectName("card7")
        self.verticalLayout_31.addWidget(self.card7)
        self.gridLayout.addWidget(self.frame_9, 4, 0, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem22, 3, 2, 1, 1)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(230, 10, 641, 81))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.searchQuery = QtWidgets.QTextEdit(self.horizontalLayoutWidget_10)
        self.searchQuery.setMinimumSize(QtCore.QSize(400, 41))
        self.searchQuery.setMaximumSize(QtCore.QSize(400, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(True)
        font.setWeight(75)
        self.searchQuery.setFont(font)
        self.searchQuery.setStyleSheet("background-color: #FFFFFF;\n"
"border-radius: 20px;\n"
"border: 0px;\n"
"color: #c4c4c4;\n"
"text-align: center;\n"
"padding-top: 8px;")
        self.searchQuery.setObjectName("searchQuery")
        self.searchQuery.setPlaceholderText("Search By Name;Date;Time")
        self.horizontalLayout_15.addWidget(self.searchQuery)
        self.findDoctorButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_10)
        self.findDoctorButton.setMinimumSize(QtCore.QSize(100, 40))
        self.findDoctorButton.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(True)
        font.setWeight(75)
        self.findDoctorButton.setFont(font)
        self.findDoctorButton.setStyleSheet("""
        QPushButton {
            background-color: rgb(28, 168, 255);\n
            color: white;
            border: 0px;
            border-radius: 10px;
        }
        QPushButton:hover {
            color: rgb(28, 168, 255);
            background-color: white;
        }
        """)
        self.findDoctorButton.setObjectName("findDoctorButton")
        self.horizontalLayout_15.addWidget(self.findDoctorButton)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem23)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.label_16.setMinimumSize(QtCore.QSize(600, 0))
        self.label_16.setMaximumSize(QtCore.QSize(600, 16777215))
        self.label_16.setStyleSheet("color : #6A6E83;")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(920, 20, 168, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.prevPage = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.prevPage.setMinimumSize(QtCore.QSize(0, 30))
        self.prevPage.setStyleSheet("""
        QPushButton {
            background-color: rgb(28, 168, 255);\n
            color: white;
            border: 0px;
            border-radius: 10px;
            padding: 10px;
        }
        QPushButton:hover {
            color: rgb(28, 168, 255);
            background-color: white;
        }
        """)
        self.prevPage.setObjectName("prevPage")
        self.horizontalLayout_5.addWidget(self.prevPage)
        self.nextPage = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.nextPage.setMinimumSize(QtCore.QSize(0, 30))
        self.nextPage.setStyleSheet("""
        QPushButton {
            background-color: rgb(28, 168, 255);\n
            color: white;
            border: 0px;
            border-radius: 10px;
            padding: 10px;
        }
        QPushButton:hover {
            color: rgb(28, 168, 255);
            background-color: white;
        }
        """)
        self.nextPage.setObjectName("nextPage")
        self.horizontalLayout_5.addWidget(self.nextPage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.nextPage.clicked.connect(self.nextPageFunction)
        self.prevPage.clicked.connect(self.prevPageFunction)
        self.findDoctorButton.clicked.connect(self.updateDoctor)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Hospita"))
        self.label_5.setText(_translate("MainWindow", "Lite"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Appointment</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Room"))
        self.signOutButton.setText(_translate("MainWindow", "Sign Out"))
        self.doctorName6.setText(_translate("MainWindow", "Dr. " + self.data[self.Page + 5]))
        self.card6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Make An Appointment</span></p></body></html>"))
        self.doctorName9.setText(_translate("MainWindow", "Dr. " + self.data[self.Page + 8]))
        self.card9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Make An Appointment</span></p></body></html>"))
        self.doctorName3.setText(_translate("MainWindow", "Dr. " + self.data[self.Page + 2]))
        self.card3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Make An Appointment</span></p></body></html>"))
        self.doctorName4.setText(_translate("MainWindow", "Dr. " + self.data[self.Page + 3]))
        self.card4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Make An Appointment</span></p></body></html>"))
        self.doctorName8.setText(_translate("MainWindow", "Dr. " + self.data[self.Page + 7]))
        self.card8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Make An Appointment</span></p></body></html>"))
        self.doctorName5.setText(_translate("MainWindow", "Dr. " + self.data[self.Page + 4]))
        self.card5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Make An Appointment</span></p></body></html>"))
        self.doctorName2.setText(_translate("MainWindow", "Dr. " + self.data[self.Page + 1]))
        self.card2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Make An Appointment</span></p></body></html>"))
        self.doctorName1.setText(_translate("MainWindow", "Dr. " + self.data[self.Page]))
        self.card1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Make An Appointment</span></p></body></html>"))
        self.doctorName7.setText(_translate("MainWindow", "Dr. " + self.data[self.Page + 6]))
        self.card7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Make An Appointment</span></p></body></html>"))
        self.searchQuery.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:10px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.findDoctorButton.setText(_translate("MainWindow", "Find Doctor"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Query Example: &quot;Patrick;;&quot;, or &quot;Patrick;2022-01-01;10&quot;</span></p></body></html>"))
        self.prevPage.setText(_translate("MainWindow", "<"))
        self.nextPage.setText(_translate("MainWindow", ">"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AppoinmentPage()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
