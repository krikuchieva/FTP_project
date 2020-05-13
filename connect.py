import paramiko
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ConnectFTP:
    def __init__(self, username, passwd, ip):
        self.user = username
        self.password = passwd
        self.ip_address = ip
        self.client = self.conn(self.user, self.password,  self.ip_address)
        self.path= self.pwd_def()

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

    def get_ls_dir(self, path='.'):
        with self.client.invoke_shell() as ssh:
            ftp = self.client.open_sftp()
            files = ftp.listdir(path)
        return files, path

    def pwd_def(self, path):
        stdin, stdout, stderr = self.client.exec_command("pwd")
        print(stdin, stdout, stderr)
        return stdout