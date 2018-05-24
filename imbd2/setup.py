import sys,requests
from PyQt5 import QtWidgets
from bs4 import BeautifulSoup
from gui import Ui_Dialog

class MainWindow(QtWidgets.QDialog,Ui_Dialog):

    def __init__(self,app = None):

        super(MainWindow,self).__init__()

        self.app = app

        self.setupUi(self)

        self.veri_cek()

        self.show()

    def veri_cek(self):

        self.url = "http://www.imdb.com/chart/top"  #

        self.response = requests.get(self.url)  #

        self.html_icerigi = self.response.content  #

        self.soup = BeautifulSoup(self.html_icerigi, "html.parser")  #


        self.basliklar = self.soup.find_all("td", {"class": "titleColumn"})  #

        self.ratingler = self.soup.find_all("td", {"class", "ratingColumn imdbRating"})


    def guncelle(self):
        try:
            with open("tümsıralama.txt","w") as file:
                for baslik, rating in zip(self.basliklar, self.ratingler):
                    baslik = baslik.text  #
                    rating = rating.text  #
                    baslik = baslik.strip()  #
                    baslik = baslik.replace("\n", "")  #
                    rating = rating.strip()
                    rating = rating.replace("\n", "")
                    file.write(baslik + " " + rating + "\n")
            with open("tümsıralama.txt","r") as file2:
                yek = file2.read()
                self.textBrowser.setText(yek)
                self.label_2.setText("Güncel sıralama başarıyla gerçekleşti.")

        except:
            self.label_2.setText("Başarısız oldu.")
    def clear(self):

        self.textEdit.clear()



    def sirala(self):
        try:
            a = float(self.lineEdit.text())
            with open("puan.txt","w") as file2:
                for baslik, rating in zip(self.basliklar, self.ratingler):  # baslik ve ratingi zip ile birleştirerek arıyoruz
                    baslik = baslik.text  #
                    rating = rating.text  #
                    baslik = baslik.strip()  # parçalıyoruz
                    baslik = baslik.replace("\n", "")  # n yerine " "
                    rating = rating.strip()
                    rating = rating.replace("\n", "")
                    if(float(a) < float(rating)):
                        file2.write(baslik + " " + rating + "\n")

            with open("puan.txt","r") as file3:
                yek = file3.read()
                self.textBrowser.setText(yek)

            self.label_2.setText("Sıralama başarıyla gerçekleşti.")
        except:
            self.label_2.setText("Sıralama Başarısız.")

if __name__=="__main__": #  Başka dosya import edip etmedıgını sorgula.

    app = QtWidgets.QApplication(sys.argv) # app değişkenini çalıştırmak ıcın

    mainWin = MainWindow(app) ## main win  Ana Pencere

    ret = app.exec() #

    app.exit()

    sys.exit(ret) # dongu sonlanması ıcın



