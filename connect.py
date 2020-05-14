import paramiko
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


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
