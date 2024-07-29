from random import choice

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 200, 300, 250)

        self.edit = QLineEdit(self)

        self.lbl = QLabel("ISM", self)
        self.lbl.move(200,0)

        self.btn = QPushButton("OK", self)
        self.btn.move(0, 100)
        self.btn.clicked.connect(self.RANG)

    def RANG(self):
        lst = ['lightgreen', 'lightblue', 'lightyellow', 'purple']
        natija = choice(lst)
        self.setStyleSheet(f"background-color: {natija}")
        ']]]]'



app = QApplication([])
win = MyWindow()
win.show()
app.exec_()