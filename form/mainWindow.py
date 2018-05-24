#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from  PyQt5 import QtCore
import sys
from gui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self,app = None):
        super(MainWindow,self).__init__()

        self.app = app

        self.setupUi(self)

        self.show()

    def push(self):
        spin = str(self.spinBox.text())

        liste = self.listWidget

        ekle = str(self.lineEdit.text())

        liste.addItem(ekle)

        liste.addItem(spin)

    def on_actionKapat_triggered(self):
        self.close()

        

if __name__=="__main__": #  Başka dosya import edip etmedıgını sorgula.  sorun yok ise main çalıştır.

    app = QtWidgets.QApplication(sys.argv) # app değişkenini çalıştırmak ıcın

    mainWin = MainWindow(app) # MainWindow değişkeninde programı  atıyoruz.

    ret = app.exec()  # app çalıştırıldı

    app.exit() # exit komutu çalıştırıldıgında

    sys.exit(ret) # sys'den exit komutu çalıştırıldıgında..