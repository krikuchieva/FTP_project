import sys
import re
from PyQt5.QtGui import QIcon
from connect import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from main_qt import Ui_MainWindow


class MainClassProject(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(600, 150, 0, 0)
        path = QDir.homePath()
        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(QDir.rootPath())
        self.dirModel.setFilter(QDir.AllDirs | QDir.Files | QDir.NoDot)
        self.local_list.setModel(self.dirModel)
        self.client = None
        self.windows_open = None
        self.connect_button.clicked.connect(self.conn_button)
        self.disconnect_but.clicked.connect(self.disconn)
        self.remote_list.itemDoubleClicked.connect(self.double_click_remotelist)
        self.local_list.doubleClicked.connect(self.double_click_locallost)
        self.local_to_remote.clicked.connect(self.local_to_remote_copy)
        self.remote_to_local.clicked.connect(self.remote_to_local_copy)
        self.actionNew.triggered.connect(self.click_new)
        self.actionOpen.triggered.connect(self.click_open)
        self.actionAbout_Project.triggered.connect(self.about_click)
        self.actionExit.triggered.connect(sys.exit)


        self.button_action_new = QAction(QIcon("img/file.png"), "New connection", self)
        self.button_action_new.triggered.connect(self.click_new)
        self.button_action_new.setCheckable(True)
        self.toolBar.addAction(self.button_action_new)
        self.toolBar.addSeparator()

        self.button_action_open = QAction(QIcon("img/conn.png"), "Open connection", self)
        self.button_action_open.triggered.connect(self.click_open)
        self.button_action_open.setCheckable(True)
        self.toolBar.addAction(self.button_action_open)
        self.toolBar.addSeparator()

        self.button_action_discon = QAction(QIcon("img/disconn.png"), "Close connection", self)
        self.button_action_discon.triggered.connect(self.disconn)
        self.button_action_discon.setCheckable(True)
        self.toolBar.addAction(self.button_action_discon)
        self.toolBar.addSeparator()

        self.button_action_about = QAction(QIcon("img/about.png"), "About", self)
        self.button_action_about.triggered.connect(self.about_click)
        self.button_action_about.setCheckable(True)
        self.toolBar.addAction(self.button_action_about)
        self.toolBar.addSeparator()

        self.button_action_exit = QAction(QIcon("img/exit.png"), "Exit", self)
        self.button_action_exit.triggered.connect(sys.exit)
        self.button_action_exit.setCheckable(True)
        self.toolBar.addAction(self.button_action_exit)
        self.toolBar.addSeparator()

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

    def conn_button(self, username='', password='', ip='', flag=True):
        if flag:
            if self.username_line.text() and self.password_line.text() and self.ip_line.text():
                try:
                    self.client = ConnectFTP(self.username_line.text(), self.password_line.text(), self.ip_line.text())
                    self.show_all_flies()
                except Exception as e:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setInformativeText(str(e))
                    msg.setWindowTitle("Error")
                    msg.exec_()
        else:
            try:
                print(username)
                self.client = ConnectFTP(username, password, ip)
                self.show_all_flies()
                self.username_line.setText(username)
                self.ip_line.setText(ip)
                self.password_line.setText(password)
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
            self.ip_line.setText('Enter ip address')
            self.password_line.setText('Enter password')
            self.username_line.setText('Enter username')
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
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setInformativeText('Files send')
                msg.setWindowTitle("OK")
                msg.exec_()

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

    def click_new(self):
        self.windows_new_con = NewConnect()
        self.windows_new_con.show()

    def click_open(self):
        self.windows_open = ConnectOpen(self.conn_button)
        self.windows_open.show()

    def about_click(self):
        self.windows_about = About()
        self.windows_about.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainClassProject()
    w.show()
    sys.exit(app.exec_())


