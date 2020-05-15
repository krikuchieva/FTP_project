# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_con.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(394, 408)
        Form.setMinimumSize(QtCore.QSize(394, 408))
        Form.setMaximumSize(QtCore.QSize(394, 408))
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 28, 351, 141))
        self.groupBox.setObjectName("groupBox")
        self.name_line = QtWidgets.QLineEdit(self.groupBox)
        self.name_line.setGeometry(QtCore.QRect(150, 48, 190, 27))
        self.name_line.setObjectName("name_line")
        self.host_addr_line = QtWidgets.QLineEdit(self.groupBox)
        self.host_addr_line.setGeometry(QtCore.QRect(150, 78, 190, 27))
        self.host_addr_line.setObjectName("host_addr_line")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 55, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 84, 111, 17))
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 188, 351, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.user_name_line = QtWidgets.QLineEdit(self.groupBox_2)
        self.user_name_line.setGeometry(QtCore.QRect(150, 58, 190, 27))
        self.user_name_line.setObjectName("user_name_line")
        self.password_line = QtWidgets.QLineEdit(self.groupBox_2)
        self.password_line.setGeometry(QtCore.QRect(150, 88, 190, 27))
        self.password_line.setObjectName("password_line")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 63, 101, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 93, 91, 17))
        self.label_4.setObjectName("label_4")
        self.ok_button = QtWidgets.QPushButton(Form)
        self.ok_button.setGeometry(QtCore.QRect(110, 368, 99, 27))
        self.ok_button.setObjectName("ok_button")
        self.cancel_button = QtWidgets.QPushButton(Form)
        self.cancel_button.setGeometry(QtCore.QRect(210, 368, 99, 27))
        self.cancel_button.setObjectName("cancel_button")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 18, 20, 341))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(10, 350, 370, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(10, 10, 370, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(370, 18, 20, 340))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "New"))
        self.groupBox.setTitle(_translate("Form", "FTP Site"))
        self.label.setText(_translate("Form", "Name:"))
        self.label_2.setText(_translate("Form", "Host address:"))
        self.groupBox_2.setTitle(_translate("Form", "Login"))
        self.label_3.setText(_translate("Form", "User name:"))
        self.label_4.setText(_translate("Form", "Password:"))
        self.ok_button.setText(_translate("Form", "OK"))
        self.cancel_button.setText(_translate("Form", "Cancel"))
