import sys

from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()
    def init_ui(self):

        self.yazı_alanı = QtWidgets.QLabel("Bana Henüz tıklanmadı..")

        self.buton = QtWidgets.QPushButton("Bana tıkla")

        self.say = 0

        vbox = QtWidgets.QVBoxLayout()

        vbox.addWidget(self.buton)
        vbox.addWidget(self.yazı_alanı)
        vbox.addStretch()
        hbox = QtWidgets.QHBoxLayout()
        hbox.addStretch()
        hbox.addLayout(vbox)
        hbox.addStretch()
        self.setLayout(hbox)

        self.buton.clicked.connect(self.click)
        self.show()
    def click(self):

        self.say += 1
        self.yazı_alanı.setText("Bana " + str(self.say)  +  "defa Tıklandı.")



app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec())
