from PyQt5 import QtWidgets
import smtplib
from email.mime.multipart import MIMEMultipart
from  email.mime.text import MIMEText
import  sys

class pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()
    def init_ui(self):


        self.to   = QtWidgets.QLineEdit()

        self.login = QtWidgets.QPushButton("Login")

        self.send =  QtWidgets.QPushButton("Send")

        self.clear = QtWidgets.QPushButton("Clear")

        self.textarea = QtWidgets.QTextEdit()

        self.konu = QtWidgets.QLineEdit()

        self.email = QtWidgets.QLineEdit()

        self.passw = QtWidgets.QLineEdit()

        self.passw.setEchoMode(QtWidgets.QLineEdit.Password)

        self.label1 = QtWidgets.QLabel("Email:")

        self.label2 = QtWidgets.QLabel("Password:")

        self.label3 = QtWidgets.QLabel("Subject:")

        self.label4 = QtWidgets.QLabel("To:")


        vbox  = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.email)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.passw)
        vbox.addStretch()
        vbox.addWidget(self.label3)
        vbox.addWidget(self.konu)
        vbox.addWidget(self.textarea)
        vbox.addWidget(self.label4)
        vbox.addWidget(self.to)
        vbox.addWidget(self.send)
        vbox.addWidget(self.clear)
        hbox = QtWidgets.QHBoxLayout()
        hbox.addLayout(vbox)
        hbox.addStretch()
        self.setLayout(hbox)
        self.send.clicked.connect(self.defsend)
        self.clear.clicked.connect(self.defclear)
        self.setWindowTitle("EMAİL")
        self.setGeometry(100,100,250,250)

        self.show()


    def defsend(self):

        mail = self.email.text()
        sifre = self.passw.text()
        yazi = self.textarea.toPlainText()
        konu = self.konu.text()
        kime = self.to.text()

        mesaj = MIMEMultipart()  # multıpart sınıfından obje oluşturuldu

        mesaj["From"] =  mail

        mesaj["To"] = kime

        mesaj["subject"] = konu

        mesaj_gövdesi = MIMEText(yazi, "plain")  # mesaj gövdesi mimetext sınıfından plain ile oluşturuldu

        mesaj.attach(mesaj_gövdesi)  # mesaj gövdesi eklendi

        try:
            mail = smtplib.SMTP("smtp.gmail.com", 587)  # port bağlantısı

            mail.ehlo()  # bağlantı isteği

            mail.starttls()  # ttls isteği

            mail.login(self.email.text(),self.passw.text())  # login bilgileri

            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())  # mail gönderim işlemi

            print("Mail Başarıyla Gönderildi..")

            mail.close()  # close işlemi

        except:
            sys.stderr.write("Bir sorun oluştu...")  # sys hata fırlatma
            sys.stderr.flush()  # buffer flush



    def defclear(self):

        self.email.clear()

        self.textarea.clear()

        self.passw.clear()

        self.konu.clear()

        self.to.clear()

app = QtWidgets.QApplication(sys.argv)

x = pencere()

sys.exit(app.exec())