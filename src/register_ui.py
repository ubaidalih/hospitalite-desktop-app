# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/register.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import re
from register import register as reg
from PyQt5 import QtCore, QtGui, QtWidgets

class RegisterPage(QtWidgets.QMainWindow):
    def __init__(self, window, isDoctor, parent=None):
        super(RegisterPage, self).__init__(parent)
        self.MainWindow = window
        self.Parent = parent
        self.isDoctor = isDoctor

    def toLoginPage(self):
        self.Parent.setupUi(self.MainWindow)
        self.MainWindow.show()

    def register(self):
        registerInfo = [self.textEdit_13.toPlainText(), self.textEdit_16.toPlainText(), self.textEdit_18.toPlainText(), self.textEdit_15.toPlainText()]
        if not re.match("""/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/""", self.textEdit_16.toPlainText()):
            self.changeState(False)
        else:
            self.changeState(reg(registerInfo, self.isDoctor))

    def changeState(self, state):
        _translate = QtCore.QCoreApplication.translate
        if state:
            self.label_1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Register Successful</span></p></body></html>"))
        else:
            if not re.match("""/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/""", self.textEdit_16.toPlainText()):
                self.label_1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;color:red;\">Email Invalid</span></p></body></html>"))
            else:
                self.label_1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;color:red;\">Username or Password already exist</span></p></body></html>"))


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        MainWindow.setMinimumSize(QtCore.QSize(960, 540))
        MainWindow.setMaximumSize(QtCore.QSize(960, 540))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(30, 30, 404, 486))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_25.addItem(spacerItem)
        self.label_15 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_15.setStyleSheet("text-align:center;\n"
"color: rgb(106, 110, 131);\n"
"font: 20px;\n"
"font-weight: bold;")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_25.addWidget(self.label_15)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_13.setStyleSheet("text-align:center;\n"
"color: rgb(106, 110, 131);\n"
"font: 40px;\n"
"font-weight: bold;")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_10.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_14.setStyleSheet("text-align:center;\n"
"color: #1CA8FF;\n"
"font: 40px;\n"
"font-weight: bold;")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_10.addWidget(self.label_14)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.verticalLayout_25.addLayout(self.horizontalLayout_10)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_25.addItem(spacerItem7)
        self.horizontalLayout_13.addLayout(self.verticalLayout_25)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(500, 10, 431, 501))
        self.frame_2.setMinimumSize(QtCore.QSize(400, 400))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setStyleSheet("background-color: #F1F3FA;\n"
"border-radius: 40px;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 20, 389, 484))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_27.addLayout(self.horizontalLayout_11)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_19.setStyleSheet("text-align:center;\n"
"color: rgb(106, 110, 131);\n"
"font: 30px;\n"
"font-weight: bold;")
        self.label_19.setObjectName("label_19")
        self.verticalLayout_27.addWidget(self.label_19)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_27.addLayout(self.verticalLayout_12)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_27.addItem(spacerItem8)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(106, 110, 131);")
        self.label_20.setObjectName("label_20")
        self.verticalLayout_27.addWidget(self.label_20)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.textEdit_13 = QtWidgets.QTextEdit(self.verticalLayoutWidget_4)
        self.textEdit_13.setMinimumSize(QtCore.QSize(300, 40))
        self.textEdit_13.setMaximumSize(QtCore.QSize(300, 30))
        self.textEdit_13.setStyleSheet("background-color: #F8F9FD;\n"
"color: #6A6E83;\n"
"border-radius: 30px;\n"
"font: 20px;")
        self.textEdit_13.setObjectName("textEdit_13")
        self.horizontalLayout_5.addWidget(self.textEdit_13)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.verticalLayout_27.addLayout(self.horizontalLayout_5)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_27.addItem(spacerItem11)
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(106, 110, 131);")
        self.label_21.setObjectName("label_21")
        self.verticalLayout_27.addWidget(self.label_21)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.textEdit_16 = QtWidgets.QTextEdit(self.verticalLayoutWidget_4)
        self.textEdit_16.setMinimumSize(QtCore.QSize(300, 40))
        self.textEdit_16.setMaximumSize(QtCore.QSize(300, 30))
        self.textEdit_16.setStyleSheet("background-color: #F8F9FD;\n"
"color: #6A6E83;\n"
"border-radius: 30px;\n"
"font: 20px;")
        self.textEdit_16.setObjectName("textEdit_16")
        self.horizontalLayout_7.addWidget(self.textEdit_16)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem13)
        self.verticalLayout_27.addLayout(self.horizontalLayout_7)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_27.addItem(spacerItem14)
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(106, 110, 131);")
        self.label_22.setObjectName("label_22")
        self.verticalLayout_27.addWidget(self.label_22)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem15)
        self.textEdit_18 = QtWidgets.QTextEdit(self.verticalLayoutWidget_4)
        self.textEdit_18.setMinimumSize(QtCore.QSize(300, 40))
        self.textEdit_18.setMaximumSize(QtCore.QSize(300, 30))
        self.textEdit_18.setStyleSheet("background-color: #F8F9FD;\n"
"color: #6A6E83;\n"
"border-radius: 30px;\n"
"font: 20px;")
        self.textEdit_18.setObjectName("textEdit_18")
        self.horizontalLayout_15.addWidget(self.textEdit_18)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem16)
        self.verticalLayout_27.addLayout(self.horizontalLayout_15)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_27.addItem(spacerItem17)
        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(106, 110, 131);")
        self.label_23.setObjectName("label_23")
        self.verticalLayout_27.addWidget(self.label_23)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem18)
        self.textEdit_15 = QtWidgets.QTextEdit(self.verticalLayoutWidget_4)
        self.textEdit_15.setMinimumSize(QtCore.QSize(300, 40))
        self.textEdit_15.setMaximumSize(QtCore.QSize(300, 30))
        self.textEdit_15.setStyleSheet("background-color: #F8F9FD;\n"
"color: #6A6E83;\n"
"border-radius: 30px;\n"
"font: 20px;")
        self.textEdit_15.setObjectName("textEdit_15")
        self.horizontalLayout_16.addWidget(self.textEdit_15)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem19)
        self.verticalLayout_27.addLayout(self.horizontalLayout_16)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_27.addItem(spacerItem20)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem21)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_4.setMinimumSize(QtCore.QSize(200, 40))
        self.pushButton_4.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("""
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
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.register)
        self.horizontalLayout_29.addWidget(self.pushButton_4)
        self.label_1 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_1.setObjectName("label_1")
        self.verticalLayout_27.addWidget(self.label_1)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem22)
        self.verticalLayout_27.addLayout(self.horizontalLayout_29)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_27.addItem(spacerItem23)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label.setObjectName("label")
        self.verticalLayout_27.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton.setStyleSheet("""
        QPushButton {
            color: rgb(28, 168, 255);
            border: 0px;
        }
        QPushButton:hover {
            color: #6A6E83;
        } """)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.toLoginPage)
        self.verticalLayout_27.addWidget(self.pushButton)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_27.addItem(spacerItem24)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_27.addItem(spacerItem25)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">Welcome To</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "Hospita"))
        self.label_14.setText(_translate("MainWindow", "Lite"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Create Account</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Nama Lengkap</p></body></html>"))
        self.textEdit_13.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:20px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Email</p></body></html>"))
        self.textEdit_16.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:20px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Username</p></body></html>"))
        self.textEdit_18.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:20px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Password</p></body></html>"))
        self.textEdit_15.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:20px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "Sign in"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Already have an account?</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Login Here!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = RegisterPage()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
