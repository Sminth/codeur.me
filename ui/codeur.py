# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'codeur.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(857, 611)
        MainWindow.setMaximumSize(QtCore.QSize(857, 618))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/prefix1/lc.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(9, 0, 837, 601))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(-4, -8, 841, 601))
        self.label.setStyleSheet("border-image: url(:/newPrefix/modern-laptop.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.titre = QtWidgets.QLabel(self.page)
        self.titre.setGeometry(QtCore.QRect(170, 170, 521, 111))
        self.titre.setStyleSheet("border:solid;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"background-color: rgb(0, 0, 0,96);")
        self.titre.setObjectName("titre")
        self.texte = QtWidgets.QLabel(self.page)
        self.texte.setGeometry(QtCore.QRect(270, 340, 341, 121))
        self.texte.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.texte.setStyleSheet("font: 27pt \"Poor Richard\";\n"
"color: rgb(255, 255, 255)")
        self.texte.setObjectName("texte")
        self.btn_cle = QtWidgets.QPushButton(self.page)
        self.btn_cle.setGeometry(QtCore.QRect(260, 385, 331, 41))
        self.btn_cle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cle.setStyleSheet("background:transparent;\n"
"border:solid;\n"
"border-width:2px;\n"
"border-color: rgb(255, 255, 255);")
        self.btn_cle.setText("")
        self.btn_cle.setObjectName("btn_cle")
        self.bg = QtWidgets.QLabel(self.page)
        self.bg.setGeometry(QtCore.QRect(10, 50, 831, 301))
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.line = QtWidgets.QFrame(self.page)
        self.line.setGeometry(QtCore.QRect(270, 415, 311, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label.raise_()
        self.titre.raise_()
        self.texte.raise_()
        self.bg.raise_()
        self.line.raise_()
        self.btn_cle.raise_()
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.fond1 = QtWidgets.QLabel(self.page_2)
        self.fond1.setGeometry(QtCore.QRect(140, 20, 641, 381))
        self.fond1.setStyleSheet("border:solid;\n"
"\n"
"background-color: rgb(0, 0, 0,123);\n"
"border-image: url(:/prefix1/h.jpg);")
        self.fond1.setText("")
        self.fond1.setObjectName("fond1")
        self.groupBox = QtWidgets.QGroupBox(self.page_2)
        self.groupBox.setGeometry(QtCore.QRect(180, 430, 561, 121))
        self.groupBox.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.groupBox.setTitle("")
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.para = QtWidgets.QPushButton(self.groupBox)
        self.para.setGeometry(QtCore.QRect(410, 40, 71, 51))
        self.para.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.para.setStyleSheet("border-image: url(:/prefix1/settings.png);\n"
"border:solid;\n"
"\n"
"color: rgb(255, 255, 255);")
        self.para.setText("")
        self.para.setObjectName("para")
        self.astuce = QtWidgets.QPushButton(self.groupBox)
        self.astuce.setGeometry(QtCore.QRect(255, 40, 51, 41))
        self.astuce.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.astuce.setStyleSheet("border:solid;\n"
"border-radius:20;\n"
"background-color: rgb(1, 116, 211);\n"
"font: 75 15pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Matura MT Script Capitals\";\n"
"\n"
"")
        self.astuce.setObjectName("astuce")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(420, 50, 51, 31))
        self.label_12.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.tech = QtWidgets.QPushButton(self.groupBox)
        self.tech.setGeometry(QtCore.QRect(80, 40, 71, 51))
        self.tech.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tech.setStyleSheet("border-image: url(:/prefix1/download.png);\n"
"border:solid;\n"
"\n"
"color: rgb(255, 255, 255);")
        self.tech.setText("")
        self.tech.setObjectName("tech")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(90, 50, 51, 31))
        self.label_13.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.astuce.raise_()
        self.label_12.raise_()
        self.para.raise_()
        self.label_13.raise_()
        self.tech.raise_()
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(226, 362, 611, 171))
        self.label_7.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(240, 410, 611, 181))
        self.label_8.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 791, 591))
        self.label_9.setStyleSheet("background-color: rgb(29, 29, 29);\n"
"")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.page_2)
        self.label_11.setGeometry(QtCore.QRect(190, 440, 71, 71))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_22 = QtWidgets.QLabel(self.page_2)
        self.label_22.setGeometry(QtCore.QRect(620, 0, 241, 561))
        self.label_22.setStyleSheet("background-color: rgb(29, 29, 29);\n"
"")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.doc1 = QtWidgets.QScrollArea(self.page_2)
        self.doc1.setGeometry(QtCore.QRect(0, 0, 71, 591))
        self.doc1.setStyleSheet("background:transparent;\n"
"background-color: rgb(29, 29, 29);")
        self.doc1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.doc1.setWidgetResizable(True)
        self.doc1.setObjectName("doc1")
        self.scrollAreaWidgetContents_10 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_10.setGeometry(QtCore.QRect(0, 0, 69, 589))
        self.scrollAreaWidgetContents_10.setObjectName("scrollAreaWidgetContents_10")
        self.Java = QtWidgets.QPushButton(self.scrollAreaWidgetContents_10)
        self.Java.setGeometry(QtCore.QRect(80, 320, 151, 41))
        self.Java.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Java.setStyleSheet("\n"
"\n"
"background-color: rgb(0, 0, 0,116);\n"
"font: 75 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border:solid;\n"
"border-width:1;\n"
"border-color: rgb(0, 0, 0);")
        self.Java.setObjectName("Java")
        self.Python = QtWidgets.QPushButton(self.scrollAreaWidgetContents_10)
        self.Python.setGeometry(QtCore.QRect(80, 200, 151, 41))
        self.Python.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Python.setStyleSheet("border:solid;\n"
"\n"
"background-color: rgb(0, 0, 0,116);\n"
"font: 75 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-width:1;\n"
"border-color: rgb(0, 0, 0);")
        self.Python.setObjectName("Python")
        self.python = QtWidgets.QPushButton(self.scrollAreaWidgetContents_10)
        self.python.setGeometry(QtCore.QRect(8, 200, 51, 40))
        self.python.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.python.setStyleSheet("border-image: url(:/prefix1/images (11).jpg);\n"
"border-radius:10")
        self.python.setText("")
        self.python.setObjectName("python")
        self.java = QtWidgets.QPushButton(self.scrollAreaWidgetContents_10)
        self.java.setGeometry(QtCore.QRect(10, 320, 51, 40))
        self.java.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.java.setStyleSheet("border-image: url(:/prefix1/g (1).png);\n"
"border-radius:10")
        self.java.setText("")
        self.java.setObjectName("java")
        self.c = QtWidgets.QPushButton(self.scrollAreaWidgetContents_10)
        self.c.setGeometry(QtCore.QRect(10, 430, 51, 40))
        self.c.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.c.setStyleSheet("border-image: url(:/prefix1/lc.jpg);\n"
"background:transparent;\n"
"border-radius:10")
        self.c.setText("")
        self.c.setObjectName("c")
        self.pushButton_63 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_10)
        self.pushButton_63.setGeometry(QtCore.QRect(10, 10, 51, 41))
        self.pushButton_63.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_63.setStyleSheet("background:transparent;border-image: url(:/prefix1/iconlistez.png);")
        self.pushButton_63.setText("")
        self.pushButton_63.setObjectName("pushButton_63")
        self.btn_elargie = QtWidgets.QPushButton(self.scrollAreaWidgetContents_10)
        self.btn_elargie.setGeometry(QtCore.QRect(8, 10, 53, 41))
        self.btn_elargie.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_elargie.setStyleSheet("background:transparent;\n"
"border-image: url(:/prefix1/list.png);")
        self.btn_elargie.setText("")
        self.btn_elargie.setObjectName("btn_elargie")
        self.C = QtWidgets.QPushButton(self.scrollAreaWidgetContents_10)
        self.C.setGeometry(QtCore.QRect(80, 430, 151, 41))
        self.C.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.C.setStyleSheet("border:solid;\n"
"\n"
"background-color: rgb(0, 0, 0,116);\n"
"font: 75 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-width:1;\n"
"border-color: rgb(0, 0, 0);")
        self.C.setObjectName("C")
        self.algo = QtWidgets.QPushButton(self.scrollAreaWidgetContents_10)
        self.algo.setGeometry(QtCore.QRect(10, 80, 51, 40))
        self.algo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.algo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.algo.setObjectName("algo")
        self.retressi = QtWidgets.QPushButton(self.scrollAreaWidgetContents_10)
        self.retressi.setGeometry(QtCore.QRect(180, 10, 53, 41))
        self.retressi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.retressi.setStyleSheet("background:transparent;\n"
"border-image: url(:/prefix1/flec.png);")
        self.retressi.setText("")
        self.retressi.setObjectName("retressi")
        self.cache = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.cache.setGeometry(QtCore.QRect(0, 10, 61, 41))
        self.cache.setStyleSheet("background-color: rgb(29, 29, 29);\n"
"")
        self.cache.setText("")
        self.cache.setObjectName("cache")
        self.Algo = QtWidgets.QPushButton(self.scrollAreaWidgetContents_10)
        self.Algo.setGeometry(QtCore.QRect(80, 80, 151, 41))
        self.Algo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Algo.setStyleSheet("\n"
"\n"
"background-color: rgb(0, 0, 0,116);\n"
"font: 75 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border:solid;\n"
"border-width:1;\n"
"border-color: rgb(0, 0, 0);")
        self.Algo.setObjectName("Algo")
        self.Java.raise_()
        self.Python.raise_()
        self.python.raise_()
        self.java.raise_()
        self.c.raise_()
        self.C.raise_()
        self.algo.raise_()
        self.retressi.raise_()
        self.pushButton_63.raise_()
        self.btn_elargie.raise_()
        self.cache.raise_()
        self.Algo.raise_()
        self.doc1.setWidget(self.scrollAreaWidgetContents_10)
        self.label_9.raise_()
        self.label_22.raise_()
        self.label_8.raise_()
        self.label_7.raise_()
        self.groupBox.raise_()
        self.label_11.raise_()
        self.fond1.raise_()
        self.doc1.raise_()
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setGeometry(QtCore.QRect(0, -10, 841, 611))
        self.label_10.setStyleSheet("background-color: rgb(29, 29, 29);\n"
"")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_14 = QtWidgets.QLabel(self.page_3)
        self.label_14.setGeometry(QtCore.QRect(-100, -10, 1031, 661))
        self.label_14.setStyleSheet("border:solid;\n"
"\n"
"background-color: rgb(0, 0, 0,123);\n"
"border-image: url(:/prefix1/h.jpg);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.page_3)
        self.stackedWidget_2.setGeometry(QtCore.QRect(41, 40, 752, 511))
        self.stackedWidget_2.setStyleSheet("background-color: rgb(29, 29, 29);\n"
"")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.texte_code = QtWidgets.QTextEdit(self.page_4)
        self.texte_code.setGeometry(QtCore.QRect(200, 0, 551, 511))
        self.texte_code.setStyleSheet("font: 14pt \"Modern No. 20\";\n"
"color:rgb(255, 255, 255) ;\n"
"/*border-radius:20;*/\n"
"border:solid;\n"
"border-width:1;\n"
"border-color: rgb(255, 255, 255);")
        self.texte_code.setObjectName("texte_code")
        self.toolBox = QtWidgets.QTreeView(self.page_4)
        self.toolBox.setGeometry(QtCore.QRect(0, 0, 191, 511))
        self.toolBox.setStyleSheet("border: 2px solid white")
        self.toolBox.setObjectName("toolBox")
        self.stackedWidget_2.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidget_2.addWidget(self.page_5)
        self.label_16 = QtWidgets.QLabel(self.page_3)
        self.label_16.setGeometry(QtCore.QRect(780, 20, 15, 15))
        self.label_16.setStyleSheet("\n"
"background-color: rgb(255, 0, 0);\n"
"border-radius:90;")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.page_3)
        self.label_17.setGeometry(QtCore.QRect(750, 20, 15, 15))
        self.label_17.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"\n"
"border-radius:90;")
        self.label_17.setObjectName("label_17")
        self.fermer = QtWidgets.QPushButton(self.page_3)
        self.fermer.setGeometry(QtCore.QRect(780, 20, 16, 16))
        self.fermer.setStyleSheet("background:transparent")
        self.fermer.setText("")
        self.fermer.setObjectName("fermer")
        self.un = QtWidgets.QCommandLinkButton(self.page_3)
        self.un.setGeometry(QtCore.QRect(34, 6, 41, 31))
        self.un.setText("")
        self.un.setObjectName("un")
        self.grand = QtWidgets.QPushButton(self.page_3)
        self.grand.setGeometry(QtCore.QRect(750, 20, 16, 16))
        self.grand.setStyleSheet("background:transparent")
        self.grand.setText("")
        self.grand.setObjectName("grand")
        self.doc2 = QtWidgets.QScrollArea(self.page_3)
        self.doc2.setGeometry(QtCore.QRect(-20, 0, 16, 591))
        self.doc2.setStyleSheet("background:transparent;\n"
"background-color: rgb(29, 29, 29);")
        self.doc2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.doc2.setWidgetResizable(True)
        self.doc2.setObjectName("doc2")
        self.scrollAreaWidgetContents_11 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_11.setGeometry(QtCore.QRect(0, 0, 16, 572))
        self.scrollAreaWidgetContents_11.setObjectName("scrollAreaWidgetContents_11")
        self.python_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_11)
        self.python_2.setGeometry(QtCore.QRect(18, 131, 51, 40))
        self.python_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.python_2.setStyleSheet("border-image: url(:/prefix1/images (11).jpg);\n"
"border-radius:10")
        self.python_2.setText("")
        self.python_2.setObjectName("python_2")
        self.java_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_11)
        self.java_2.setGeometry(QtCore.QRect(20, 190, 51, 40))
        self.java_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.java_2.setStyleSheet("border-image: url(:/prefix1/g (1).png);\n"
"border-radius:10")
        self.java_2.setText("")
        self.java_2.setObjectName("java_2")
        self.c_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_11)
        self.c_2.setGeometry(QtCore.QRect(20, 250, 51, 40))
        self.c_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.c_2.setStyleSheet("border-image: url(:/prefix1/lc.jpg);\n"
"background:transparent;\n"
"border-radius:10")
        self.c_2.setText("")
        self.c_2.setObjectName("c_2")
        self.csharp_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_11)
        self.csharp_2.setGeometry(QtCore.QRect(20, 310, 51, 40))
        self.csharp_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.csharp_2.setStyleSheet("border-image: url(:/prefix1/cdsharp.jpg);\n"
"border-radius:10")
        self.csharp_2.setText("")
        self.csharp_2.setObjectName("csharp_2")
        self.cplus_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_11)
        self.cplus_2.setGeometry(QtCore.QRect(20, 370, 51, 40))
        self.cplus_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cplus_2.setStyleSheet("border-image: url(:/prefix1/cplus.png);\n"
"border-radius:10")
        self.cplus_2.setText("")
        self.cplus_2.setObjectName("cplus_2")
        self.php_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_11)
        self.php_2.setGeometry(QtCore.QRect(20, 430, 51, 40))
        self.php_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.php_2.setStyleSheet("border-image: url(:/prefix1/g.png);\n"
"border-radius:10")
        self.php_2.setText("")
        self.php_2.setObjectName("php_2")
        self.js_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_11)
        self.js_2.setGeometry(QtCore.QRect(20, 490, 51, 40))
        self.js_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.js_2.setStyleSheet("border-image: url(:/prefix1/js (2).png);\n"
"border-radius:10")
        self.js_2.setText("")
        self.js_2.setObjectName("js_2")
        self.algo_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_11)
        self.algo_2.setGeometry(QtCore.QRect(20, 70, 51, 40))
        self.algo_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.algo_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10;\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.algo_2.setObjectName("algo_2")
        self.fermer_doc = QtWidgets.QPushButton(self.scrollAreaWidgetContents_11)
        self.fermer_doc.setGeometry(QtCore.QRect(20, 10, 51, 31))
        self.fermer_doc.setStyleSheet("background:transparent")
        self.fermer_doc.setText("")
        self.fermer_doc.setObjectName("fermer_doc")
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents_11)
        self.label_19.setGeometry(QtCore.QRect(26, 10, 41, 31))
        self.label_19.setStyleSheet("border-radius:10;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 0, 0);\n"
"")
        self.label_19.setObjectName("label_19")
        self.python_2.raise_()
        self.java_2.raise_()
        self.c_2.raise_()
        self.csharp_2.raise_()
        self.cplus_2.raise_()
        self.php_2.raise_()
        self.js_2.raise_()
        self.algo_2.raise_()
        self.label_19.raise_()
        self.fermer_doc.raise_()
        self.doc2.setWidget(self.scrollAreaWidgetContents_11)
        self.btn_titre = QtWidgets.QPushButton(self.page_3)
        self.btn_titre.setGeometry(QtCore.QRect(60, 13, 91, 21))
        self.btn_titre.setStyleSheet("background:transparent;")
        self.btn_titre.setText("")
        self.btn_titre.setObjectName("btn_titre")
        self.color = QtWidgets.QLabel(self.page_3)
        self.color.setGeometry(QtCore.QRect(411, 27, 10, 10))
        self.color.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-radius:20")
        self.color.setText("")
        self.color.setObjectName("color")
        self.btn_color = QtWidgets.QPushButton(self.page_3)
        self.btn_color.setGeometry(QtCore.QRect(409, 27, 16, 13))
        self.btn_color.setStyleSheet("background:transparent;\n"
"")
        self.btn_color.setText("")
        self.btn_color.setObjectName("btn_color")
        self.magie = QtWidgets.QLabel(self.page_3)
        self.magie.setGeometry(QtCore.QRect(-20, 0, 21, 571))
        self.magie.setText("")
        self.magie.setObjectName("magie")
        self.langage = QtWidgets.QLabel(self.page_3)
        self.langage.setGeometry(QtCore.QRect(65, 16, 101, 21))
        self.langage.setStyleSheet("font: italic 9pt \"Verdana\";\n"
"color: rgb(255, 255, 255);")
        self.langage.setObjectName("langage")
        self.nom_fichier = QtWidgets.QLabel(self.page_3)
        self.nom_fichier.setGeometry(QtCore.QRect(520, 18, 160, 16))
        self.nom_fichier.setStyleSheet("font: italic 9pt \"Verdana\";\n"
"color: rgb(255, 255, 255);")
        self.nom_fichier.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nom_fichier.setObjectName("nom_fichier")
        self.m = QtWidgets.QPushButton(self.page_3)
        self.m.setGeometry(QtCore.QRect(425, 24, 21, 15))
        self.m.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.m.setStyleSheet("color: rgb(0, 170, 255);\n"
"\n"
"font: 12pt \"Franklin Gothic Demi\";\n"
"background:transparent")
        self.m.setText("")
        self.m.setObjectName("m")
        self.label_10.raise_()
        self.label_14.raise_()
        self.stackedWidget_2.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.fermer.raise_()
        self.un.raise_()
        self.grand.raise_()
        self.doc2.raise_()
        self.color.raise_()
        self.btn_color.raise_()
        self.magie.raise_()
        self.langage.raise_()
        self.btn_titre.raise_()
        self.nom_fichier.raise_()
        self.m.raise_()
        self.stackedWidget.addWidget(self.page_3)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_24 = QtWidgets.QLabel(self.page_6)
        self.label_24.setGeometry(QtCore.QRect(-4, -8, 841, 601))
        self.label_24.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.groupBox_5 = QtWidgets.QGroupBox(self.page_6)
        self.groupBox_5.setGeometry(QtCore.QRect(580, 10, 251, 561))
        self.groupBox_5.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_31 = QtWidgets.QLabel(self.groupBox_5)
        self.label_31.setGeometry(QtCore.QRect(40, 90, 131, 21))
        self.label_31.setStyleSheet("font: 14pt \"Poor Richard\";\n"
"")
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.groupBox_5)
        self.label_32.setGeometry(QtCore.QRect(30, 30, 201, 31))
        self.label_32.setStyleSheet("font: 14pt \"Poor Richard\";\n"
"")
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.groupBox_5)
        self.label_33.setGeometry(QtCore.QRect(40, 140, 131, 21))
        self.label_33.setStyleSheet("font: 14pt \"Poor Richard\";\n"
"")
        self.label_33.setObjectName("label_33")
        self.btn_cle2 = QtWidgets.QPushButton(self.groupBox_5)
        self.btn_cle2.setGeometry(QtCore.QRect(40, 385, 101, 31))
        self.btn_cle2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cle2.setStyleSheet("background:transparent;font: 14pt \"Poor Richard\";border:solid;\n"
"border-bottom:2px solid red;\n"
"\n"
"")
        self.btn_cle2.setText("")
        self.btn_cle2.setObjectName("btn_cle2")
        self.label_50 = QtWidgets.QLabel(self.groupBox_5)
        self.label_50.setGeometry(QtCore.QRect(40, 250, 131, 21))
        self.label_50.setStyleSheet("font: 14pt \"Poor Richard\";\n"
"")
        self.label_50.setObjectName("label_50")
        self.label_52 = QtWidgets.QLabel(self.groupBox_5)
        self.label_52.setGeometry(QtCore.QRect(40, 200, 131, 21))
        self.label_52.setStyleSheet("font: 14pt \"Poor Richard\";\n"
"")
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.groupBox_5)
        self.label_53.setGeometry(QtCore.QRect(40, 300, 131, 21))
        self.label_53.setStyleSheet("font: 14pt \"Poor Richard\";\n"
"")
        self.label_53.setObjectName("label_53")
        self.compte = QtWidgets.QPushButton(self.groupBox_5)
        self.compte.setGeometry(QtCore.QRect(40, 90, 111, 31))
        self.compte.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.compte.setStyleSheet("background:transparent;")
        self.compte.setText("")
        self.compte.setObjectName("compte")
        self.personnalise = QtWidgets.QPushButton(self.groupBox_5)
        self.personnalise.setGeometry(QtCore.QRect(40, 140, 141, 31))
        self.personnalise.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.personnalise.setStyleSheet("background:transparent;")
        self.personnalise.setText("")
        self.personnalise.setObjectName("personnalise")
        self.aide = QtWidgets.QPushButton(self.groupBox_5)
        self.aide.setGeometry(QtCore.QRect(40, 200, 111, 21))
        self.aide.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.aide.setStyleSheet("background:transparent;")
        self.aide.setText("")
        self.aide.setObjectName("aide")
        self.apropos = QtWidgets.QPushButton(self.groupBox_5)
        self.apropos.setGeometry(QtCore.QRect(40, 250, 111, 21))
        self.apropos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.apropos.setStyleSheet("background:transparent;")
        self.apropos.setText("")
        self.apropos.setObjectName("apropos")
        self.contact = QtWidgets.QPushButton(self.groupBox_5)
        self.contact.setGeometry(QtCore.QRect(40, 300, 111, 21))
        self.contact.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.contact.setStyleSheet("background:transparent;")
        self.contact.setText("")
        self.contact.setObjectName("contact")
        self.label_56 = QtWidgets.QLabel(self.groupBox_5)
        self.label_56.setGeometry(QtCore.QRect(40, 390, 131, 21))
        self.label_56.setStyleSheet("font: 14pt \"Poor Richard\";\n"
"")
        self.label_56.setObjectName("label_56")
        self.label_31.raise_()
        self.label_32.raise_()
        self.label_33.raise_()
        self.label_50.raise_()
        self.label_52.raise_()
        self.label_53.raise_()
        self.compte.raise_()
        self.personnalise.raise_()
        self.aide.raise_()
        self.apropos.raise_()
        self.contact.raise_()
        self.label_56.raise_()
        self.btn_cle2.raise_()
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.page_6)
        self.stackedWidget_3.setGeometry(QtCore.QRect(9, 9, 561, 561))
        self.stackedWidget_3.setStyleSheet("background-color: rgb(10, 22, 61);")
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.groupBox_6 = QtWidgets.QGroupBox(self.page_8)
        self.groupBox_6.setGeometry(QtCore.QRect(0, -10, 561, 571))
        self.groupBox_6.setStyleSheet("font: 16pt \"Poor Richard\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.groupBox_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.groupBox_6.setObjectName("groupBox_6")
        self.nom = QtWidgets.QLineEdit(self.groupBox_6)
        self.nom.setGeometry(QtCore.QRect(20, 200, 241, 31))
        self.nom.setStyleSheet("background-color: rgb(255, 255, 255);/*\n"
"border-radius:15;*/\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"background:transparent;\n"
"border:solid;\n"
"border-width:2px;\n"
"color: rgb(255, 255, 255);")
        self.nom.setText("")
        self.nom.setObjectName("nom")
        self.label_23 = QtWidgets.QLabel(self.groupBox_6)
        self.label_23.setGeometry(QtCore.QRect(20, 159, 111, 21))
        self.label_23.setObjectName("label_23")
        self.label_34 = QtWidgets.QLabel(self.groupBox_6)
        self.label_34.setGeometry(QtCore.QRect(20, 270, 111, 21))
        self.label_34.setObjectName("label_34")
        self.prenom = QtWidgets.QLineEdit(self.groupBox_6)
        self.prenom.setGeometry(QtCore.QRect(20, 310, 241, 31))
        self.prenom.setStyleSheet("background-color: rgb(255, 255, 255);/*\n"
"border-radius:15;*/\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"background:transparent;\n"
"border:solid;\n"
"border-width:2px;\n"
"color: rgb(255, 255, 255);")
        self.prenom.setText("")
        self.prenom.setObjectName("prenom")
        self.label_35 = QtWidgets.QLabel(self.groupBox_6)
        self.label_35.setGeometry(QtCore.QRect(310, 150, 111, 41))
        self.label_35.setStyleSheet("background:transparent")
        self.label_35.setObjectName("label_35")
        self.age = QtWidgets.QLineEdit(self.groupBox_6)
        self.age.setGeometry(QtCore.QRect(310, 200, 241, 31))
        self.age.setStyleSheet("background-color: rgb(255, 255, 255);/*\n"
"border-radius:15;*/\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"background:transparent;\n"
"border:solid;\n"
"border-width:2px;\n"
"color: rgb(255, 255, 255);")
        self.age.setText("")
        self.age.setObjectName("age")
        self.label_36 = QtWidgets.QLabel(self.groupBox_6)
        self.label_36.setGeometry(QtCore.QRect(20, 380, 111, 21))
        self.label_36.setObjectName("label_36")
        self.niveau = QtWidgets.QLineEdit(self.groupBox_6)
        self.niveau.setGeometry(QtCore.QRect(20, 420, 241, 31))
        self.niveau.setStyleSheet("background-color: rgb(255, 255, 255);/*\n"
"border-radius:15;*/\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"background:transparent;\n"
"border:solid;\n"
"border-width:2px;\n"
"color: rgb(255, 255, 255);")
        self.niveau.setText("")
        self.niveau.setObjectName("niveau")
        self.label_37 = QtWidgets.QLabel(self.groupBox_6)
        self.label_37.setGeometry(QtCore.QRect(310, 270, 111, 21))
        self.label_37.setObjectName("label_37")
        self.email = QtWidgets.QLineEdit(self.groupBox_6)
        self.email.setGeometry(QtCore.QRect(310, 310, 241, 31))
        self.email.setStyleSheet("background-color: rgb(255, 255, 255);/*\n"
"border-radius:15;*/\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"background:transparent;\n"
"border:solid;\n"
"border-width:2px;\n"
"color: rgb(255, 255, 255);")
        self.email.setText("")
        self.email.setObjectName("email")
        self.label_38 = QtWidgets.QLabel(self.groupBox_6)
        self.label_38.setGeometry(QtCore.QRect(300, 50, 181, 31))
        self.label_38.setObjectName("label_38")
        self.langage_pre = QtWidgets.QComboBox(self.groupBox_6)
        self.langage_pre.setGeometry(QtCore.QRect(300, 90, 241, 31))
        self.langage_pre.setStyleSheet("/*\n"
"border-radius:15;*/\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"background:transparent;\n"
"border:solid;\n"
"border-width:2px;\n"
"color: rgb(255, 255, 255);")
        self.langage_pre.setObjectName("langage_pre")
        self.langage_pre.addItem("")
        self.langage_pre.addItem("")
        self.langage_pre.addItem("")
        self.langage_pre.addItem("")
        self.langage_pre.addItem("")
        self.langage_pre.addItem("")
        self.langage_pre.addItem("")
        self.label_46 = QtWidgets.QLabel(self.groupBox_6)
        self.label_46.setGeometry(QtCore.QRect(310, 380, 181, 31))
        self.label_46.setObjectName("label_46")
        self.matiere = QtWidgets.QLineEdit(self.groupBox_6)
        self.matiere.setGeometry(QtCore.QRect(310, 420, 241, 31))
        self.matiere.setStyleSheet("background-color: rgb(255, 255, 255);/*\n"
"border-radius:15;*/\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"background:transparent;\n"
"border:solid;\n"
"border-width:2px;\n"
"color: rgb(255, 255, 255);")
        self.matiere.setText("")
        self.matiere.setObjectName("matiere")
        self.enregistrer = QtWidgets.QPushButton(self.groupBox_6)
        self.enregistrer.setGeometry(QtCore.QRect(150, 500, 281, 41))
        self.enregistrer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enregistrer.setStyleSheet("\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"background:transparent;\n"
"border:solid;\n"
"border-width:2px;\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 255);")
        self.enregistrer.setObjectName("enregistrer")
        self.btn_foto = QtWidgets.QPushButton(self.groupBox_6)
        self.btn_foto.setGeometry(QtCore.QRect(20, 20, 171, 131))
        self.btn_foto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_foto.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:transparent;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.btn_foto.setText("")
        self.btn_foto.setObjectName("btn_foto")
        self.label_foto = QtWidgets.QLabel(self.groupBox_6)
        self.label_foto.setGeometry(QtCore.QRect(20, 20, 171, 131))
        self.label_foto.setStyleSheet("border-image: url(:/prefix1/images (15).jpg);")
        self.label_foto.setText("")
        self.label_foto.setObjectName("label_foto")
        self.label_foto.raise_()
        self.nom.raise_()
        self.label_23.raise_()
        self.label_34.raise_()
        self.prenom.raise_()
        self.label_35.raise_()
        self.age.raise_()
        self.label_36.raise_()
        self.niveau.raise_()
        self.label_37.raise_()
        self.email.raise_()
        self.label_38.raise_()
        self.langage_pre.raise_()
        self.label_46.raise_()
        self.matiere.raise_()
        self.enregistrer.raise_()
        self.btn_foto.raise_()
        self.stackedWidget_3.addWidget(self.page_8)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.label_54 = QtWidgets.QLabel(self.page_9)
        self.label_54.setGeometry(QtCore.QRect(80, 120, 411, 241))
        self.label_54.setStyleSheet("font: 63 22pt \"Yu Gothic UI Semibold\";\n"
"color: rgb(255, 255, 255);")
        self.label_54.setObjectName("label_54")
        self.stackedWidget_3.addWidget(self.page_9)
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.label_69 = QtWidgets.QLabel(self.page_11)
        self.label_69.setGeometry(QtCore.QRect(10, 80, 551, 311))
        self.label_69.setStyleSheet("font: 63  \"Yu Gothic UI Semibold\";\n"
"color: rgb(255, 255, 255);")
        self.label_69.setObjectName("label_69")
        self.stackedWidget_3.addWidget(self.page_11)
        self.page_22 = QtWidgets.QWidget()
        self.page_22.setObjectName("page_22")
        self.label_71 = QtWidgets.QLabel(self.page_22)
        self.label_71.setGeometry(QtCore.QRect(30, 40, 351, 41))
        self.label_71.setStyleSheet("font: 63  \"Yu Gothic UI Semibold\";\n"
"color: rgb(255, 255, 255);")
        self.label_71.setObjectName("label_71")
        self.textEdit_5 = QtWidgets.QTextEdit(self.page_22)
        self.textEdit_5.setGeometry(QtCore.QRect(40, 120, 421, 341))
        self.textEdit_5.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit_5.setStyleSheet("font: 63  \"Yu Gothic UI Semibold\";\n"
"color: rgb(255, 255, 255);")
        self.textEdit_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_5.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit_5.setPlaceholderText("")
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_15 = QtWidgets.QLabel(self.page_22)
        self.label_15.setGeometry(QtCore.QRect(157, 417, 21, 16))
        self.label_15.setStyleSheet("border-image: url(:/prefix1/coeur.png);")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.stackedWidget_3.addWidget(self.page_22)
        self.page_23 = QtWidgets.QWidget()
        self.page_23.setObjectName("page_23")
        self.label_72 = QtWidgets.QLabel(self.page_23)
        self.label_72.setGeometry(QtCore.QRect(110, 40, 331, 121))
        self.label_72.setStyleSheet("font: 63  \"Yu Gothic UI Semibold\";\n"
"color: rgb(255, 255, 255);")
        self.label_72.setObjectName("label_72")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.page_23)
        self.lineEdit_20.setGeometry(QtCore.QRect(200, 230, 321, 41))
        self.lineEdit_20.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lineEdit_20.setStyleSheet("border-radius:10;\n"
"\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"background:transparent;\n"
"border-bottom:solid;\n"
"border-width:2px;\n"
"border-color: rgb(255, 255, 255);\n"
"color:white;")
        self.lineEdit_20.setReadOnly(True)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.page_23)
        self.lineEdit_22.setGeometry(QtCore.QRect(200, 340, 321, 41))
        self.lineEdit_22.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lineEdit_22.setStyleSheet("color:white;border-radius:10;\n"
"\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"background:transparent;\n"
"border-bottom:solid;\n"
"border-width:2px;\n"
"border-color: rgb(255, 255, 255);")
        self.lineEdit_22.setReadOnly(True)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.label_4 = QtWidgets.QLabel(self.page_23)
        self.label_4.setGeometry(QtCore.QRect(26, 240, 151, 31))
        self.label_4.setStyleSheet("font: 16pt \"Poor Richard\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_29 = QtWidgets.QLabel(self.page_23)
        self.label_29.setGeometry(QtCore.QRect(20, 350, 151, 31))
        self.label_29.setStyleSheet("font: 16pt \"Poor Richard\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_29.setObjectName("label_29")
        self.stackedWidget_3.addWidget(self.page_23)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.label_26 = QtWidgets.QLabel(self.page_7)
        self.label_26.setGeometry(QtCore.QRect(-4, -8, 841, 621))
        self.label_26.setStyleSheet("border-image: url(:/newPrefix/free-business.jpg);")
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.label_28 = QtWidgets.QLabel(self.page_7)
        self.label_28.setGeometry(QtCore.QRect(290, 20, 321, 51))
        self.label_28.setStyleSheet("border:solid;\n"
"border-radius:10;\n"
"")
        self.label_28.setObjectName("label_28")
        self.btn_cle3 = QtWidgets.QPushButton(self.page_7)
        self.btn_cle3.setGeometry(QtCore.QRect(10, 0, 81, 35))
        self.btn_cle3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cle3.setStyleSheet("background:transparent;font: 14pt \"Poor Richard\";border:solid;\n"
"border-bottom:2px solid red;\n"
"\n"
"")
        self.btn_cle3.setText("")
        self.btn_cle3.setObjectName("btn_cle3")
        self.stackedWidget_4 = QtWidgets.QStackedWidget(self.page_7)
        self.stackedWidget_4.setGeometry(QtCore.QRect(20, 140, 801, 401))
        self.stackedWidget_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.stackedWidget_4.setStyleSheet("font: 14pt \"Rockwell\";")
        self.stackedWidget_4.setObjectName("stackedWidget_4")
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.groupBox_7 = QtWidgets.QGroupBox(self.page_12)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 10, 781, 391))
        self.groupBox_7.setStyleSheet("border:solid;border-width:2;\n"
"border-color: rgb(0, 0, 255);background-color: rgb(0, 0, 0,153);")
        self.groupBox_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.groupBox_7.setObjectName("groupBox_7")
        self.pack_logi = QtWidgets.QPushButton(self.groupBox_7)
        self.pack_logi.setGeometry(QtCore.QRect(510, 342, 241, 31))
        self.pack_logi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pack_logi.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.pack_logi.setObjectName("pack_logi")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox_7)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 30, 761, 301))
        self.textEdit_3.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit_3.setStyleSheet("background :transparent;border:transparent;\n"
"\n"
"color: rgb(255, 255, 255);")
        self.textEdit_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName("textEdit_3")
        self.stackedWidget_4.addWidget(self.page_12)
        self.page_20 = QtWidgets.QWidget()
        self.page_20.setObjectName("page_20")
        self.groupBox_9 = QtWidgets.QGroupBox(self.page_20)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 10, 781, 391))
        self.groupBox_9.setStyleSheet("border:solid;border-width:2;\n"
"border-color: rgb(0, 0, 255);background-color: rgb(0, 0, 0,153);")
        self.groupBox_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.groupBox_9.setObjectName("groupBox_9")
        self.pack_formation = QtWidgets.QPushButton(self.groupBox_9)
        self.pack_formation.setGeometry(QtCore.QRect(510, 342, 241, 31))
        self.pack_formation.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pack_formation.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.pack_formation.setObjectName("pack_formation")
        self.textEdit_6 = QtWidgets.QTextEdit(self.groupBox_9)
        self.textEdit_6.setGeometry(QtCore.QRect(10, 30, 681, 311))
        self.textEdit_6.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit_6.setStyleSheet("background :transparent;border:transparent;\n"
"\n"
"color: rgb(255, 255, 255);")
        self.textEdit_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_6.setReadOnly(True)
        self.textEdit_6.setObjectName("textEdit_6")
        self.stackedWidget_4.addWidget(self.page_20)
        self.page_19 = QtWidgets.QWidget()
        self.page_19.setObjectName("page_19")
        self.groupBox_8 = QtWidgets.QGroupBox(self.page_19)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 10, 781, 391))
        self.groupBox_8.setStyleSheet("border:solid;border-width:2;\n"
"border-color: rgb(0, 0, 255);background-color: rgb(0, 0, 0,153);")
        self.groupBox_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.groupBox_8.setObjectName("groupBox_8")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_8)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 30, 761, 301))
        self.textEdit_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit_2.setStyleSheet("background :transparent;border:transparent;\n"
"\n"
"color: rgb(255, 255, 255);")
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.pack_pdf = QtWidgets.QPushButton(self.groupBox_8)
        self.pack_pdf.setGeometry(QtCore.QRect(510, 342, 241, 31))
        self.pack_pdf.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pack_pdf.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.pack_pdf.setObjectName("pack_pdf")
        self.stackedWidget_4.addWidget(self.page_19)
        self.pack1 = QtWidgets.QPushButton(self.page_7)
        self.pack1.setGeometry(QtCore.QRect(30, 120, 121, 31))
        self.pack1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pack1.setStyleSheet("border:solid;border-width:2;\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 255);\n"
"font: 75 16pt \"Rockwell\";\n"
"")
        self.pack1.setObjectName("pack1")
        self.pack2 = QtWidgets.QPushButton(self.page_7)
        self.pack2.setGeometry(QtCore.QRect(160, 120, 151, 31))
        self.pack2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pack2.setStyleSheet("border:solid;border-width:1;\n"
"color: rgb(255, 255, 255);\n"
"/*border-color: rgb(0, 0, 255);*/\n"
"font: 75 16pt \"Rockwell\";\n"
"")
        self.pack2.setObjectName("pack2")
        self.pack3 = QtWidgets.QPushButton(self.page_7)
        self.pack3.setGeometry(QtCore.QRect(320, 120, 161, 31))
        self.pack3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pack3.setStyleSheet("border:solid;border-width:1;\n"
"color: rgb(255, 255, 255);\n"
"/*border-color: rgb(0, 0, 255);*/\n"
"font: 75 16pt \"Rockwell\";\n"
"")
        self.pack3.setObjectName("pack3")
        self.label_57 = QtWidgets.QLabel(self.page_7)
        self.label_57.setGeometry(QtCore.QRect(10, 10, 111, 21))
        self.label_57.setStyleSheet("font: 14pt \"Poor Richard\";\n"
"")
        self.label_57.setObjectName("label_57")
        self.label_26.raise_()
        self.label_28.raise_()
        self.pack1.raise_()
        self.pack2.raise_()
        self.pack3.raise_()
        self.stackedWidget_4.raise_()
        self.label_57.raise_()
        self.btn_cle3.raise_()
        self.stackedWidget.addWidget(self.page_7)
        self.page_21 = QtWidgets.QWidget()
        self.page_21.setObjectName("page_21")
        self.groupBox_2 = QtWidgets.QGroupBox(self.page_21)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 201, 561))
        self.groupBox_2.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"font: 16pt \"Poor Richard\";\n"
"border:solid;\n"
"border-width:1px;\n"
"border-color: transparent;\n"
"")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_45 = QtWidgets.QLabel(self.groupBox_2)
        self.label_45.setGeometry(QtCore.QRect(10, 50, 141, 41))
        self.label_45.setStyleSheet("font: 14pt \"Matura MT Script Capitals\";\n"
"color: rgb(255, 85, 0);\n"
"")
        self.label_45.setObjectName("label_45")
        self.btn_cle2_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_cle2_2.setGeometry(QtCore.QRect(20, 0, 161, 41))
        self.btn_cle2_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cle2_2.setStyleSheet("background:transparent;")
        self.btn_cle2_2.setText("")
        self.btn_cle2_2.setObjectName("btn_cle2_2")
        self.astuce_M = QtWidgets.QPushButton(self.groupBox_2)
        self.astuce_M.setGeometry(QtCore.QRect(10, 130, 121, 23))
        self.astuce_M.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.astuce_M.setStyleSheet("\n"
"border-bottom-color:rgb(255, 85, 0)\n"
"")
        self.astuce_M.setObjectName("astuce_M")
        self.conseil_M = QtWidgets.QPushButton(self.groupBox_2)
        self.conseil_M.setGeometry(QtCore.QRect(50, 160, 91, 23))
        self.conseil_M.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.conseil_M.setStyleSheet("font: 14pt \"Poor Richard\";\n"
"border:solid;\n"
"border-width:1px;\n"
"border-color: transparent;\n"
"\n"
"")
        self.conseil_M.setObjectName("conseil_M")
        self.Lien_M = QtWidgets.QPushButton(self.groupBox_2)
        self.Lien_M.setGeometry(QtCore.QRect(60, 190, 81, 23))
        self.Lien_M.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Lien_M.setStyleSheet("font: 14pt \"Poor Richard\";\n"
"border:solid;\n"
"border-width:1px;\n"
"border-color: transparent;\n"
"\n"
"")
        self.Lien_M.setObjectName("Lien_M")
        self.maquette = QtWidgets.QPushButton(self.groupBox_2)
        self.maquette.setGeometry(QtCore.QRect(60, 220, 131, 23))
        self.maquette.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.maquette.setStyleSheet("font: 14pt \"Poor Richard\";\n"
"border:solid;\n"
"border-width:1px;\n"
"border-color: transparent;\n"
"\n"
"")
        self.maquette.setObjectName("maquette")
        self.conseil_P = QtWidgets.QPushButton(self.groupBox_2)
        self.conseil_P.setGeometry(QtCore.QRect(50, 310, 91, 23))
        self.conseil_P.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.conseil_P.setStyleSheet("font: 14pt \"Poor Richard\";\n"
"border:solid;\n"
"border-width:1px;\n"
"border-color: transparent;\n"
"\n"
"")
        self.conseil_P.setObjectName("conseil_P")
        self.lien_P = QtWidgets.QPushButton(self.groupBox_2)
        self.lien_P.setGeometry(QtCore.QRect(60, 340, 81, 23))
        self.lien_P.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lien_P.setStyleSheet("font: 14pt \"Poor Richard\";\n"
"border:solid;\n"
"border-width:1px;\n"
"border-color: transparent;\n"
"\n"
"")
        self.lien_P.setObjectName("lien_P")
        self.astuce_P = QtWidgets.QPushButton(self.groupBox_2)
        self.astuce_P.setGeometry(QtCore.QRect(10, 270, 181, 31))
        self.astuce_P.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.astuce_P.setObjectName("astuce_P")
        self.autre = QtWidgets.QPushButton(self.groupBox_2)
        self.autre.setGeometry(QtCore.QRect(10, 410, 121, 23))
        self.autre.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.autre.setObjectName("autre")
        self.toolButton = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton.setGeometry(QtCore.QRect(45, 166, 15, 12))
        self.toolButton.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton_2.setGeometry(QtCore.QRect(45, 198, 15, 12))
        self.toolButton_2.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton_3.setGeometry(QtCore.QRect(45, 228, 15, 12))
        self.toolButton_3.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton_4.setGeometry(QtCore.QRect(45, 348, 15, 12))
        self.toolButton_4.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_5 = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton_5.setGeometry(QtCore.QRect(45, 315, 15, 12))
        self.toolButton_5.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_5.setObjectName("toolButton_5")
        self.btn_accueil = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_accueil.setGeometry(QtCore.QRect(10, 525, 91, 31))
        self.btn_accueil.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_accueil.setStyleSheet("background:transparent;font: 14pt \"Poor Richard\";border:solid;\n"
"border-bottom:2px solid red;\n"
"\n"
"")
        self.btn_accueil.setText("")
        self.btn_accueil.setObjectName("btn_accueil")
        self.toolButton_6 = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton_6.setGeometry(QtCore.QRect(45, 378, 15, 12))
        self.toolButton_6.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton_6.setObjectName("toolButton_6")
        self.pdf = QtWidgets.QPushButton(self.groupBox_2)
        self.pdf.setGeometry(QtCore.QRect(60, 370, 31, 23))
        self.pdf.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pdf.setStyleSheet("font: 14pt \"Poor Richard\";\n"
"border:solid;\n"
"border-width:1px;\n"
"border-color: transparent;\n"
"\n"
"")
        self.pdf.setObjectName("pdf")
        self.label_58 = QtWidgets.QLabel(self.groupBox_2)
        self.label_58.setGeometry(QtCore.QRect(10, 530, 111, 21))
        self.label_58.setStyleSheet("font: 14pt \"Poor Richard\";\n"
"")
        self.label_58.setObjectName("label_58")
        self.label_45.raise_()
        self.btn_cle2_2.raise_()
        self.astuce_M.raise_()
        self.conseil_M.raise_()
        self.Lien_M.raise_()
        self.maquette.raise_()
        self.conseil_P.raise_()
        self.lien_P.raise_()
        self.astuce_P.raise_()
        self.autre.raise_()
        self.toolButton.raise_()
        self.toolButton_2.raise_()
        self.toolButton_3.raise_()
        self.toolButton_4.raise_()
        self.toolButton_5.raise_()
        self.toolButton_6.raise_()
        self.pdf.raise_()
        self.label_58.raise_()
        self.btn_accueil.raise_()
        self.stackedWidget_5 = QtWidgets.QStackedWidget(self.page_21)
        self.stackedWidget_5.setGeometry(QtCore.QRect(220, 10, 611, 561))
        self.stackedWidget_5.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.stackedWidget_5.setObjectName("stackedWidget_5")
        self.page_24 = QtWidgets.QWidget()
        self.page_24.setObjectName("page_24")
        self.textEdit_7 = QtWidgets.QTextEdit(self.page_24)
        self.textEdit_7.setGeometry(QtCore.QRect(30, 50, 571, 461))
        self.textEdit_7.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit_7.setStyleSheet("background :transparent;border:transparent;\n"
"\n"
"")
        self.textEdit_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_7.setReadOnly(True)
        self.textEdit_7.setObjectName("textEdit_7")
        self.stackedWidget_5.addWidget(self.page_24)
        self.page_25 = QtWidgets.QWidget()
        self.page_25.setObjectName("page_25")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.page_25)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 50, 571, 461))
        self.textBrowser_2.setStyleSheet("border:none")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.stackedWidget_5.addWidget(self.page_25)
        self.page_26 = QtWidgets.QWidget()
        self.page_26.setObjectName("page_26")
        self.enregistre = QtWidgets.QPushButton(self.page_26)
        self.enregistre.setGeometry(QtCore.QRect(130, 300, 341, 31))
        self.enregistre.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enregistre.setStyleSheet("font: 17pt \"Poor Richard\";\n"
"border:solid;\n"
"border-width:1px;\n"
"border-color: transparent;\n"
"border-color: rgb(0, 0, 255);")
        self.enregistre.setObjectName("enregistre")
        self.label_2 = QtWidgets.QLabel(self.page_26)
        self.label_2.setGeometry(QtCore.QRect(130, 90, 191, 31))
        self.label_2.setStyleSheet("font: 75 18pt \"Segoe MDL2 Assets\";\n"
"\n"
"border:solid;\n"
"border-width:1px;\n"
"border-color: transparent;\n"
"border-bottom-color: rgb(0, 0, 255);")
        self.label_2.setObjectName("label_2")
        self.textEdit_11 = QtWidgets.QTextEdit(self.page_26)
        self.textEdit_11.setGeometry(QtCore.QRect(130, 160, 351, 101))
        self.textEdit_11.setStyleSheet("border:none;\n"
"background-color:transparent;")
        self.textEdit_11.setObjectName("textEdit_11")
        self.stackedWidget_5.addWidget(self.page_26)
        self.page_27 = QtWidgets.QWidget()
        self.page_27.setObjectName("page_27")
        self.textEdit_9 = QtWidgets.QTextEdit(self.page_27)
        self.textEdit_9.setGeometry(QtCore.QRect(20, 50, 571, 441))
        self.textEdit_9.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit_9.setStyleSheet("background :transparent;border:transparent;\n"
"\n"
"")
        self.textEdit_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_9.setReadOnly(True)
        self.textEdit_9.setObjectName("textEdit_9")
        self.stackedWidget_5.addWidget(self.page_27)
        self.page_28 = QtWidgets.QWidget()
        self.page_28.setObjectName("page_28")
        self.textBrowser = QtWidgets.QTextBrowser(self.page_28)
        self.textBrowser.setGeometry(QtCore.QRect(30, 50, 571, 411))
        self.textBrowser.setStyleSheet("border:none")
        self.textBrowser.setObjectName("textBrowser")
        self.stackedWidget_5.addWidget(self.page_28)
        self.page_29 = QtWidgets.QWidget()
        self.page_29.setObjectName("page_29")
        self.textEdit_4 = QtWidgets.QTextEdit(self.page_29)
        self.textEdit_4.setGeometry(QtCore.QRect(13, 20, 591, 491))
        self.textEdit_4.setStyleSheet("border:none;\n"
"background-color:transparent;")
        self.textEdit_4.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit_4.setObjectName("textEdit_4")
        self.stackedWidget_5.addWidget(self.page_29)
        self.page_18 = QtWidgets.QWidget()
        self.page_18.setObjectName("page_18")
        self.enregistre2 = QtWidgets.QPushButton(self.page_18)
        self.enregistre2.setGeometry(QtCore.QRect(120, 320, 341, 31))
        self.enregistre2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enregistre2.setStyleSheet("font: 17pt \"Poor Richard\";\n"
"border:solid;\n"
"border-width:1px;\n"
"border-color: transparent;\n"
"border-color: rgb(0, 0, 255);")
        self.enregistre2.setObjectName("enregistre2")
        self.label_20 = QtWidgets.QLabel(self.page_18)
        self.label_20.setGeometry(QtCore.QRect(110, 120, 411, 141))
        self.label_20.setStyleSheet("font: 75 18pt \"Segoe MDL2 Assets\";\n"
"\n"
"border:solid;\n"
"border-width:1px;\n"
"border-color: transparent;\n"
"")
        self.label_20.setObjectName("label_20")
        self.stackedWidget_5.addWidget(self.page_18)
        self.stackedWidget.addWidget(self.page_21)
        self.label_70 = QtWidgets.QLabel(self.centralwidget)
        self.label_70.setGeometry(QtCore.QRect(720, 540, 111, 41))
        self.label_70.setStyleSheet("font: italic 14pt \"Poor Richard\";\n"
"color: rgb(0, 0, 0);")
        self.label_70.setObjectName("label_70")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 857, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(2)
        self.stackedWidget_4.setCurrentIndex(0)
        self.stackedWidget_5.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Codeur.mi"))
        self.titre.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">codeur.mi</span></p></body></html>"))
        self.texte.setText(_translate("MainWindow", "programmer est un art !"))
        self.astuce.setText(_translate("MainWindow", "A"))
        self.Java.setText(_translate("MainWindow", "langage java"))
        self.Python.setText(_translate("MainWindow", "langage python"))
        self.C.setText(_translate("MainWindow", "langage c"))
        self.algo.setText(_translate("MainWindow", "A"))
        self.Algo.setText(_translate("MainWindow", "algorithme"))
        self.texte_code.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Modern No. 20\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">PROGRAMME ALGO</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">(* Auteur: Emmanuel Malan</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">   date : 09-09-19</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">   detail : programme permettant de calculer le factoriel d\'un nombre entrez au clavier *)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">VARIABLE : </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">    facto, n , val: REEL</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">DEBUT</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">    AFFICHER (&quot;CALCUL DU FACORIEL D UN                 NOMBRE&quot;)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">    AFFICHER (&quot;Entrez un nombre : &quot;)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">    SAISIR (val)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">    n &lt;-- val</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">    facto &lt;-- 1</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">    TANTQUE (n &gt; 1) FAIRE</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">        facto &lt;-- facto * n</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">        n &lt;-- n - 1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">    FIN TANTQUE</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">    AFFICHER (&quot;le factoriel de&quot; + val + &quot;vaut &quot;+ facto)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">FIN</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">    </span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">x</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">¤</span></p></body></html>"))
        self.algo_2.setText(_translate("MainWindow", "A"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">x</span></p></body></html>"))
        self.langage.setText(_translate("MainWindow", "langage python"))
        self.nom_fichier.setText(_translate("MainWindow", "factoriel.py"))
        self.label_31.setText(_translate("MainWindow", "Mon compte"))
        self.label_32.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt;\">Parametre</span></p></body></html>"))
        self.label_33.setText(_translate("MainWindow", "Personnalisation"))
        self.label_50.setText(_translate("MainWindow", "Apropos"))
        self.label_52.setText(_translate("MainWindow", "Aide"))
        self.label_53.setText(_translate("MainWindow", "Contacts"))
        self.label_56.setText(_translate("MainWindow", "Accueil"))
        self.groupBox_6.setTitle(_translate("MainWindow", "mes info"))
        self.label_23.setText(_translate("MainWindow", "Mon Nom :"))
        self.label_34.setText(_translate("MainWindow", "Mon Prenom :"))
        self.label_35.setText(_translate("MainWindow", "Mon Age :"))
        self.label_36.setText(_translate("MainWindow", "Mon Niveau :"))
        self.label_37.setText(_translate("MainWindow", "Mon Email:"))
        self.label_38.setText(_translate("MainWindow", "Mon Langage Preferé :"))
        self.langage_pre.setItemText(0, _translate("MainWindow", "Python"))
        self.langage_pre.setItemText(1, _translate("MainWindow", "Java"))
        self.langage_pre.setItemText(2, _translate("MainWindow", "C"))
        self.langage_pre.setItemText(3, _translate("MainWindow", "C++"))
        self.langage_pre.setItemText(4, _translate("MainWindow", "C#"))
        self.langage_pre.setItemText(5, _translate("MainWindow", "PHP"))
        self.langage_pre.setItemText(6, _translate("MainWindow", "JS"))
        self.label_46.setText(_translate("MainWindow", "Ma Matière Préferé :"))
        self.enregistrer.setText(_translate("MainWindow", "Enregistrer"))
        self.label_54.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Cet Onglet </p><p align=\"center\">Est En Cour </p><p align=\"center\">de Devellopement</p></body></html>"))
        self.label_69.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Ce Logiciel est</span></p><p align=\"center\"><span style=\" font-size:22pt;\">tres simple d\'utilisation</span></p><p align=\"center\"><span style=\" font-size:22pt;\">pas besoin d\'aide pour sa .</span></p><p align=\"center\"><span style=\" font-size:22pt;\">n\'es ce pas?</span></p><p align=\"center\"><span style=\" font-size:22pt;\">dans le cas contraire veuillez me contacter.</span></p></body></html>"))
        self.label_71.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Apropos de Codeur.mi</span></p></body></html>"))
        self.textEdit_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:56; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:13pt; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\"> </span><span style=\" font-size:18pt; font-weight:400;\">Nom du logiciel: </span><span style=\" font-size:18pt; font-weight:600;\">Codeur.mi</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\"> </span><span style=\" font-size:18pt; font-weight:400;\">Version : 1.0.1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:400;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:400;\"> copyright @ 2020 , nucleus inc. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:400;\"> Tous droit réservés </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:400;\"> Licence MIT</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:400;\"> Fait avec     by nucleus @sminth</span></p></body></html>"))
        self.label_72.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Contactez sminth ?</span></p></body></html>"))
        self.lineEdit_20.setText(_translate("MainWindow", "               88 36 44 03"))
        self.lineEdit_22.setText(_translate("MainWindow", "emmanuelmalan225@gmail.com"))
        self.label_4.setText(_translate("MainWindow", "Numero What"))
        self.label_29.setText(_translate("MainWindow", "Email"))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">codeur.mi</span></p></body></html>"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Pack_logiciel"))
        self.pack_logi.setText(_translate("MainWindow", "Telecharger ce pack"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Rockwell\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Ce pack contient une série de logiciel spécifique à certains langage de programmation, offrant à tous debutant un environnement pour commencer a coder .</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">contenue :</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">-Algobox</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">-python 3.8 64 bits</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">-PyQt5 for python 3.5 64 bits</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">-jdk 12</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">-Netbeans IDE</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">-Visual Studio Code</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">-Notepad++</span></p></body></html>"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Pack_formations"))
        self.pack_formation.setText(_translate("MainWindow", "Telecharger ce pact"))
        self.textEdit_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Rockwell\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Ce pack contient une serie de formation specifique à certains langages de programmation, permettant d\'aprofondir ses connaissances en programmation</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">contenue :</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">-Formation Python</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">-Formation java </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">-Formation Html css</span></p></body></html>"))
        self.groupBox_8.setTitle(_translate("MainWindow", "pack pdf"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Rockwell\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Ce pack contient une serie de cour en pdf spécifique à certains langage de programmation, qui seront bénéfique pour tout débutant ne sachant pas par ou et comment commencer à coder .</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">contenue :</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">-AlgoBoxBook</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">-DVD Miage Exo Algo</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">-Apprendre à programmer en python</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">-Exercice python 3</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">-Apprendre à programmer en java</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">-Exercice en java</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">-Apprennez à programmer en C</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">-Un site dynamique avec PHP</span></p></body></html>"))
        self.pack_pdf.setText(_translate("MainWindow", "Telecharger ce pack"))
        self.pack1.setText(_translate("MainWindow", "Pack pdf"))
        self.pack2.setText(_translate("MainWindow", "Pack logiciel"))
        self.pack3.setText(_translate("MainWindow", "Pack formation"))
        self.label_57.setText(_translate("MainWindow", "Accueil"))
        self.label_45.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt;\">Astuces</span></p></body></html>"))
        self.astuce_M.setText(_translate("MainWindow", "Astuces Miage"))
        self.conseil_M.setText(_translate("MainWindow", "Conseils"))
        self.Lien_M.setText(_translate("MainWindow", "Liens utiles"))
        self.maquette.setText(_translate("MainWindow", "Maquette licence"))
        self.conseil_P.setText(_translate("MainWindow", "Conseils"))
        self.lien_P.setText(_translate("MainWindow", "Liens utiles"))
        self.astuce_P.setText(_translate("MainWindow", "Astuces Programmation"))
        self.autre.setText(_translate("MainWindow", "Autres Astuces"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.toolButton_3.setText(_translate("MainWindow", "..."))
        self.toolButton_4.setText(_translate("MainWindow", "..."))
        self.toolButton_5.setText(_translate("MainWindow", "..."))
        self.toolButton_6.setText(_translate("MainWindow", "..."))
        self.pdf.setText(_translate("MainWindow", "Pdf"))
        self.label_58.setText(_translate("MainWindow", "Accueil"))
        self.textEdit_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Vous êtes étudiant à Miage ?</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Miage vous paraît compliqué ?</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Certaines matières vous font peur ?</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Rockwell\'; font-size:18pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Voici 5 astuces, si elles sont bien appliquées démystifie cette utopie selon laquelle la filière miage serait compliquée .</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Rockwell\'; font-size:18pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt; color:#ff5500;\">1)</span><span style=\" font-family:\'Rockwell\'; font-size:18pt;\"> La première astuce est simple : faite tout pour être à l\'heure, toujours copier les leçons, les td et autres...</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">car c\'est seulement avec assiduté, détermination et perséverance qu\'on obtient ce qu\'on désire le plus .</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Rockwell\'; font-size:18pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt; color:#ff5500;\">2)</span><span style=\" font-family:\'Rockwell\'; font-size:18pt;\"> Habituez vous à bosser au jour le jour sans oublier que l\'essentiel n\'est pas de tout bosser mais de bosser l\'essentiel</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Rockwell\'; font-size:18pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt; color:#ff5500;\">3) </span><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Ayez l\'attitude juste. Comme disait un philosophe &quot;toute bataille est gagnée ou perdue d\'avance dans la tête&quot;</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">si vous vous imprégnez d\'une attitude de vainqueur, de premier, alors il n\'y a aucune chance que vous ne validez vos deux semestres</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Rockwell\'; font-size:18pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt; color:#ff5500;\">4) </span><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Apprenez toujours des autres, approchez vous du plus fort, étudiez avec lui sans relâche, donnez vous à fond dans la bosse.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Aussi, les anciens vous seront d\'une grande utilité, ne manquez jamais d\'aller prendre conseil chez un ancien mais aussi de vous  approchez d\'eux pour qu\'il vous aident .</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Rockwell\'; font-size:18pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt; color:#ff5500;\">5)</span><span style=\" font-family:\'Rockwell\'; font-size:18pt;\"> Voici la dernière astuce, la plus méthodique: </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">d\'après la Bible il n\'y a rien de nouveau sous le soleil ainsi sachez qu\'à Miage aucun devoir où examen n\'est descendu du ciel, tout est pareil depuis des lustres .</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Si vous prenez pour habitude de traiter continuellement les exercices,les devoirs et examen du valideur, ou des sujets des années passées alors il n\'y aucune chance que vous ne reussissiez pas .</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">les sujets ne seront pas les mêmes sans aucun doute mais ils auront des simulitudes et avec beaucoup de chance vous pourriez faire des croiso.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Rockwell\'; font-size:18pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Une chôse est sûre, votre avenir à Miage est dans votre main, tenez le bien.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Sur ce, bonne chance !</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Rockwell\'; font-size:18pt;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/prefix1/logo.png\" /></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Voici 5 sites web, des plus populaire, qui vous serons utiles dans votre parcour Miage</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">(liste non exhaustive)</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Rockwell\'; font-size:18pt;\"><br /></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Verdana\'; font-size:8pt; color:#444444;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"www.bibmath.net\"><span style=\" font-size:16pt; text-decoration: underline; color:#0000ff;\">Bibmath</span></a></li>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><a name=\"s-lg-link-desc-31019949\"></a><span style=\" font-family:\'Verdana\'; font-size:16pt; color:#444444;\">S</span><span style=\" font-family:\'Verdana\'; font-size:16pt; color:#444444;\">ite qui comprend un dictionnaire de mathématique (alphabétique et thématique) et qui permet d\'accéder à un ensemble de ressources:exercices, corrigés de concours.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-family:\'Verdana\'; font-size:16pt; color:#444444;\"><br /></p>\n"
"<li style=\" font-family:\'Verdana\'; font-size:16pt; color:#444444;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"www.serge.mehl.free.fr\"><span style=\" text-decoration: underline; color:#0000ff;\">Chronomath</span></a></li>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><a name=\"s-lg-link-desc-31019952\"></a><span style=\" font-family:\'Verdana\'; font-size:16pt; color:#444444;\">C</span><span style=\" font-family:\'Verdana\'; font-size:16pt; color:#444444;\">hronologie de mathématiques pour les professeurs de collège et lycée.<br />Accès à des fiches descriptives gratuites.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-family:\'Verdana\'; font-size:16pt; color:#444444;\"><br /></p>\n"
"<li style=\" font-family:\'Verdana\'; font-size:16pt; color:#444444;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"www.exo7.emath.fr/index.html\"><span style=\" text-decoration: underline; color:#0000ff;\">Exo7 : cours et exercices de mathematiques</span></a></li>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><a name=\"s-lg-link-desc-31020626\"></a><span style=\" font-family:\'Verdana\'; font-size:16pt; color:#444444;\">R</span><span style=\" font-family:\'Verdana\'; font-size:16pt; color:#444444;\">etrouvez des cours, exercices et corrigés, disponible en format Pdf ou vidéo. Niveau licence</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-family:\'Verdana\'; font-size:16pt; color:#444444;\"><br /></p>\n"
"<li style=\" font-family:\'Verdana\'; font-size:16pt; color:#444444;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"fr.khanacademy.org/\"><span style=\" text-decoration: underline; color:#0000ff;\">Khan Academy</span></a></li>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><a name=\"s-lg-link-desc-31020447\"></a><span style=\" font-family:\'Verdana\'; font-size:16pt; color:#444444;\">C</span><span style=\" font-family:\'Verdana\'; font-size:16pt; color:#444444;\">e site édité par une organisation à but non lucratif, propose des cours en ligne sous forme vidéo, disponibles à tous. Une grande partie du site est traduite en français.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-family:\'Verdana\'; font-size:16pt; color:#444444;\"><br /></p>\n"
"<li style=\" font-family:\'Verdana\'; font-size:16pt; color:#444444;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"www.siteduzero.com\"><span style=\" text-decoration: underline; color:#0000ff;\">Open Classrooms, le Site du zéro</span></a></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><a name=\"s-lg-link-desc-31020628\"></a><span style=\" font-family:\'Verdana\'; font-size:16pt; color:#444444;\">P</span><span style=\" font-family:\'Verdana\'; font-size:16pt; color:#444444;\">ropose des tutoriels, principalement en informatique, mais aussi en mathématiques.<br />Propose des cours complets sur différents sujets scientifiques.</span></p></body></html>"))
        self.enregistre.setText(_translate("MainWindow", "Enregistrez la maquette sur son pc"))
        self.label_2.setText(_translate("MainWindow", "Maquette Licence"))
        self.textEdit_11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Elle contient la liste complète et detaillé des matieres de la licence 1 à master 2</span></p></body></html>"))
        self.textEdit_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Tu ne sais pas programmer  ?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">La programmation te parait difficile ?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Tu ne sais pas par ou commencer ?</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Rockwell\'; font-size:18pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Alors voici des conseils de pro qui peuvent bien te guider.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Rockwell\'; font-size:18pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Avant de commencer la moindre ligne de code, tu dois d\'abord te poser un certains nombres de questions</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Rockwell\'; font-size:18pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt; color:#ff5500;\">1.</span><span style=\" font-family:\'Rockwell\'; font-size:18pt;\"> qu\'est-ce que je veux faire PRÉCISÉMENT ?</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Rockwell\'; font-size:18pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Note-le par écrit, n\'hésite pas à faire des petits croquis pour avoir les idées plus claires.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Tu te rendras sans doute compte que tu n\'es pas partie dans la bonne direction pour le moment.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Rockwell\'; font-size:18pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt; color:#ff5500;\">2.</span><span style=\" font-family:\'Rockwell\'; font-size:18pt;\"> DE QUOI je dispose pour le faire ?</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Rockwell\'; font-size:18pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Tu as déjà trouvé deux réponses : un langage de programmation (bravo!) et ton imagination</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Il te manque toutefois la réponse à la troisième question :</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Rockwell\'; font-size:18pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt; color:#ff5500;\">3.</span><span style=\" font-family:\'Rockwell\'; font-size:18pt;\"> avant d\'appeler au secours, OÙ PUIS-JE ME DOCUMENTER ?</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Rockwell\'; font-size:18pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Google est ton ami.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Si tu comprends l\'anglais - ce que tu as intérêt, si tu te destines à une carrière dans l\'informatique - tu trouveras tout ce qu\'il te faut sur internet .</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">AVANT de solliciter la bienveillance d\'autrui, fait tes propres recherches tu auras meilleure réputation, crois-moi.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Rockwell\'; font-size:18pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt; color:#ff5500;\">4.</span><span style=\" font-family:\'Rockwell\'; font-size:18pt;\"> Suis-je assez intelligent pour programmer ?</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Rockwell\'; font-size:18pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Nulle doute qu\'il faut être intelligent et avoir une certaine capacité de reflexion pour pouvoir programmer mais le plus important c\'est l\'imagination, un programmeur intelligent qui n\'a aucune imagination n\'est pas un programmeur, faites travaillez votre imagination pour resoudre les problemes les plus complexe car au fond programmer c\'est un jeu .</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Rockwell\'; font-size:18pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt; color:#ff5500;\">5.</span><span style=\" font-family:\'Rockwell\'; font-size:18pt;\"> Et  apres ?</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Rockwell\'; font-size:18pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Le plus dur c\'est de s\'ameliorer car en dehors des exercices de l\'ecole on ne sait plus quoi fait d\'autre, lancer vous des defis, realisez des programmes utiles, des logiciels,des jeux,des sites web , donnez vous à fond, prennez toujours de l\'avance sur les autres et ayez le desir de toujours vous surpassez.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Rockwell\'; font-size:18pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Allez, courage. On n\'append jamais mieux que par soi-même.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Rockwell\'; font-size:18pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Amuse-toi bien </span><span style=\" font-family:\'Rockwell\'; font-size:18pt; color:#ff5500;\">!</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">Voici 10 sites web, des plus populaire, qui vous serons utiles </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Rockwell\'; font-size:18pt;\">(liste non exhaustive)</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Rockwell\'; font-size:18pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://fr.openclassrooms.com/\"><span style=\" font-size:16pt; text-decoration: underline; color:#0000ff;\">Open Classrooms</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto,Arial,Helvetica,sans-serif\'; font-size:14pt; font-weight:296; color:#555555; background-color:#ffffff;\">Open Classrooms propose des cours de programmation accessibles à tous supports : ordinateur, tablette, smartphone. La plateforme compte plus d’un million d’élèves et propose des forums, afin de faciliter l’entraide. En fin de formation, les élèves reçoivent une attestation de succès qu’ils pourront utiliser pour trouver un emploi de codeur.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Roboto,Arial,Helvetica,sans-serif\'; font-size:14pt; font-weight:296; color:#555555;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://www.developpez.com/\"><span style=\" font-size:16pt; text-decoration: underline; color:#0000ff;\">Developpez.com</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:28px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Roboto,Arial,Helvetica,sans-serif\'; font-size:14pt; font-weight:296; color:#555555; background-color:#ffffff;\">Developpez.com est un hébergeur et un club d’entraide fréquenté par plus de 2 millions d’utilisateurs. Sur la plateforme, les internautes ont à leur disposition des tutoriels, des formations en ligne, des blogs, un forum et un réseau social. Les forums du portail abordent de nombreux sujets, notamment les langages de programmation.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:28px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><a href=\"https://www.codecademy.com/\"><span style=\" font-size:16pt; text-decoration: underline; color:#0000ff;\">Codecademy</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:28px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Roboto,Arial,Helvetica,sans-serif\'; font-size:14pt; font-weight:296; color:#555555;\">Codecademy est le site d’apprentissage de programmation le plus connu. Il propose des exercices interactifs sur les différents langages web (HTML, PHP, Python ou Ruby). Après chaque exercice réussi, l’élève reçoit des points et des trophées, en remplacement des notes. Les cours proposés sont accessibles aux personnes n’ayant aucune connaissance en programmation.</span></p>\n"
"<h3 style=\" margin-top:40px; margin-bottom:20px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><a href=\"http://www.alsacreations.com/tutoriels/\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline; color:#0000ff;\">Alsacréations</span></a></h3>\n"
"<h3 style=\" margin-top:40px; margin-bottom:20px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'Roboto,Arial,Helvetica,sans-serif\'; font-size:14pt; font-weight:296; color:#555555;\">Alsacréations est un site qui se révèle être très utile pour apprendre à coder. Il propose des tutoriels, des astuces et des livres qui traitent de nombreux sujets, en l’occurrence le langage HTML, Cascading Style Sheet, plus connu sous le nom de CSS, le web design et le célèbre JavaScript.</span></h3>\n"
"<h3 style=\" margin-top:40px; margin-bottom:20px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><a href=\"https://www.khanacademy.org/\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline; color:#0000ff;\">Khan Academy</span></a></h3>\n"
"<h3 style=\" margin-top:40px; margin-bottom:20px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-family:\'Roboto,Arial,Helvetica,sans-serif\'; font-size:14pt; font-weight:296; color:#555555;\">Khan Academy met à disposition des exercices, des vidéos, etc. La mission de la plateforme est de permettre d’étudier à un rythme propre à chacun. Il propose des cours de programmation et travaille en partenariat avec la NASA, le Museum of Modern Art, l’Académie des Sciences de Californie et le MIT.</span></h3>\n"
"<p style=\" margin-top:0px; margin-bottom:28px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.codeschool.com/\"><span style=\" font-size:16pt; text-decoration: underline; color:#0000ff;\">Code School</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:28px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto,Arial,Helvetica,sans-serif\'; font-size:14pt; font-weight:296; color:#555555;\">Code School est un site d’apprentissage essentiellement dédié à la programmation. Les cours proposés par la plateforme sont sous forme de “paths” qui traitent d’un sujet défini, notamment le langage Ruby, Javascript, l’HTML/CSS, etc. Dans les “paths”, l’élève apprend progressivement les rouages de chaque langage et de chaque système de programmation.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:28px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://www.programmr.com/\"><span style=\" font-size:16pt; text-decoration: underline; color:#0000ff;\">Programmr</span></a></p>\n"
"<h3 style=\" margin-top:40px; margin-bottom:20px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:\'Roboto,Arial,Helvetica,sans-serif\'; font-size:14pt; font-weight:296; color:#555555;\">Programmr propose des exercices et des cours de programmation et ses langages. Pour permettre aux élèves de se perfectionner, ce site d’apprentissage offre la possibilité de se lancer des défis. Programmr propose des concours qui ont pour objectif de tester les connaissances de chaque apprenant et d’offrir des récompenses aux plus méritants.</span></h3>\n"
"<h3 style=\" margin-top:40px; margin-bottom:20px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><a href=\"https://www.coursera.org/\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline; color:#0000ff;\">Coursera</span></a></h3>\n"
"<h3 style=\" margin-top:40px; margin-bottom:20px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:\'Roboto,Arial,Helvetica,sans-serif\'; font-size:14pt; font-weight:296; color:#555555;\">Coursera est une plateforme incontournable pour suivre en ligne les cours donnés dans les grandes écoles du monde. Dans la programmation des débutants, la plateforme propose une initiation au langage Python prodiguée par l’Université du Michigan. Pour favoriser les élèves au perfectionnement, différents exercices sont proposés lors de l’apprentissage.</span></h3>\n"
"<h3 style=\" margin-top:40px; margin-bottom:20px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><a href=\"http://fr.html.net/tutorials/html/\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline; color:#0000ff;\">HTML.net</span></a></h3>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto,Arial,Helvetica,sans-serif\'; font-size:14pt; font-weight:296; color:#555555;\">HTML.net est un site d’apprentissage du langage HTML. L’accession aux cours ne nécessite aucune connaissance préalable en programmation. Il enseigne les méthodes de création d’un site web et la maîtrise du langage HTML. Le site met à disposition des forums qui abordent des sujets très variés, notamment CSS, PHP, etc.<br /></span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Roboto,Arial,Helvetica,sans-serif\'; font-size:14pt; font-weight:296; color:#555555;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://www.grafikart.fr/\"><span style=\" font-size:16pt; text-decoration: underline; color:#0000ff;\">Grafikart</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto,Arial,Helvetica,sans-serif\'; font-size:14pt; font-weight:296; color:#555555;\">Grafikart est un site ayant pour objectif d’offrir un contenu en langue française concernant le développement web. Il propose des tutoriels et une formation qui traitent des langages HTML/CSS, JavaScript et PHP. Il met à la disposition des apprenants des cours dédiés à l’apprentissage de différents outils, notamment versioning Git.</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Si tu veux être doué en programmation il faut :</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">-</span><span style=\" font-size:20pt;\"> </span><span style=\" font-size:16pt;\">se focaliser sur un langage plutôt que de chercher à tout connaitre</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">-</span><span style=\" font-size:16pt;\"> Se lancer des défis quotidiens afin de se surpasser et de mieux apprendre .</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">- S</span><span style=\" font-size:16pt;\">\'exercer, réaliser des projets afin de mieux vous amelioré et voir l\'étendu du langage que vous aprenez</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Si vous ne savez pas vraiment quel projet ou defis realiser veillez vous referez à mon site web qui contients des exemples de projets et de defis ou veillez entrez en contacte avec moi !</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#0000ff;\">     emmanuelmalan225@gmail.com</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#0000ff;\">     bit.ly/emmanuelmalan</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#0000ff;\">     @sminth 88 36 44 03</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#0000ff;\">     </span></p></body></html>"))
        self.enregistre2.setText(_translate("MainWindow", "Enregistrez"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p>Livre pdf qui detail les 3 étapes pour </p><p>devenir un bon développeur web </p></body></html>"))
        self.label_70.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">by sminth</span></p></body></html>"))
import ress_rc
