from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()


        self.setFixedSize(300, 250)

        self.lampochka = False

        self.lbl = QLabel(self)
        self.lbl.move(10, 100)

        self.reset_btn = QPushButton("R", self)
        self.reset_btn.move(10, 200)
        self.reset_btn.clicked.connect(self.RESET)

        self.add_btn = QPushButton("+", self)
        self.add_btn.move(105, 200)
        self.add_btn.clicked.connect(self.ADD)

        self.on_off_btn = QPushButton("ON|OFF", self)
        self.on_off_btn.move(205, 200)
        self.on_off_btn.clicked.connect(self.ONOFF)   # funksiya nomi


    def ONOFF(self):
        if self.lampochka:
            self.lbl.clear()
            self.lampochka = False
        else:
            self.lbl.setText("0")
            self.lampochka = True

    def RESET(self):
        if self.lampochka:
            self.lbl.setText("0")


    def ADD(self):
        if self.lampochka:
            self.lbl.setText(str(int(self.lbl.text())+1))
            self.lbl.adjustSize()



app = QApplication([])
win = MyWindow()
win.show()
app.exec_()