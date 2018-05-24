import  sys
from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow


class Menu(QMainWindow):
    def __init__(self):

        super().__init__()

        menubar = self.menuBar()

        dosya = menubar.addMenu("Dosya")
        duzenle = menubar.addMenu("Düzenle")

        dosya_ac = QAction("Dosya aç",self)
        dosya_ac.setShortcut("Ctrl+o")
        dosya_kaydet = QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+s")
        cikis = QAction("Çıkış",self)
        cikis.setShortcut("ctrl+q")

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cikis)



        ara_ve_degistir = duzenle.addMenu("Ara ve değiştir")

        ara = QAction("ara",self)

        degistir = QAction("değiştir",self)

        temizle = QAction("temizle",self)

        ara_ve_degistir.addAction(ara)
        ara_ve_degistir.addAction(degistir)

        duzenle.addAction(temizle)




        cikis.triggered.connect(self.cikis_yap)

        dosya.triggered.connect(self.response)





        self.setWindowTitle("Menüler")

        self.show()

    def cikis_yap(self):
        qApp.quit()

    def response(self,action):

        if action.text() == "Dosya aç":
            print("Dosya Aç")
        elif action.text() == "Dosya Kaydet":
            print(" Dosya Kaydet")
        elif action.text() == "Çıkış":
            print("Çıkış")



app = QApplication(sys.argv)

menu = Menu()

sys.exit(app.exec())