# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(686, 376)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 431, 28))
        self.lineEdit.setObjectName("lineEdit")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(10, 10, 431, 28))
        self.spinBox.setObjectName("spinBox")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 100, 431, 192))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 90, 221, 201))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setPixmap(QtGui.QPixmap("../../asd.jpeg"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 10, 88, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 686, 22))
        self.menubar.setObjectName("menubar")
        self.menuDosya = QtWidgets.QMenu(self.menubar)
        self.menuDosya.setObjectName("menuDosya")
        self.menuAyarlar = QtWidgets.QMenu(self.menubar)
        self.menuAyarlar.setObjectName("menuAyarlar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionKapat = QtWidgets.QAction(MainWindow)
        self.actionKapat.setObjectName("actionKapat")
        self.actionBuraya_Yaz = QtWidgets.QAction(MainWindow)
        self.actionBuraya_Yaz.setObjectName("actionBuraya_Yaz")
        self.menuDosya.addAction(self.actionKapat)
        self.menuAyarlar.addAction(self.actionBuraya_Yaz)
        self.menubar.addAction(self.menuDosya.menuAction())
        self.menubar.addAction(self.menuAyarlar.menuAction())

        self.retranslateUi(MainWindow)


        self.pushButton.clicked.connect(self.push)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Yazdır"))
        self.menuDosya.setTitle(_translate("MainWindow", "Dosya"))
        self.menuAyarlar.setTitle(_translate("MainWindow", "Ayarlar"))
        self.actionKapat.setText(_translate("MainWindow", "Kapat"))
        self.actionBuraya_Yaz.setText(_translate("MainWindow", "Yapılandır"))

