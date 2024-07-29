from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon


# QApllication -> ilovani shaklantrish uchun
# QWidget  -> oynani shakllantrish uchun


app = QApplication([])
win = QWidget()


# win.move(50,100)   # oynani x va y oqida belgilab beradi
# win.setFixedSize(300,500)  # oynani boyi va enini olchamini belgilab beradi
win.setGeometry(200, 300, 500, 400)   # 2ta metodni ozida jamlaydi

win.setWindowTitle("Foundation65")  # titleni ozgartish
win.setWindowIcon(QIcon("C:\\Users\\User\\Desktop\\s.jpg"))   # iconni ozgartirsa ham boladi


lbl = QLabel("Negadur Chunmayapsizmi, Bilmadim?", win)
lbl.move(0, 100)   # x va y oqlarini razmeri berilgan
# lbl2 = QLabel("Malina", win)
lbl.setStyleSheet("font-size: 20px; background-color: lightgreen; color:red") # yozuvni razmeeri ozgaradi va orqa foni bilan birga
lbl.setText("ANA ENDI CHUNMAYAPSIZLAR, YANAYAM BILMADIM")


# lbl = QLabel("Palakt", win)
# lbl.setText("HAZILLASHUDIMDE")


edit = QLineEdit(win)
edit.setGeometry(10, 10, 200, 50)   # table ozgartb beradi
edit.setStyleSheet("font-size:25px';  background-color:lightblue")
# edit.setPlaceholderText("TEST REJIMI")


def TEST():
    natija = edit.text()
    # print(natija)   # consolega chiqarb beradi
    edit.clear()
    lbl.setText(natija)
    lbl.adjustSize()   # satr ozgarishini amalga oshrb beradi


btn = QPushButton("OK", win)
btn.setStyleSheet("font-size:15px; background-color: lightyellow")
btn.move(50, 250)
btn.clicked.connect(TEST)


win.show()   # oynani korsatb beradi
app.exec_()   # oynani x ni bosib turmaguncha korsatib berib turadi, tsikl vazifasini bajarib beradi