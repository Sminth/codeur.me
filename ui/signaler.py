# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signaler.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(464, 392)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 78, 121, 21))
        self.label_2.setStyleSheet("font: 11pt \"Rockwell\";")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 461, 351))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.nom = QtWidgets.QLineEdit(self.centralwidget)
        self.nom.setGeometry(QtCore.QRect(170, 77, 261, 31))
        self.nom.setStyleSheet("font: 12pt \"Rockwell\";")
        self.nom.setText("")
        self.nom.setClearButtonEnabled(True)
        self.nom.setObjectName("nom")
        self.envoyer = QtWidgets.QPushButton(self.centralwidget)
        self.envoyer.setGeometry(QtCore.QRect(170, 310, 261, 21))
        self.envoyer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.envoyer.setStyleSheet("font: 11pt \"Rockwell\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"border:solid;border-width:1;\n"
"border-color: rgb(0, 0, 255);")
        self.envoyer.setObjectName("envoyer")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 8, 311, 41))
        self.label.setStyleSheet("font: 19pt \"Rockwell\";")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 129, 121, 21))
        self.label_3.setStyleSheet("font: 11pt \"Rockwell\";")
        self.label_3.setObjectName("label_3")
        self.contact = QtWidgets.QLineEdit(self.centralwidget)
        self.contact.setGeometry(QtCore.QRect(170, 130, 261, 31))
        self.contact.setStyleSheet("font: 12pt \"Rockwell\";")
        self.contact.setText("")
        self.contact.setClearButtonEnabled(True)
        self.contact.setObjectName("contact")
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setGeometry(QtCore.QRect(400, 20, 31, 21))
        self.close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close.setStyleSheet("border:solid;border-radius:20;border-width:1;\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.close.setObjectName("close")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 121, 21))
        self.label_5.setStyleSheet("font: 11pt \"Rockwell\";")
        self.label_5.setObjectName("label_5")
        self.message = QtWidgets.QTextEdit(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(170, 180, 261, 111))
        self.message.setStyleSheet("font: 13pt \"Rockwell\";")
        self.message.setObjectName("message")
        self.label_4.raise_()
        self.label_2.raise_()
        self.nom.raise_()
        self.envoyer.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.contact.raise_()
        self.close.raise_()
        self.label_5.raise_()
        self.message.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 464, 21))
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
        self.label_2.setText(_translate("MainWindow", "Votre nom"))
        self.nom.setPlaceholderText(_translate("MainWindow", "lambda"))
        self.envoyer.setText(_translate("MainWindow", "Envoyer"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">Signaler une erreur !</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Votre contact"))
        self.contact.setPlaceholderText(_translate("MainWindow", "xx xx xx xx"))
        self.close.setText(_translate("MainWindow", "X"))
        self.label_5.setText(_translate("MainWindow", "Votre message"))
        self.message.setPlaceholderText(_translate("MainWindow", "Entrez votre message ici !"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

