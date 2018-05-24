# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(639, 526)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 6, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 2, 2, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 2, 2, 1)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 2, 1, 1)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.guncelle)
        self.pushButton_2.clicked.connect(Dialog.clear)
        self.pushButton_3.clicked.connect(Dialog.close)
        self.pushButton_4.clicked.connect(Dialog.sirala)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "İmbd Top250"))
        self.pushButton.setText(_translate("Dialog", "Güncelle"))
        self.pushButton_3.setText(_translate("Dialog", "Çıkış"))
        self.pushButton_2.setText(_translate("Dialog", "Temizle"))
        self.pushButton_4.setText(_translate("Dialog", "Sıralama"))
        self.label.setText(_translate("Dialog", "İmbb Puanı:"))
        self.label_2.setText(_translate("Dialog", ""))

