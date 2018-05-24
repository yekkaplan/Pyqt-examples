import  sys

from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv) # app oluşturuldu

    okay = QtWidgets.QPushButton("Tamam") # buton oluşturuldu

    cancel = QtWidgets.QPushButton("İptal") # buton oluşturuldur

    hbox = QtWidgets.QHBoxLayout()


    hbox.addWidget(okay)

    hbox.addWidget(cancel)

    hbox.addStretch()

    vbox = QtWidgets.QVBoxLayout()

    vbox.addLayout(hbox)

    vbox.addStretch()


    pencere = QtWidgets.QWidget() # pencere oluşturuldu

    pencere.setWindowTitle("Yunus Emre Kaplan") # başlık oluşturuldu

    pencere.setLayout(vbox) # vbox yerleştiriildi

    pencere.setGeometry(100,100,500,500) # pencere geometrisi

    pencere.show() # pencereyi göster

    sys.exit(app.exec()) # pencereyi çalıştır ve çıkış yap.

Pencere()
