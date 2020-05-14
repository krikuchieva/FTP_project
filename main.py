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
        self.client = None
        self.connect_button.clicked.connect(self.conn_button)
        self.disconnect_but.clicked.connect(self.disconn)
        self.remote_list.itemDoubleClicked.connect(self.double_click_remotelist)
        self.local_list.doubleClicked.connect(self.double_click_locallost)
        self.local_to_remote.clicked.connect(self.local_to_remote_copy)
        self.remote_to_local.clicked.connect(self.remote_to_local_copy)

    def show_all_flies(self, path='/'):
        try:
            list_dir = self.client.get_ls_dir(path)
            list_dir.insert(0, '..')
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText(str(e))
            msg.setWindowTitle("Error")
            msg.exec_()
            self.show_all_flies(self.client.path)
        else:
            for i in list_dir:
                item = QListWidgetItem()
                item.setText(i)
                if i == '..' or self.client.ftp.stat(path+'/'+i).st_mode & 0x4000:
                    icon = QIcon('img/dir.png')
                    item.setIcon(icon)
                    self.remote_list.addItem(item)
                elif i[0] == '.' and i[1] != '.':
                    pass
                else:
                    icon = QIcon('img/file.png')
                    item.setIcon(icon)
                    self.remote_list.addItem(item)

    def conn_button(self):
        ip_cheack = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", self.ip_line.text())
        if self.username_line.text() and self.password_line.text() and ip_cheack:
            try:
                self.client = connect.ConnectFTP(self.username_line.text(), self.password_line.text(), self.ip_line.text())
                self.show_all_flies()
            except Exception as e:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setInformativeText(str(e))
                msg.setWindowTitle("Error")
                msg.exec_()

    def disconn(self):
        if self.client is not None:
            self.client.client.close()
            self.remote_list.clear()
            self.client = None
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('No active session')
            msg.setWindowTitle("Error")
            msg.exec_()

    def double_click_remotelist(self):
        text = self.remote_list.currentItem().text()
        if text == '..' and self.client.path == '/':
            return
        elif text == '..' and self.client.path != '/':
            change_path = self.client.path.split('/')
            change_path = '/'.join(change_path[:-1])
            self.remote_list.clear()
            self.show_all_flies(change_path)
            self.client.path = change_path
        elif self.client.ftp.stat(self.client.path + '/' + text).st_mode & 0x4000:
            self.remote_list.clear()
            self.show_all_flies(self.client.path + '/' + text)

    def double_click_locallost(self, index):
        path = self.dirModel.fileInfo(index).absoluteFilePath()
        self.local_list.setRootIndex(self.dirModel.setRootPath(path))

    def local_to_remote_copy(self):
        try:
            if self.dirModel.fileInfo(self.local_list.currentIndex()).isFile(): #for files
                self.client.ftp.put(self.dirModel.filePath(self.local_list.currentIndex()),
                                        self.client.path + "/" +
                                            self.dirModel.fileInfo(self.local_list.currentIndex()).fileName())
                self.remote_list.clear()
                self.show_all_flies(self.client.path)
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText(str(e))
            msg.setWindowTitle("Error")
            msg.exec_()

    def remote_to_local_copy(self):
        try:
            if not (self.client.ftp.stat(self.client.path + '/' + self.remote_list.currentItem().text()).st_mode & 0x4000): #for files
                self.client.ftp.get(self.client.path + '/' + self.remote_list.currentItem().text(),
                                    self.dirModel.filePath(self.local_list.currentIndex()) + '/'
                                    + self.remote_list.currentItem().text())
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText(str(e))
            msg.setWindowTitle("Error")
            msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainClassProject()
    w.show()
    sys.exit(app.exec_())


