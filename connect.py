import paramiko
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from new_con import Ui_Form as Ui_Form_new_con
from about_qt import Ui_Form as Ui_Form_about
from open_connection import Ui_Form as Ui_Form_open_con
import sqlite3


class ConnectFTP:
    def __init__(self, username, passwd, ip):
        self.user = username
        self.password = passwd
        self.ip_address = ip
        self.client = self.conn(self.user, self.password,  self.ip_address)
        self.ftp = self.client.open_sftp()
        self.path = None

    def conn(self, user, password, ip):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(
            hostname=ip,
            username=user,
            password=password,
            look_for_keys=False,
            allow_agent=False)
        if client is None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Authentication failed")
        return client

    def get_ls_dir(self, path='/'):
        files = self.ftp.listdir(path)
        self.path = path
        return files


class NewConnect(QtWidgets.QWidget, Ui_Form_new_con):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(900, 200, 0, 0)
        self.ok_button.clicked.connect(self.ok_button_click)
        self.cancel_button.clicked.connect(self.close)

    def ok_button_click(self):
        try:
            if self.host_addr_line.text() and self.user_name_line.text() and self.name_line.text() and self.password_line.text():
                conn_sql = sqlite3.connect("connection_list.db")
                cursor = conn_sql.cursor()
                cursor.execute("INSERT INTO  main_table VALUES('%s', '%s', '%s', '%s')"
                                    % (self.name_line.text(), self.host_addr_line.text(), self.user_name_line.text(),
                                        self.password_line.text()))
                cursor.close()
                conn_sql.commit()

                conn_sql.close()

                self.host_addr_line.clear()
                self.user_name_line.clear()
                self.name_line.clear()
                self.password_line.clear()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setInformativeText('Record created')
                msg.setWindowTitle("OK")
                msg.exec_()
                self.close()
            else:
                raise Exception("Enter all lines")
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText(str(e))
            msg.setWindowTitle("Error")
            msg.exec_()


class ConnectOpen(QtWidgets.QWidget, Ui_Form_open_con ):
    def __init__(self, main_obj: classmethod):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(900, 200, 0, 0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Name", "Host address", "User name"])
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.doubleClicked.connect(self.double_click_table)
        self.init_self()
        self.client = main_obj

    def init_self(self):
        conn_sql = sqlite3.connect("connection_list.db")
        cursor = conn_sql.cursor()
        cursor.execute("SELECT * FROM main_table")
        record = cursor.fetchall()
        self.tableWidget.setRowCount(len(record))
        for i in range(len(record)):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(record[i][0]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(record[i][1]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(record[i][2]))
        cursor.close()
        conn_sql.close()

    def connect(self, ip, username, password):
        try:
            client = ConnectFTP(username, password, ip)
            self.show_all_flies()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText(str(e))
            msg.setWindowTitle("Error")
            msg.exec_()

    def double_click_table(self):
        conn_sql = sqlite3.connect("connection_list.db")
        cursor = conn_sql.cursor()
        host_name = self.tableWidget.item(self.tableWidget.currentRow(), 1).text()
        user_name = self.tableWidget.item(self.tableWidget.currentRow(), 2).text()
        name = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
        cursor.execute("SELECT password FROM main_table where name='%s' and host_name='%s' and user_name='%s'"
                     %(name, host_name, user_name))
        password = cursor.fetchall()[0][0]
        self.client(user_name, password, host_name, False)
        self.close()




class About(QtWidgets.QWidget, Ui_Form_about):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(900, 200, 0, 0)


