# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enregistrer_code.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(478, 275)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 311, 41))
        self.label.setStyleSheet("font: 19pt \"Rockwell\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 121, 21))
        self.label_2.setStyleSheet("font: 11pt \"Rockwell\";")
        self.label_2.setObjectName("label_2")
        self.nom_fichier = QtWidgets.QLineEdit(self.centralwidget)
        self.nom_fichier.setGeometry(QtCore.QRect(150, 79, 231, 21))
        self.nom_fichier.setStyleSheet("font: 12pt \"Rockwell\";")
        self.nom_fichier.setClearButtonEnabled(True)
        self.nom_fichier.setObjectName("nom_fichier")
        self.destination = QtWidgets.QLineEdit(self.centralwidget)
        self.destination.setGeometry(QtCore.QRect(150, 130, 231, 21))
        self.destination.setStyleSheet("font: 12pt \"Rockwell\";")
        self.destination.setClearButtonEnabled(True)
        self.destination.setObjectName("destination")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 131, 121, 21))
        self.label_3.setStyleSheet("font: 11pt \"Rockwell\";")
        self.label_3.setObjectName("label_3")
        self.change = QtWidgets.QPushButton(self.centralwidget)
        self.change.setGeometry(QtCore.QRect(390, 130, 51, 21))
        self.change.setStyleSheet("border:solid;border-width:1;font: 9pt \"Rockwell\";")
        self.change.setObjectName("change")
        self.enregistrer = QtWidgets.QPushButton(self.centralwidget)
        self.enregistrer.setGeometry(QtCore.QRect(150, 180, 231, 21))
        self.enregistrer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enregistrer.setStyleSheet("font: 11pt \"Rockwell\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"border:solid;border-width:1;\n"
"border-color: rgb(0, 0, 255);")
        self.enregistrer.setObjectName("enregistrer")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 2, 461, 231))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setGeometry(QtCore.QRect(410, 22, 31, 21))
        self.close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close.setStyleSheet("border:solid;border-radius:20;border-width:1;\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.close.setObjectName("close")
        self.label_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.nom_fichier.raise_()
        self.destination.raise_()
        self.label_3.raise_()
        self.change.raise_()
        self.enregistrer.raise_()
        self.close.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 478, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">Enregistrer ce code</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Nom du fichier :"))
        self.nom_fichier.setText(_translate("MainWindow", "factoriel.py"))
        self.destination.setText(_translate("MainWindow", "C:\\"))
        self.label_3.setText(_translate("MainWindow", "Destination :"))
        self.change.setText(_translate("MainWindow", "changer"))
        self.enregistrer.setText(_translate("MainWindow", "Enregistrer"))
        self.close.setText(_translate("MainWindow", "X"))
