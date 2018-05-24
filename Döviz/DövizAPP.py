
from PyQt5 import QtWidgets
import  sys
import requests
from bs4 import  BeautifulSoup

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()
    def init_ui(self):
        url = "https://www.doviz.com/"
        response = requests.get(url)

        self.html_icerigi = response.content

        self.soup = BeautifulSoup(self.html_icerigi, "html.parser")
        self.dov = self.soup.find_all("div", {"class": "column2-row2"})  # bahsedilen divler
        self.güncel = list()
        for i in self.dov:
            i = i.text
            i = i.strip()
            self.güncel.append(i)
        self.yazı_alanı = QtWidgets.QTextEdit()
        self.buton1 = QtWidgets.QPushButton("Altın Hesapla")
        self.buton2 = QtWidgets.QPushButton("Dolar Hesapla")
        self.buton3 = QtWidgets.QPushButton("Euro Hesapla")
        self.button4 = QtWidgets.QPushButton("Temizle")
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.buton2)
        vbox.addWidget(self.buton1)
        vbox.addWidget(self.buton3)
        vbox.addWidget(self.yazı_alanı)
        vbox.addStretch()
        vbox.addWidget(self.button4)
        hbox = QtWidgets.QHBoxLayout()
        hbox.addStretch()
        hbox.addLayout(vbox)
        hbox.addStretch()
        self.setLayout(hbox)
        self.buton1.clicked.connect(self.click)
        self.buton2.clicked.connect(self.click2)
        self.buton3.clicked.connect(self.click3)
        self.button4.clicked.connect(self.clear)

        self.setWindowTitle("DÖVİZ APP BY YEK")
        self.show()

    def click(self):

        self.yazı_alanı.setText("Çeyrek Altın Alış: {}\nÇeyrek Altın Satış: {}\nYarım Altın Alış: {}\nYarım Altın Satış: {}\nTam Altın Alış: {}\nTam Altın Satış: {}\n".format(self.güncel[14],self.güncel[15],self.güncel[16],self.güncel[17],self.güncel[18],self.güncel[19]))

    def click2(self):
        self.yazı_alanı.setText("Dolar Alış: {}\nDolar Satış: {}".format(self.güncel[2], self.güncel[3]))
    def click3(self):
        self.yazı_alanı.setText("Euro Alış: {}\nEuro Satış: {}".format(self.güncel[4],self.güncel[5]))
    def clear(self):
        self.yazı_alanı.clear()



app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec())