# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(993, 634)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(22, 90, 440, 481))
        self.groupBox.setObjectName("groupBox")
        self.local_list = QtWidgets.QListView(self.groupBox)
        self.local_list.setGeometry(QtCore.QRect(0, 20, 440, 461))
        self.local_list.setIconSize(QtCore.QSize(25, 25))
        self.local_list.setObjectName("local_list")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(530, 90, 440, 481))
        self.groupBox_2.setObjectName("groupBox_2")
        self.remote_list = QtWidgets.QListWidget(self.groupBox_2)
        self.remote_list.setGeometry(QtCore.QRect(0, 20, 440, 461))
        self.remote_list.setIconSize(QtCore.QSize(25, 25))
        self.remote_list.setObjectName("remote_list")
        self.ip_line = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_line.setGeometry(QtCore.QRect(10, 30, 241, 31))
        self.ip_line.setClearButtonEnabled(True)
        self.ip_line.setObjectName("ip_line")
        self.username_line = QtWidgets.QLineEdit(self.centralwidget)
        self.username_line.setGeometry(QtCore.QRect(256, 30, 240, 30))
        self.username_line.setClearButtonEnabled(True)
        self.username_line.setObjectName("username_line")
        self.password_line = QtWidgets.QLineEdit(self.centralwidget)
        self.password_line.setGeometry(QtCore.QRect(499, 30, 240, 31))
        self.password_line.setInputMask("")
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line.setClearButtonEnabled(True)
        self.password_line.setObjectName("password_line")
        self.connect_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_button.setGeometry(QtCore.QRect(741, 30, 120, 30))
        self.connect_button.setObjectName("connect_button")
        self.disconnect_but = QtWidgets.QPushButton(self.centralwidget)
        self.disconnect_but.setGeometry(QtCore.QRect(860, 30, 120, 30))
        self.disconnect_but.setObjectName("disconnect_but")
        self.local_to_remote = QtWidgets.QPushButton(self.centralwidget)
        self.local_to_remote.setGeometry(QtCore.QRect(465, 260, 60, 50))
        self.local_to_remote.setObjectName("local_to_remote")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(465, 320, 60, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 993, 25))
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
        self.groupBox.setTitle(_translate("MainWindow", "Local site"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Remote site"))
        self.ip_line.setText(_translate("MainWindow", "Введити адрес"))
        self.username_line.setText(_translate("MainWindow", "Введите логин"))
        self.password_line.setText(_translate("MainWindow", "Введите пароль"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
        self.disconnect_but.setText(_translate("MainWindow", "Disconnect"))
        self.local_to_remote.setText(_translate("MainWindow", ">>>"))
        self.pushButton_2.setText(_translate("MainWindow", "<<<"))
