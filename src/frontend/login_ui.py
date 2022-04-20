# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from register_ui import RegisterPage
from appointment_ui import AppoinmentPage
from doctorLanding_ui import DoctorLandingPage
import os,sys
sys.path.append(os.path.join(sys.path[0], "../backend"))
from login import login as lg

class LoginPage(QtWidgets.QMainWindow):
    def __init__(self, window, isDoctor, parent=None):
        super(LoginPage, self).__init__(parent)
        self.MainWindow = window
        self.isDoctor = isDoctor
        self.parent = parent
        self.register = RegisterPage(self.MainWindow, self.isDoctor, self)
        self.appointment = AppoinmentPage(self.MainWindow, self)
        self.doctorLandingPage = DoctorLandingPage(self.MainWindow, self)

    def toLandingPage(self):
        self.parent.setupUi(self.MainWindow)
        self.MainWindow.show()

    def toAppointmentPage(self):
        if self.isDoctor:
            self.doctorLandingPage.setupUi(self.MainWindow)
            self.MainWindow.show()
        else:
            self.appointment.setupUi(self.MainWindow)
            self.MainWindow.show()

    def toRegisterPage(self):
        self.register.setupUi(self.MainWindow)
        self.MainWindow.show()

    def login(self):
        username = self.textEdit.text()
        password = self.textEdit_2.text()
        self.changeState(lg([username,password], self.isDoctor))

    def changeState(self, state):
        _translate = QtCore.QCoreApplication.translate
        if not state:
            self.textEdit.setText("")
            self.textEdit_2.setText("")
            self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:13pt; color: red;\">Username or Password is invalid</span></p></body></html>"))
        else:
            self.toAppointmentPage()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        MainWindow.setMinimumSize(QtCore.QSize(960, 540))
        MainWindow.setMaximumSize(QtCore.QSize(960, 540))
        MainWindow.setStyleSheet("background-color: rgb(238, 238, 236)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 10, 351, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("text-align:center;\n"
"color: rgb(106, 110, 131);\n"
"border-radius: 40px;\n"
"font: 40px;\n"
"font-weight: bold;\n"
"margin-left: 20px;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("text-align:center;\n"
"color: #1CA8FF;\n"
"font: 40px;\n"
"font-weight: bold;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 90, 911, 421))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.frame.setMinimumSize(QtCore.QSize(400, 400))
        self.frame.setMaximumSize(QtCore.QSize(400, 400))
        self.frame.setStyleSheet("background-color: #F1F3FA;\n""")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 416, 381))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setStyleSheet("text-align:center;\n"
"color: rgb(106, 110, 131);\n"
"font: 30px;\n"
"font-weight: bold;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.textEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.textEdit.setMinimumSize(QtCore.QSize(300, 50))
        self.textEdit.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: #F8F9FD;\n"
"color: #6A6E83;\n"
"border-radius: 40px;\n"
"font-weight: 800;\n"
"font: 20px;")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setPlaceholderText("Enter Username")
        self.horizontalLayout_4.addWidget(self.textEdit)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.textEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.textEdit_2.setMinimumSize(QtCore.QSize(300, 50))
        self.textEdit_2.setMaximumSize(QtCore.QSize(300, 30))
        self.textEdit_2.setStyleSheet("background-color: #F8F9FD;\n"
"color: #6A6E83;\n"
"border-radius: 30px;\n"
"font: 20px;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setPlaceholderText("Enter Password")
        self.textEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.horizontalLayout_5.addWidget(self.textEdit_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("""
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
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login)
        self.horizontalLayout_7.addWidget(self.pushButton)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem11)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem12)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem13)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem14)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setStyleSheet("""
        QPushButton {
            color: rgb(28, 168, 255);
            border: 0px;
        }
        QPushButton:hover {
            color: #6A6E83;
        }
        """)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.toRegisterPage)
        self.horizontalLayout_11.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_3.setStyleSheet("""
        QPushButton {
            color: rgb(28, 168, 255);
            border: 0px;
        }
        QPushButton:hover {
            color: #6A6E83;
        }
        """)
        self.pushButton_3.setObjectName("pushButton_2")
        self.pushButton_3.clicked.connect(self.toLandingPage)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem15)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.verticalLayout_2.addWidget(self.pushButton_3)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem16)
        self.horizontalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Register Page"))
        self.label.setText(_translate("MainWindow", "Hospita"))
        self.label_3.setText(_translate("MainWindow", "Lite"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:23pt;\">Sign In</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Sign in"))
        self.label_4.setText(_translate("MainWindow", "Don\'t have an account?"))
        self.pushButton_2.setText(_translate("MainWindow", "Register Here!"))
        self.pushButton_3.setText(_translate("MainWindow", "Change Role!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LoginPage()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
