from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from open_connection_qt import Ui_Form
import sqlite3


class OpenConnect(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(900, 200, 0, 0)
