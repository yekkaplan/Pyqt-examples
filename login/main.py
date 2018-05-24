import sys
import sqlite3
from PyQt5 import QtWidgets
from gui import Ui_Dialog

class MainWindow(QtWidgets.QDialog,Ui_Dialog):

    def __init__(self,app = None):

        super(MainWindow,self).__init__()

        self.app = app

        self.setupUi(self)

        self.baglanti_olustur()



        self.show()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("Database.db")

        self.cursor = self.baglanti.cursor()

        self.cursor.execute("Create Table If not exists üyeler (kullanıcı_adı TEXT,parola TEXT)")

        self.baglanti.commit()

    def girisyap(self):
        adi = self.lineEdit.text()
        par = self.lineEdit_2.text()

        self.cursor.execute("Select * From üyeler where kullanıcı_adı = ? and parola = ?",(adi,par))

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.label_4.setText("Böyle bir kullanıcı yok.")



        else:

            self.label_4.setText("Başarıyla giriş yaptınız..")


if __name__=="__main__":

    app = QtWidgets.QApplication(sys.argv)

    mainWin = MainWindow(app)

    ret = app.exec()

    app.exit()

    sys.exit(ret)



