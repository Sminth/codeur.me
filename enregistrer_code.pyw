from ui.enregistrer_code import *
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
        self.ui.close.clicked.connect(lambda : self.close())
        with open("data","r") as d : nom_fichier=d.read()
        self.ui.nom_fichier.setText(nom_fichier)
        self.ui.change.clicked.connect(self.choisir_destination)
        self.ui.enregistrer.clicked.connect(self.enregistrer)
        os.remove("data")

    def choisir_destination(self):
        options = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        dossier = QFileDialog.getExistingDirectory(self,
                "Selectionnez un dossier",
                self.ui.destination.text(), options=options)
        if dossier:
            self.ui.destination.setText(dossier)
            print(dossier)

    def enregistrer(self):
        nom=self.ui.nom_fichier.text()
        lieu=self.ui.destination.text()
        try:

            if not os.path.exists(lieu+"/"+nom) : open(lieu+"/"+nom,'x')
            ok=self.copie("doc/"+nom,lieu+"/"+nom)
            if(ok):
                QMessageBox.information(self,"erreur","""<html><head><meta name="qrichtext" content="1" /><style type="text/css">
                    </style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;">
                    <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600;">Operation Effectuer</span></p></body></html>""")
                self.close()
            else :
                QMessageBox.information(self,"erreur","""<html><head><meta name="qrichtext" content="1" /><style type="text/css">
                    </style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;">
                    <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600;">dsl fichier source inexistant</span></p></body></html>""")
                self.close()
        except PermissionError:
            QMessageBox.information(self,"erreur","""<html><head><meta name="qrichtext" content="1" /><style type="text/css">
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600;">Permission refuser</span></p></body></html>""")

    def copie(self,source, dest,follow_symlinks=True):
        try:
            shutil.copyfile(source, dest,follow_symlinks=True)
            return True
        except Exception:
            return False

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
