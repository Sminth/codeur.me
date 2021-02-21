from ui.signaler import *
import base64,random,time,os
#module pyqt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap, QImage, QPainter, QPainterPath
from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox
import shutil
import glob
class MainWindow(QMainWindow):
    global nom_fichier
    global destination
    def __init__(self):

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        MainWindow.setWindowFlags(self,
                             QtCore.Qt.WindowStaysOnTopHint
                             | QtCore.Qt.FramelessWindowHint
                             | QtCore.Qt.Tool)
        MainWindow.setAttribute(self,QtCore.Qt.WA_TranslucentBackground)
        self.ui.close.clicked.connect(lambda: self.close())
        self.ui.envoyer.clicked.connect(self.envoie)

    def envoie(self):
        if self.ui.nom.text() =="" or self.ui.contact.text() =="" or self.ui.message.toPlainText()=="":
            QMessageBox.information(self,"erreur","""<html><head><meta name="qrichtext" content="1" /><style type="text/css">
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600;">Veillez renseigner tous les champs</span></p></body></html>""")



    def closeEvent(self,event):
        quit()
        ui.close()

if __name__ == '__main__':
    import sys,os
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

#sauvegarde("sminth.py")
