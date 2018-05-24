import sys,requests
from PyQt5 import QtWidgets
from bs4 import BeautifulSoup

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()


        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("İMBD")

        self.button1 = QtWidgets.QPushButton("Update")

        self.button2 = QtWidgets.QPushButton("Clean")

        self.button3 = QtWidgets.QListWidget()
        hbox = QtWidgets.QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        self.setLayout(hbox)

        self.button1.clicked.connect(self.defupdate)
        self.show()

    def defupdate(self):

        url = "http://www.imdb.com/chart/top"  # url girdik

        response = requests.get(url)  # url'i çekmek ıcın response değişkenine atıyoruz

        html_icerigi = response.content  # içerigi content fonksıyonuyla alıyoruz

        soup = BeautifulSoup(html_icerigi, "html.parser")  # soup değişkenine parseleyerek atıyoruz


        basliklar = soup.find_all("td", {"class": "titleColumn"})  # bahsedilen divler
        ratingler = soup.find_all("td", {"class", "ratingColumn imdbRating"})
        liste = list()
        for baslik, rating in zip(basliklar, ratingler):  # baslik ve ratingi zip ile birleştirerek arıyoruz
            baslik = baslik.text  #
            rating = rating.text  #
            baslik = baslik.strip()  # parçalıyoruz
            baslik = baslik.replace("\n", "")  # n yerine " "
            rating = rating.strip()
            rating = rating.replace("\n", "")


app = QtWidgets.QApplication(sys.argv)

a = Pencere()

sys.exit(app.exec())