import  sys
from PyQt5 import  QtWidgets

def pencere():
    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PYQT5 3.")

    buton = QtWidgets.QPushButton(pencere)

    buton.setText("Burası Bir Butondur.")

    etiket = QtWidgets.QLabel(pencere)

    etiket.setText("Merhaba Dünya")

    etiket.move(200,30)

    buton.move(190,80)

    pencere.setGeometry(100,100,500,500)

    pencere.show()

    sys.exit(app.exec())

pencere()

h_box = QtWidgets.QHBoxLayout()  # horizontalbox oluşturuldu dikey

h_box.addStretch()  # boşluk bırakıldı

h_box.addWidget(okay)  # h box a butonlar atıldı

h_box.addWidget(cancel)

v_box = QtWidgets.QVBoxLayout()  # Vertical box oluşturuldu..

v_box.addStretch()  # boşluk bırakıldı en köşeye inmesi icin

v_box.addLayout(h_box)  # verticale horizontal atıldı..
