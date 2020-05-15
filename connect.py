import paramiko
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from new_con import Ui_Form
import sqlite3

class ConnectFTP:
    def __init__(self, username, passwd, ip):
        self.user = username
        self.password = passwd
        self.ip_address = ip
        self.client = self.conn(self.user, self.password,  self.ip_address)
        self.ftp = self.client.open_sftp()
        self.path = None
        print(type(self.ftp))

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



class NewConnect(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(900, 200,0, 0)
        self.ok_button.clicked.connect(self.ok_button_click)
        self.conn_sql = None
        self.cursor = None

    def ok_button_click(self):
        try:
            if self.host_addr_line.text() and self.user_name_line.text() and self.name_line.text() and self.password_line.text():
                self.conn_sql = sqlite3.connect("connection_list.db")
                self.cursor = self.conn_sql.cursor()
                self.cursor.execute("""INSERT INTO  main_table VALUES('%s', '%s', '%s', '%s')"""
                                    % (self.name_line.text(), self.host_addr_line.text(), self.user_name_line.text(),
                                        self.password_line.text()))
                self.cursor.close()
                self.conn_sql.commit()
                self.cursor = None
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText(str(e))
            msg.setWindowTitle("Error")
            msg.exec_()
        finally:
            self.conn_sql.close()
            self.conn_sql = None

