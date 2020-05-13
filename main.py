import sys
import re
from PyQt5.QtGui import QIcon

import connect
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from main_qt import Ui_MainWindow


class MainClassProject(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        path = QDir.homePath()
        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(QDir.rootPath())
        self.dirModel.setFilter(QDir.AllDirs | QDir.Files | QDir.NoDot)
        self.local_list.setModel(self.dirModel)
        self.local_list.clicked.connect(self.on_clicked)
        self.client = None
        self.connect_button.clicked.connect(self.conn_button)
        self.disconnect_but.clicked.connect(self.disconn)
        self.remote_list.itemDoubleClicked.connect(self.double_click_remotelist)

    def conn_button(self):
        ip_cheack = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", self.ip_line.text())
        print(self.username_line.text())
        print(self.password_line.text())
        print(ip_cheack)
        if self.username_line.text() and self.password_line.text() and ip_cheack:
            try:
                self.client = connect.ConnectFTP(self.username_line.text(), self.password_line.text(), self.ip_line.text())
                print(self.client)
                a = self.client.get_ls_dir()
                a.insert(0, '..')
                ftp = self.client.client.open_sftp()
                for i in a:
                    item = QListWidgetItem()
                    item.setText(i)
                    if i == '..':
                        icon = QIcon('/root/python_project/img/dir.png')
                        item.setIcon(icon)
                        self.remote_list.addItem(item)
                    elif ftp.stat(i).st_mode & 0x4000:
                        icon = QIcon('/root/python_project/img/dir.png')
                        item.setIcon(icon)
                        self.remote_list.addItem(item)
                    else:
                        icon = QIcon('/root/python_project/img/file.png')
                        item.setIcon(icon)
                        self.remote_list.addItem(item)
            except Exception as e:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(str(e))
                msg.show()

    def disconn(self):
        if self.client is not None:
            self.client.client.close()
            self.remote_list.clear()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("No active session")
            msg.show()
            print('asdasdd')

    def double_click_remotelist(self):
        pass

    def on_clicked(self, index):
        path = self.dirModel.fileInfo(index).absoluteFilePath()
        self.local_list.setRootIndex(self.dirModel.setRootPath(path))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainClassProject()
    w.show()
    sys.exit(app.exec_())


