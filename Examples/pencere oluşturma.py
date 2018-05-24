import sys
from PyQt5 import QtWidgets,QtGui

def pencere ():


    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("PYQT DERSLERİ")

    etiket1 = QtWidgets.QLabel(pencere)
    etiket2 = QtWidgets.QLabel(pencere)
    etiket1.setText("Burası bir yazıdır..")
    etiket1.move(200,30)
    etiket2.setPixmap(QtGui.QPixmap("python.png"))
    etiket2.move(70,70)



pencere()