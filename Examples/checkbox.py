import sys

from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout


class Pencere(QWidget): # pencere sınıfımızı oluşturduk..
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self): # init ui kısmına özellıklerımızı ekledik..

        self.checkbox = QCheckBox("Python'ı seviyor musunuz ?") # checkboxu ekledık
        self.yazi_alani = QLabel("") # az sonra yazı gelicekburaya
        self.buton = QPushButton("Bana Tıkla") # butonu oluşturduk

        v_box = QVBoxLayout() # vertical ekledık

        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)

        self.setWindowTitle("Check Box")

        self.buton.clicked.connect(lambda : self.click(self.checkbox.isChecked(),self.yazi_alani))
        # fonksiyon olarak çalışması ıcın lambda kullandık
        self.show()

    def click(self,checkbox,yazi_alani):

        if checkbox:
            yazi_alani.setText("Python'u Seviyosun çok güzel..")
        else:
            yazi_alani.setText("Neden Sevmiyosun ?")

app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())