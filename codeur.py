"""
@date : 27-08-19
@auteur: Emmanuel Malan
@site:
@email: emmanuelmalan225@gmail.com
@file: codeur.py
@description: logiciel qui contient quelques code source des programmes informatiques usuel
"""

from ui.codeur import *
from fichiers import enregistrer_code
from fichiers import Dialog_signalBug
from fichiers.ligth_py import Highlighter_py
from fichiers.ligth_c import Highlighter_c
from fichiers.ligth_cpp import Highlighter_cpp
from fichiers.ligth_java import Highlighter_java
from fichiers.ligth_algo import Highlighter_algo

import pyperclip, webbrowser, subprocess
import threading,time,random, base64,os
import shutil, glob

#modules pyqt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QFrame, QPushButton
from PyQt5.QtCore import QRect, QPropertyAnimation
from PyQt5.Qt import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import (QDialog, QApplication,QPushButton, QFileDialog, QMainWindow,QMessageBox)
from fichiers.AnimationShadowEffect import AnimationShadowEffect


class StandardItem(QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(255, 255, 225)):
        super().__init__()
 
        fnt = QFont('Open Sans', font_size)
        fnt.setBold(set_bold)
 
        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)


class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #gere l'affichage des differentes pages lorsque l'application est lancer()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget_3.setCurrentIndex(0)
        self.ui.stackedWidget_4.setCurrentIndex(2)
        self.ui.stackedWidget_5.setCurrentIndex(0)
        #self.ui.texte_code.setTextColor(Qt.white)
        #--------------------------------------------------------
        #lorsque le signal d'un bouton est un clic,on se connect a une fonction particulière
        self.ui.btn_cle.clicked.connect(self.acces)
        self.ui.btn_cle2.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.btn_cle3.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.btn_accueil.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.tech.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.para.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.retressi.clicked.connect(self.retressir)
        self.ui.btn_elargie.clicked.connect(self.elargissement)
        self.ui.fermer.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.fermer_doc.clicked.connect(self.fermer)
        self.ui.grand.clicked.connect(self.redimensionner)
        self.ui.btn_color.clicked.connect(lambda : QMessageBox.information(self,"codeur.mi","coder est un art"))
        self.ui.pack1.clicked.connect(self.pack1)
        self.ui.pack_pdf.clicked.connect(lambda : webbrowser.open("nucleus.eblackci.com/recherche?q=pack+pdf",2))
        self.ui.pack2.clicked.connect(self.pack2)
        self.ui.pack_logi.clicked.connect(lambda : webbrowser.open("nucleus.eblackci.com/recherche?q=pack+logiciel"))
        self.ui.pack3.clicked.connect(self.pack3)
        self.ui.pack_formation.clicked.connect(lambda : webbrowser.open("nucleus.eblackci.com/recherche?q=pack+formation"))
        self.ui.compte.clicked.connect(lambda : self.ui.stackedWidget_3.setCurrentIndex(0))
        self.ui.personnalise.clicked.connect(lambda : self.ui.stackedWidget_3.setCurrentIndex(1))
        self.ui.aide.clicked.connect(lambda : self.ui.stackedWidget_3.setCurrentIndex(2))
        self.ui.apropos.clicked.connect(lambda : self.ui.stackedWidget_3.setCurrentIndex(3))
        self.ui.contact.clicked.connect(lambda : self.ui.stackedWidget_3.setCurrentIndex(4))
        self.ui.btn_foto.clicked.connect(self.ajoutfoto)
        self.ui.enregistrer.clicked.connect(self.enregistrer)
        self.ui.astuce.clicked.connect(self.astuce)
        self.ui.autre.clicked.connect(self.autre_astuce)
        self.ui.astuce_M.clicked.connect(self.astuce_Miage)
        self.ui.astuce_P.clicked.connect(self.astuce_Prog)
        self.ui.conseil_M.clicked.connect(self.conseil_M)
        self.ui.Lien_M.clicked.connect(self.lien_M)
        self.ui.maquette.clicked.connect(self.maquette)
        self.ui.pdf.clicked.connect(self.pdf)
        self.ui.conseil_P.clicked.connect(self.conseil_P)
        self.ui.lien_P.clicked.connect(self.lien_P)
        self.ui.enregistre.clicked.connect(lambda : self.sauve('maquettes.xlsx'))
        self.ui.enregistre2.clicked.connect(lambda : self.sauve("3etape.pdf"))
        #--------------------------------------------------
        # activer le suivi position souris
        
        self.ui.label_14.setMouseTracking(True)
        self.ui.label_14.installEventFilter(self)
        self.ui.texte_code.setMouseTracking(True) # active le suivi position souris
        self.ui.texte_code.installEventFilter(self)
        self.ui.toolBox.setMouseTracking(True) # active le suivi position souris
        self.ui.toolBox.installEventFilter(self)
        self.ui.magie.setMouseTracking(True) # active le suivi position souris
        self.ui.magie.installEventFilter(self)
        self.ui.bg.setMouseTracking(True) # active le suivi position souris
        self.ui.bg.installEventFilter(self)
        self.ui.texte.setMouseTracking(True) # active le suivi position souris
        self.ui.texte.installEventFilter(self)
        #self.installEventFilter(self)
        #--------------------------------------------------------
        self.ui.btn_cle.hide()      #cacher un bouton
        self.ui.cache.hide()
        self.init() #apppel de la fonction init

        self.ui.algo.clicked.connect(self.algo)
        self.ui.Algo.clicked.connect(self.algo)
        self.ui.python.clicked.connect(self.python)
        self.ui.Python.clicked.connect(self.python)
        self.ui.java.clicked.connect(self.java)
        self.ui.Java.clicked.connect(self.java)
        self.ui.c.clicked.connect(self.langage_C)
        self.ui.C.clicked.connect(self.langage_C)

        # self.ui.btn_facto.clicked.connect(self.factoriel)
        # self.ui.btn_fibo.clicked.connect(self.fibonacci)
        # self.ui.btn_pdPc.clicked.connect(self.pgcd_ppcm)
        # self.ui.btn_parite.clicked.connect(self.parite)
        # self.ui.btn_nbPr.clicked.connect(self.parf_prem)
        # self.ui.btn_arms.clicked.connect(self.armstrong)
        # self.ui.btn_palin.clicked.connect(self.palindrome)
        # self.ui.btn_maxmin.clicked.connect(self.maxmin)
        # self.ui.btn_tins.clicked.connect(self.trieinsertion)
        # self.ui.btn_tselec.clicked.connect(self.trieselection)
        # self.ui.btn_tbul.clicked.connect(self.triebulle)
        # self.ui.btn_rdicho.clicked.connect(self.dichotomie)
        # self.ui.btn_rseq.clicked.connect(self.sequentielle)

    def init(self):
        """cette fonction s'active lorsque le logiciel est lancer
            permet d'initialiser certaines chose des le depart"""

        self.initTreeView()

        self.couleur=["#ff5500","#ffffff","#00ff00","#0000ff","#ff007f","#ffff00","#ff0000","#5500ff","#005500","#00ffff"]
        self.verif=1;self.magimagi=0
        self.destination = "C:/Users"
        menu = QtWidgets.QMenu()
        menu.addAction('langage algorithmique', self.algo)
        menu.addAction('langage python',self.python)
        menu.addAction('langage java',self.java)
        menu.addAction('langage c',self.langage_C)
        self.ui.btn_titre.setMenu(menu)

        menu2 = QtWidgets.QMenu()
        menu2.addAction('Copier ce code',self.copy_code )
        menu2.addAction('Enregistrer ce code',self.sauve)
        menu2.addAction('Signaler une erreur',lambda : os.startfile("Dialog_signalBug.pyw"))
        self.ui.m.setMenu(menu2)

        self.createActions()
        self.createMenus()
        self.lang="algo"
        if not os.path.exists(r"fichiers\info"):
            with open(r"fichiers\info","w") as f: f.write(str({"codeur X":["codeur X","XX","Licence X","exemple@gmail.com","Python","Suite et fonction derivable","fichiers\\codeur.jpg"]}))
        with open(r"fichiers\info","r") as f : dico=eval(f.read())
        for cle in dico.keys(): self.ui.nom.setText(cle)
        self.ui.prenom.setText(dico[cle][0]) ; self.ui.age.setText(dico[cle][1])
        self.ui.niveau.setText(dico[cle][2]) ; self.ui.email.setText(dico[cle][3])
        self.ui.langage_pre.setCurrentText(dico[cle][4]) ; self.ui.matiere.setText(dico[cle][5])
        self.ajoutfoto(dico[cle][6])
        self.fileName=None
        self.passe=1
        """if not os.path.exists(r"C:\.codeur"):
            print("pas")
            os.makedirs(r"C:\.codeur")
        if not os.path.isfile(r"C:\.codeur\passe.txt"):
            print("n'existe pas")
            self.passe=0"""

    def initTreeView(self) :
        self.ui.toolBox.setHeaderHidden(True)
        self.ui.toolBox.setDragDropMode(QAbstractItemView.InternalMove)
        self.treeModel = QStandardItemModel()
        rootNode = self.treeModel.invisibleRootItem()
        
        #basic
        basic = StandardItem('CODE BASIC', 12, set_bold=True)
        factoriel = StandardItem('Factoriel',12)
        factoriel.setData('facto')
        fibonacci = StandardItem('Fibonacci',12)
        pgcdPpcm = StandardItem('PGCD | PPCM',14)
        parite = StandardItem('Parite d\'un nombre',12)
        parite.setToolTip('Parite d\'un nombre')
        equation1 = StandardItem('Equation du 1er degré',12)
        equation1.setToolTip('Equation du 1er degré')
        parfait_premier = StandardItem('Nombre parfait | premier',12)
        parfait_premier.setToolTip('Nombre parfait | premier')
        basic.appendRows([factoriel,fibonacci,pgcdPpcm,parite,equation1,parfait_premier])

        #avance
        avance = StandardItem('CODE AVANCE', 12, set_bold=True)
        armstrong = StandardItem('Armstrong',12)
        palindrome = StandardItem('Palindrome',12)
        equation2 = StandardItem('Equation du 2nd degré',12)
        equation2.setToolTip('Equation du 2nd degré')
        avance.appendRows([armstrong,palindrome,equation2])

        #tableau
        tableau = StandardItem('GESTION TABLEAU', 12, set_bold=True)
        creationTb = StandardItem('Creer & remplir un tableau',12)
        creationTb.setToolTip('Creer & remplir un tableau')
        maxmin = StandardItem('Maximum & Minimum d\'un tableau',12)
        maxmin.setToolTip('Maximum & Minimum d\'un tableau')
        sequentielle = StandardItem('Recherche sequentielle',12)
        sequentielle.setToolTip('Recherche sequentielle')
        dichotomie = StandardItem('Recherche dichotomique',12)
        dichotomie.setToolTip('Recherche dichotomique')
        triebulle = StandardItem('Trie Bulle',12)
        trieinsertion = StandardItem('Trie par insertion',12)
        trieselection = StandardItem('Trie par selection',12)
        tableau.appendRows([creationTb,maxmin,sequentielle,dichotomie,triebulle,trieinsertion,trieselection])

        rootNode.appendRow(basic)
        rootNode.appendRow(avance)
        rootNode.appendRow(tableau)

        self.ui.toolBox.setModel(self.treeModel)
        self.ui.toolBox.expandAll()
        self.data ={'Recherche dichotomique':'self.dichotomie()','Trie Bulle':'self.triebulle()','Trie par insertion':'self.trieinsertion()','Trie par selection':'self.trieselection()',"Recherche sequentielle":'self.sequentielle()',"Maximum & Minimum d'un tableau":'self.maxmin()','Palindrome':'self.palindrome()',"Factoriel":'self.factoriel()','PGCD | PPCM':'self.pgcd_ppcm()',"Parite d'un nombre":'self.parite()','Nombre parfait | premier':'self.parf_prem()',"Armstrong" : 'self.armstrong()','Fibonacci': 'self.fibonacci()'}
        self.ui.toolBox.clicked.connect(self.getValue)
        self.ui.toolBox.doubleClicked.connect(self.getValue)
    
    def getValue(self, val):
        val = val.data()
        print(val)
        if(val in self.data): exec(self.data[val])
        # print(val.row())
        # print(val.column())

    def algo(self):
        """ cette fonction est lancer quand l'utilsateur clic sur le bouton 'algorithme'
            elle se charge d'aller a la page 2 et de mettre dans l'editeur le code du
            programme factoriel en algo """
        self.lang="algo"
        self.ui.stackedWidget.setCurrentIndex(2)
        with open("doc/facto_algo.txt") as f : cont=f.read()
        self.ui.texte_code.setHtml(cont)
        self.ui.langage.setText("algorithme")
        self.ui.nom_fichier.setText("factoriel.txt")
        try: self.highlighter = Highlighter_algo(self.ui.texte_code.document())   #pour la coloration syntaxique dans le textEdit
        except:
            QMessageBox.information(self,"erreur","erreur avec la coloration syntaxique ")
            #self.ui.texte_code.setText("")

    def python(self):
        """ cette fonction est lancer quand l'utilsateur clic sur le bouton 'langage python'
            elle se charge d'aller a la page 2 et de mettre dans l'editeur le code du
            programme factoriel en python """
        self.lang="py"
        self.ui.stackedWidget.setCurrentIndex(2)
        with open("doc/facto_py.txt") as f : cont=f.read()
        self.ui.texte_code.setHtml(cont)
        self.ui.langage.setText("langage python")
        self.ui.nom_fichier.setText("factoriel.py")
        try: self.highlighter = Highlighter_py(self.ui.texte_code.document())   #pour la coloration syntaxique dans le textEdit
        except:
            QMessageBox.information(self,"erreur","erreur avec la coloration syntaxique ")
            #self.ui.texte_code.setText("")

    def langage_C(self):
        """"cette fonction est lancer quand l'utilsateur clic sur le bouton 'langage c'
            elle se charge d'aller a la page 2 et de mettre dans l'editeur le code du
            programme factoriel en c """
        try: self.highlighter = Highlighter_c(self.ui.texte_code.document())    #pour la coloration syntaxique dans le textEdit
        except:
            QMessageBox.information(self,"erreur","erreur avec la coloration syntaxique ")
            self.ui.text_code.setText("")
        self.lang="c"
        self.ui.stackedWidget.setCurrentIndex(2)
        with open("doc/facto_c.txt") as f : cont=f.read()
        self.ui.texte_code.setHtml(cont)
        self.ui.langage.setText("langage c")
        self.ui.nom_fichier.setText("factoriel.c")
    
    def java(self):
        """"cette fonction est lancer quand l'utilsateur clic sur le bouton 'langage java'
            elle se charge d'aller a la page 2 et de mettre dans l'editeur le code du
            programme factoriel en java """
        self.lang="java"
        self.ui.stackedWidget.setCurrentIndex(2)
        with open("doc/facto_java.txt") as f : cont=f.read()
        self.ui.texte_code.setHtml(cont)
        self.ui.langage.setText("langage java")
        self.ui.nom_fichier.setText("factoriel.java")
        try: self.highlighter = Highlighter_java(self.ui.texte_code.document())    #pour la coloration syntaxique dans le textEdit
        except:
            QMessageBox.information(self,"erreur","erreur avec la coloration syntaxique ")
            self.ui.texte_code.setHtml(cont)

    def factoriel(self):
        try:
            """"cette fonction est lancer quand l'utilsateur clic sur le bouton 'factoriel'
                elle se charge de mettre dans l'editeur le code du programme factoriel dans
                le langage correspondant"""
            if self.lang=="py":
                with open("doc/facto_py.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("factoriel.py")
            elif self.lang=="c":
                with open("doc/facto_c.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("factoriel.c")
            elif self.lang=="java":
                with open("doc/facto_java.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("factoriel.java")
            elif self.lang=="algo":
                with open("doc/facto_algo.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("factoriel.txt")
            
        except:
            QMessageBox.information(self,"erreur","fichier source non trouver")
    
    def fibonacci(self):
        try:
            """"cette fonction est lancer quand l'utilsateur clic sur le bouton 'fibonacci'
                elle se charge de mettre dans l'editeur le code du programme fibonacci dans
                le langage correspondant"""
            if self.lang=="py":
                with open("doc/fibo_py.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("fibonacci.py")
            elif self.lang=="c":
                with open("doc/fibo_c.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("fibonacci.c")
            elif self.lang=="algo":
                with open("doc/fibo_algo.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("fibonacci.txt")
            elif self.lang=="java":
                with open("doc/fibo_java.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("fibonacci.java")
        except:
            QMessageBox.information(self,"erreur","fichier source non trouver")
    
    def pgcd_ppcm(self):
        try:

            """"cette fonction est lancer quand l'utilsateur clic sur le bouton 'pgcd ppcm'
                elle se charge de mettre dans l'editeur le code du programme pgcd ppcm  dans
                le langage correspondant"""
            if self.lang=="py":
                with open("doc/pp_py.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("pgcd_ppcm.py")
            elif self.lang=="c":
                with open("doc/pp_c.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("pgcd_ppcm.c")
            elif self.lang=="algo":
                with open("doc/pp_algo.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("pgcd_ppcm.txt")
            elif self.lang=="java":
                with open("doc/pp_java.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("pgcd_ppcm.java")
        except:
            QMessageBox.information(self,"erreur","fichier source non trouver")
    
    def parite(self):
        try:

            """"cette fonction est lancer quand l'utilsateur clic sur le bouton 'parite'
                elle se charge de mettre dans l'editeur le code du programme parite  dans
                le langage correspondant"""
            if self.lang=="py":
                with open("doc/parite_py.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("parite.py")
            elif self.lang=="c":
                with open("doc/parite_c.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("parite.c")
            elif self.lang=="algo":
                with open("doc/parite_algo.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("parite.txt")
            elif self.lang=="java":
                with open("doc/parite_java.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("parite.cpp")
        except:
            QMessageBox.information(self,"erreur","fichier source non trouver")
            
    def parf_prem(self):
        try:
            """"cette fonction est lancer quand l'utilsateur clic sur le bouton 'nombre parfait|premier'
                elle se charge de mettre dans l'editeur le code du programme parfait_premier  dans
                le langage correspondant"""
            if self.lang=="py":
                with open("doc/parfPrem_py.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("parfait_premier.py")
            elif self.lang=="c":
                with open("doc/parfPrem_c.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("parfait_premier.c")
            elif self.lang=="algo":
                with open("doc/parfPrem_algo.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("parfait_premier.txt")
            elif self.lang=="java":
                with open("doc/parfPrem_java.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("parfait_premier.java")
        except:
            QMessageBox.information(self,"erreur","fichier source non trouver")
    
    def armstrong(self):
        try:

            """cette fonction est lancer quand l'utilsateur clic sur le bouton 'armstrong'
                elle se charge de mettre dans l'editeur le code du programme armstrong  dans
                le langage correspondant"""
            if self.lang=="py":
                with open("doc/arms_py.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("armstrong.py")
            elif self.lang=="c":
                with open("doc/arms_c.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("armstrong.c")
            elif self.lang=="java":
                with open("doc/arms_java.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("armstrong.java")
            elif self.lang=="algo":
                with open("doc/arms_algo.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("armstrong.txt")

        except:
            QMessageBox.information(self, "erreur", "fichier source non trouver")

    def palindrome(self):
        try:

            """cette fonction est lancer quand l'utilsateur clic sur le bouton 'palindrome'
                elle se charge de mettre dans l'editeur le code du programme palindrome  dans
                le langage correspondant"""
            if self.lang=="py":
                with open("doc/palin_py.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("palindrome.py")
            elif self.lang=="c":
                with open("doc/palin_c.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("palindrome.c")
            elif self.lang=="java":
                with open("doc/palin_java.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("palindrome.java")
            elif self.lang=="algo":
                with open("doc/palin_algo.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("palindrome.txt")
        except:
            QMessageBox.information(self, "erreur", "fichier source non trouver")

    def maxmin(self):
        try:

            """cette fonction est lancer quand l'utilsateur clic sur le bouton 'maximum et minimum'
                elle se charge de mettre dans l'editeur le code du programme maxmin  dans
                le langage correspondant"""
            if self.lang=="py":
                with open("doc/maxmin_py.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("maxmin.py")
            elif self.lang=="c":
                with open("doc/maxmin_c.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("maxmin.c")
            elif self.lang=="java":
                with open("doc/maxmin_java.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("maxmin.java")
            elif self.lang=="algo":
                with open("doc/maxmin_algo.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("maxmin.txt")

        except:
            QMessageBox.information(self, "erreur", "fichier source non trouver")

    def trieinsertion(self):
        try:

            """cette fonction est lancer quand l'utilsateur clic sur le bouton 'trie par insertion'
                elle se charge de mettre dans l'editeur le code du programme maxmin  dans
                le langage correspondant"""
            if self.lang=="py":
                with open("doc/trieinsertion_py.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("trieinsertion.py")
            elif self.lang=="c":
                with open("doc/trieinsertion_c.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("trieinsertion.c")
            elif self.lang=="java":
                with open("doc/trieinsertion_java.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("trieinsertion.java")
            elif self.lang=="algo":
                with open("doc/trieinsertion_algo.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("trieinsertion.txt")

        except:
            QMessageBox.information(self, "erreur", "fichier source non trouver")

    def trieselection(self):
        try:

            """cette fonction est lancer quand l'utilsateur clic sur le bouton 'trie par selection'
                elle se charge de mettre dans l'editeur le code du programme maxmin  dans
                le langage correspondant"""
            if self.lang=="py":
                with open("doc/trieselection_py.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("trieselection.py")
            elif self.lang=="c":
                with open("doc/trieselection_c.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("trieselection.c")
            elif self.lang=="java":
                with open("doc/trieselection_java.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("trieselection.java")
            elif self.lang=="algo":
                with open("doc/trieselection_algo.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("trieselection.txt")

        except:
            QMessageBox.information(self, "erreur", "fichier source non trouver")

    def triebulle(self):
        try:

            """cette fonction est lancer quand l'utilsateur clic sur le bouton 'trie bulle'
                elle se charge de mettre dans l'editeur le code du programme maxmin  dans
                le langage correspondant"""
            if self.lang=="py":
                with open("doc/triebulle_py.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("triebulle.py")
            elif self.lang=="c":
                with open("doc/triebulle_c.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("triebulle.c")
            elif self.lang=="java":
                with open("doc/triebulle_java.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("triebulle.java")
            elif self.lang=="algo":
                with open("doc/triebulle_algo.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("triebulle.txt")

        except:
            QMessageBox.information(self, "erreur", "fichier source non trouver")

    def dichotomie(self):
        try:

            """cette fonction est lancer quand l'utilsateur clic sur le bouton 'recherche dichotomique'
                elle se charge de mettre dans l'editeur le code du programme maxmin  dans
                le langage correspondant"""
            if self.lang=="py":
                with open("doc/dichotomie_py.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("dichotomie.py")
            elif self.lang=="c":
                with open("doc/dichotomie_c.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("dichotomie.c")
            elif self.lang=="java":
                with open("doc/dichotomie_java.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("dichotomie.java")
            elif self.lang=="algo":
                with open("doc/dichotomie_algo.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("dichotomie.txt")

        except:
            QMessageBox.information(self, "erreur", "fichier source non trouver")

    def sequentielle(self):
        try:

            """cette fonction est lancer quand l'utilsateur clic sur le bouton 'recherche sequentielle'
                elle se charge de mettre dans l'editeur le code du programme maxmin  dans
                le langage correspondant"""
            if self.lang=="py":
                with open("doc/sequentielle_py.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("sequentielle.py")
            elif self.lang=="c":
                with open("doc/sequentielle_c.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("sequentielle.c")
            elif self.lang=="java":
                with open("doc/sequentielle_java.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("sequentielle.java")
            elif self.lang=="algo":
                with open("doc/sequentielle_algo.txt") as f : cont=f.read()
                self.ui.texte_code.setHtml(cont)
                self.ui.nom_fichier.setText("sequentielle.txt")

        except:
            QMessageBox.information(self, "erreur", "fichier source non trouver")

    def enterEvent(self, event):
        """ evenement sur la sourie (entrez de la sourie dans le logiciel)"""
        #print ("event ")
        x=event.pos().x()
        y=event.pos().y()
        #print ("MouseMove : x="+ str(x) + " y= " + str(y))

    def leaveEvent(self, event):
        """ evenement sur la sourie (sortie de la sourie hors du logiciel)"""
        print ("curseur sortie")

    def eventFilter(self, srcEvent, event): # fonction pour gérer filtrage évènements - reçoit l'objet source de l'évènement
        """evenement sur la sourie
            filtre chaque evenement"""
        if srcEvent==self.ui.label_14 or srcEvent==self.ui.magie or srcEvent==self.ui.texte_code or srcEvent==self.ui.toolBox : # teste si la source de l'évènement est bien le label - utile si plusieurs sources d'évènements activées

                if event.type() == QEvent.MouseMove: # si évènement "mouvement de la souris"
                        self.x=event.pos().x() # coordonnée souris au moment évènement dans le widget source de l'évènement =
                        self.y=event.pos().y()
                        #print ("souris est ixi : x="+ str(self.x) + " y= " + str(self.y)) # affiche coordonnées
                        #if 0<=self.x<=30 and 14<=self.y<=560: self.apparait()
                        #else: self.fermer()
        elif srcEvent==self.ui.bg:
            if event.type() == QEvent.MouseMove:
                x=event.pos().x()
                y=event.pos().y()
                #print ("souris est ixi : x="+ str(x) + " y= " + str(y)) # affiche coordonnées
                if 160<=x<=680 and 110<=y<=230:

                    couleur=random.choice(self.couleur)
                    self.ui.titre.setStyleSheet("background-color: "+couleur+";border-radius:10;")

                else:
                    self.ui.titre.setStyleSheet("border:solid;\n"
                    "color: rgb(255, 255, 255);\n"
                    "border-radius:10;\n"
                    "background-color: rgb(0, 0, 0,96);")
        elif srcEvent==self.ui.texte:
            
            if event.type() == QEvent.MouseMove:
                # print("leghjh")
                x=event.pos().x()
                y=event.pos().y()
                #print("x:",x,"y:",y)
                if 0<x<260 and 30<y<80:
                    self.ui.line.hide()
                    self.ui.texte.setStyleSheet("font: 27pt \"Poor Richard\";\n"
            "color: rgb(0, 250, 0);")
                    self.ui.btn_cle.show()
                else:
                    self.ui.line.show()
                    self.ui.texte.setStyleSheet("font: 27pt \"Poor Richard\";color: rgb(255, 255, 255);")
                    self.ui.btn_cle.hide()
        return False

    """"ces fonctions(pack1,pack2,pack3) sont lancer quand l'utilsateur clic sur un des bouton suivants : 'pack pdf',"pack formation",'pack logiciel'
        elle se charge d'aller a la page correspondante au bouton clicquer et de changer
        la couleur des bordures du bouton en question et des 2 autres boutons pour un effet d'animation"""
    def pack1(self):
        self.ui.stackedWidget_4.setCurrentIndex(2)
        self.ui.pack1.setStyleSheet("border:solid;border-width:2;\n"
            "color: rgb(0, 0, 0);\n"
            "border-color: rgb(0, 0, 255);\n"
            "font: 75 16pt \"Rockwell\";\n"
            "")

        self.ui.pack2.setStyleSheet("border:solid;border-width:1;\n"
            "color: rgb(255, 255, 255);\n"
            "/*border-color: rgb(0, 0, 255);*/\n"
            "font: 75 16pt \"Rockwell\";\n"
            "")
        self.ui.pack3.setStyleSheet("border:solid;border-width:1;\n"
            "color: rgb(255, 255, 255);\n"
            "/*border-color: rgb(0, 0, 255);*/\n"
            "font: 75 16pt \"Rockwell\";\n"
            "")

    def pack2(self):
        self.ui.stackedWidget_4.setCurrentIndex(0)
        self.ui.pack2.setStyleSheet("border:solid;border-width:2;\n"
            "color: rgb(0, 0, 0);\n"
            "border-color: rgb(0, 0, 255);\n"
            "font: 75 16pt \"Rockwell\";\n"
            "")
        self.ui.pack1.setStyleSheet("border:solid;border-width:1;\n"
            "color: rgb(255, 255, 255);\n"
            "/*border-color: rgb(0, 0, 255);*/\n"
            "font: 75 16pt \"Rockwell\";\n"
            "")
        self.ui.pack3.setStyleSheet("border:solid;border-width:1;\n"
            "color: rgb(255, 255, 255);\n"
            "/*border-color: rgb(0, 0, 255);*/\n"
            "font: 75 16pt \"Rockwell\";\n"
            "")
    
    def pack3(self):
        self.ui.stackedWidget_4.setCurrentIndex(1)
        self.ui.pack3.setStyleSheet("border:solid;border-width:2;\n"
            "color: rgb(0, 0, 0);\n"
            "border-color: rgb(0, 0, 255);\n"
            "font: 75 16pt \"Rockwell\";\n"
            "")
        self.ui.pack2.setStyleSheet("border:solid;border-width:1;\n"
            "color: rgb(255, 255, 255);\n"
            "/*border-color: rgb(0, 0, 255);*/\n"
            "font: 75 16pt \"Rockwell\";\n"
            "")
        self.ui.pack1.setStyleSheet("border:solid;border-width:1;\n"
            "color: rgb(255, 255, 255);\n"
            "/*border-color: rgb(0, 0, 255);*/\n"
            "font: 75 16pt \"Rockwell\";\n"
            "")

    def copy_code(self):
        """"cette fonction est lancer quand l'utilsateur clic sur l'option 'copier ce code'
            elle se charge de copier dans le presse papier le code contenue dans l'editeur"""
        pyperclip.copy(self.ui.texte_code.toPlainText())
        QMessageBox.information(self,"codeur.mi","code copié dans le presse papier")
        
    def sauve(self, nom=""):
        """"cette fonction est lancer quand l'utilsateur clic sur l'option 'enregistrer ce code'
            elle se charge d'enregistrer le programme contenue dans l'editeur
            dans l'ordi de l'utilisateur apres qu'il ai choisir la destination du fichier"""
        if nom == "" : nom=self.ui.nom_fichier.text()
        options = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        dossier = QFileDialog.getExistingDirectory(self,
                "Selectionnez un dossier",
                self.destination, options=options)
        if dossier:
            self.destination=dossier
            print(dossier)
            self.enregistrerFichier(nom)
   

    def enregistrerFichier(self,nom):
        lieu=self.destination
        try:

            if not os.path.exists(lieu+"/"+nom) : open(lieu+"/"+nom,'x')
            ok=self.copie("doc/"+nom,lieu+"/"+nom)

            if(ok):
                QMessageBox.information(self,"erreur","""<html><head><meta name="qrichtext" content="1" /><style type="text/css">
                    </style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;">
                    <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600;">Operation Effectuer</span></p></body></html>""")
                
            else :
                QMessageBox.information(self,"erreur","""<html><head><meta name="qrichtext" content="1" /><style type="text/css">
                    </style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;">
                    <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600;">dsl fichier source inexistant</span></p></body></html>""")
                
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

   
    def lum(self):
        "permet de faire le jeu de lumiere"
        print("lum")
        temp=10000
        while temp>1:
            for color in self.couleur:
                self.ui.color.setStyleSheet("background-color: "+color+";")
                time.sleep(0.5)
            temp-=1

    def acces(self):
        """cette fonction est lancer quand l'utilsateur clic sur le bouton 'se lancer dans la programmation'
           permet d'aller a la page 1 et d'appeler la fonction lum(self)
          """
        print("acces")
        if (self.passe==0):
             h=time.strftime('%H')
             m=time.strftime('%M')
             text, ok = QInputDialog.getText(self, "codeur.mi",
                "Entrez votre code d'acces", QLineEdit.Normal, QDir.home().dirName())
             if ok and text !='':
                 if h in text and m in text and "$" in text:
                     print(text)
                     with open(r"C:\.codeur\passe.txt","w") : pass
                     subprocess.check_call(["attrib","+H",r"C:\.codeur\passe.txt"])
                     
                     threading.Thread(target=self.lum).start()
                 else: self.acces()
             else: self.acces()
        self.ui.stackedWidget.setCurrentIndex(1)

    """ fonctions : conseil_M,conseil_P,lien_M,lien_P,maquette,Astuce_Miage,astuce_Prog,autre_astuce
        Toutes ces fonctions concerne l'onglet "conseil"
        tout est gerer : animation(changement de couleur), clic sur un bouton(changer de page),etc.."""
    def conseil_M(self):
        self.ui.stackedWidget_5.setCurrentIndex(0)
        self.ui.astuce_M.setStyleSheet("border-bottom-color:rgb(255, 85, 0)")
        self.ui.autre.setStyleSheet("")
        self.ui.astuce_P.setStyleSheet("")
        self.ui.astuce_M.setStyleSheet("border-bottom-color:rgb(255, 85, 0)")
   
    def conseil_P(self):
        self.ui.stackedWidget_5.setCurrentIndex(3)
        self.ui.astuce_P.setStyleSheet("border-bottom-color:rgb(255, 85, 0)")
        self.ui.autre.setStyleSheet("")
        self.ui.astuce_M.setStyleSheet("")
        self.ui.astuce_P.setStyleSheet("border-bottom-color:rgb(255, 85, 0)")
   
    def lien_M(self):
        self.ui.stackedWidget_5.setCurrentIndex(1)
        self.ui.astuce_M.setStyleSheet("border-bottom-color:rgb(255, 85, 0)")
        self.ui.autre.setStyleSheet("")
        self.ui.astuce_P.setStyleSheet("")
        self.ui.astuce_M.setStyleSheet("border-bottom-color:rgb(255, 85, 0)")
    
    def lien_P(self):
        self.ui.stackedWidget_5.setCurrentIndex(4)
        self.ui.astuce_P.setStyleSheet("border-bottom-color:rgb(255, 85, 0)")
        self.ui.autre.setStyleSheet("")
        self.ui.astuce_M.setStyleSheet("")
        self.ui.astuce_P.setStyleSheet("border-bottom-color:rgb(255, 85, 0)")
    
    def maquette(self):
        self.ui.stackedWidget_5.setCurrentIndex(2)
        self.ui.astuce_M.setStyleSheet("border-bottom-color:rgb(255, 85, 0)")
        self.ui.autre.setStyleSheet("")
        self.ui.astuce_P.setStyleSheet("")
        self.ui.astuce_M.setStyleSheet("border-bottom-color:rgb(255, 85, 0)")

    def astuce(self):
         self.ui.stackedWidget.setCurrentIndex(5)
         #aniEdit = AnimationShadowEffect(QColor("#ffaa00"),self.ui.groupBox_2)
         #self.ui.groupBox_2.setGraphicsEffect(aniEdit)
         #aniEdit.start()

    def astuce_Miage(self):
         self.ui.astuce_M.setStyleSheet("border-bottom-color:rgb(255, 85, 0)")
         self.ui.autre.setStyleSheet("")
         self.ui.astuce_P.setStyleSheet("")
         self.ui.stackedWidget_5.setCurrentIndex(0)

    def astuce_Prog(self):
         self.ui.astuce_P.setStyleSheet("border-bottom-color:rgb(255, 85, 0)")
         self.ui.autre.setStyleSheet("")
         self.ui.astuce_M.setStyleSheet("")
         self.ui.stackedWidget_5.setCurrentIndex(3)

    def pdf(self):
         self.ui.astuce_P.setStyleSheet("border-bottom-color:rgb(255, 85, 0)")
         self.ui.autre.setStyleSheet("")
         self.ui.astuce_M.setStyleSheet("")
         self.ui.stackedWidget_5.setCurrentIndex(6)

    def autre_astuce(self):
         self.ui.autre.setStyleSheet("border-bottom-color:rgb(255, 85, 0)")
         self.ui.astuce_M.setStyleSheet("")
         self.ui.astuce_P.setStyleSheet("")
         self.ui.stackedWidget_5.setCurrentIndex(5)

    def enregistrer(self):
        try:
            nom=self.ui.nom.text() ; prenom=self.ui.prenom.text()
            age=self.ui.age.text() ; niveau=self.ui.niveau.text()
            email=self.ui.email.text() ; langage=self.ui.langage_pre.currentText()
            matiere=self.ui.matiere.text()
            if self.fileName!=None : foto=self.fileName
            else : foto="fichiers\\info"
            with open(r"fichiers\info","w") as f: f.write(str({nom:[prenom,age,niveau,email,langage,matiere,foto]}))
        except:
            QMessageBox.information(self,"erreur","une erreur est survenue !")
        else:
            QMessageBox.information(self,"succes","operation effectuer avec succes !")

    def ajoutfoto(self,fileName=None):
        "pour changer la foto de profil"
        self.fileName=fileName

        if self.fileName==None or self.fileName==False :
            ACCEPT_TYPE = ("Images") + "(*.png *.jpg *.jpeg *.bmp *.gif)"
            self.fileName, _=QFileDialog.getOpenFileName(self.ui.label_foto,"choisi une image...",filter=ACCEPT_TYPE)
            if self.fileName:
                pixmap = QtGui.QPixmap(self.fileName)
                self.ui.label_foto.setPixmap(pixmap)
                self.ui.label_foto.setScaledContents(True)
        else:

            pixmap = QtGui.QPixmap(self.fileName)
            self.ui.label_foto.setPixmap(pixmap)
            self.ui.label_foto.setScaledContents(True)

    def apparait(self):
        if self.magimagi==0:
            self.anim = QPropertyAnimation(self.ui.doc2, b"geometry")
            self.anim.setDuration(700)
            self.anim.setStartValue(QRect(0, 0, 10, 591))
            self.anim.setEndValue(QRect(0, 0, 91, 591))
            self.anim.start()
            self.magimagi=1

    def fermer(self):
        if self.magimagi==1:
            self.anim = QPropertyAnimation(self.ui.doc2, b"geometry")
            self.anim.setDuration(400)
            self.anim.setStartValue(QRect(0, 0, 91, 591))
            self.anim.setEndValue(QRect(-20, 0, 16, 591))
            self.anim.start()
            self.magimagi=0

    def elargissement(self):
        "cette fonction permet de faire une animation : elargissement"
        #self.ui.btn_elargie.setEnabled(False)
        #self.ui.pushButton_63.setEnabled(False)
        self.ui.cache.show()
        self.anim = QPropertyAnimation(self.ui.doc1, b"geometry")
        self.anim.setDuration(800)
        self.anim.setStartValue(QRect(0, 0, 71, 591))
        self.anim.setEndValue(QRect(0, 0, 241, 591))
        self.anim.start()

        self.anim2 = QPropertyAnimation(self.ui.fond1, b"geometry")
        self.anim2.setDuration(800)
        self.anim2.setStartValue(QRect(140, 20, 641, 381))
        self.anim2.setEndValue(QRect(240, 20, 591, 381))
        self.anim2.start()

        self.anim3 = QPropertyAnimation(self.ui.groupBox, b"geometry")
        self.anim3.setDuration(800)
        self.anim3.setStartValue(QRect(180, 430, 561, 121))
        self.anim3.setEndValue(QRect(254, 430, 561, 121))
        self.anim3.start()

    def retressir(self):
        "cette fonction permet de faire une animation : retressissement"
        self.ui.cache.hide()
        self.anim = QPropertyAnimation(self.ui.doc1, b"geometry")
        self.anim.setDuration(800)
        self.anim.setStartValue(QRect(0, 0, 241, 591))
        self.anim.setEndValue(QRect(0, 0, 71, 591))
        self.anim.start()

        self.anim2 = QPropertyAnimation(self.ui.fond1, b"geometry")
        self.anim2.setDuration(800)
        self.anim2.setStartValue(QRect(240, 20, 591, 381))
        self.anim2.setEndValue(QRect(140, 20, 641, 381))
        self.anim2.start()

        self.anim3 = QPropertyAnimation(self.ui.groupBox, b"geometry")
        self.anim3.setDuration(800)
        self.anim3.setStartValue(QRect(254, 430, 561, 121))
        self.anim3.setEndValue(QRect(180, 430, 561, 121))
        self.anim3.start()

    def redimensionner(self):
        "cette fonction permet de faire une animation en redimensionent l'editeur de code"
        if self.verif==1:
            self.anim = QPropertyAnimation(self.ui.toolBox, b"geometry")
            self.anim.setDuration(400)
            self.anim.setStartValue(QRect(1, 0, 191, 511))
            self.anim.setEndValue(QRect(1, 0, 51, 511))
            self.anim.start()
            self.anim2 = QPropertyAnimation(self.ui.texte_code, b"geometry")
            self.anim2.setDuration(400)
            self.anim2.setStartValue(QRect(200, 0, 551, 511))
            self.anim2.setEndValue(QRect(60, 0, 691, 511))
            self.anim2.start()
            self.verif=0
        elif self.verif==0:
            self.anim = QPropertyAnimation(self.ui.toolBox, b"geometry")
            self.anim.setDuration(400)
            self.anim.setStartValue(QRect(1, 0, 51, 511))
            self.anim.setEndValue(QRect(1, 0, 191, 511))
            self.anim.start()
            self.anim2 = QPropertyAnimation(self.ui.texte_code, b"geometry")
            self.anim2.setDuration(400)
            self.anim2.setStartValue(QRect(60, 0, 691, 511))
            self.anim2.setEndValue(QRect(200, 0, 551, 511))
            self.anim2.start()
            self.verif=1

    def createActions(self):
        "cette fonction permet de creer des actions pour le menu bar"

        self.gran =QAction("&Redimensionner l'editeur", self,triggered= self.redimensionner)
        self.vider = QAction("&Vider l'editeur", self, triggered= lambda : self.ui.texte_code.setText(""))
        self.quit = QAction(QIcon('images/exit-icon.png'),"&Quitter", self, shortcut="Ctrl+Q",
                 triggered=QApplication.instance().closeAllWindows)
        self.home = QAction("&Accueil", self,shortcut="Ctrl+H",triggered= lambda : self.ui.stackedWidget.setCurrentIndex(0))

        self.langue=QAction("&Français", self)
        self.para = QAction("&Parametre", self,shortcut="Ctrl+P",
                triggered= lambda : self.ui.stackedWidget.setCurrentIndex(3))
        self.bug = QAction("&Signaler un bug", self,triggered=  lambda : os.startfile("Dialog_signalBug.pyw"))

        self.aid=QAction("&Aide", self,shortcut="Ctrl+A",
                triggered= lambda : QMessageBox.information(self,"aide","si vous avez besoin d'aide \nveillez entrez en contact avec nucleus"))
        self.apropoA=QAction(QIcon('images/about-icon.png'),"&Apropos de codeur.mi", self,
                triggered=self.apropos)
        self.apropos=QAction(QIcon('images/about-icon.png'),"&Apropos de l'auteur", self,
        triggered= lambda : QMessageBox.information(self,"apropos de ","""Apropos de l'auteur\nJe suis Emmanuel Malan alias Sminth
            Etudiant en licence 2 MIAGE, je suis l'auteur de ce logiciel,\nJ'aime l'informatique, la lecture ....
            Contact:88 36 44 03\nEmail : emmanuelmalan225@gmail.com"""))
    
    def apropos(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.stackedWidget_3.setCurrentIndex(4)
    
    def createMenus(self):
        "cette fonction permet d'ajouter des menus au menu bar et d'attribuer des actions"
        self.fichier = self.menuBar().addMenu("&Fichier(F)")

        self.fichier.addAction(self.home)
        self.fichier.addAction(self.quit)

        self.menuBar().addSeparator()

        self.outils = self.menuBar().addMenu("&Outils(O)")
        self.lang = self.outils.addMenu("&Language")
        self.lang.addAction(self.langue)
        self.outils.addAction(self.vider)
        self.outils.addAction(self.gran)
        self.outils.addAction(self.para)

        self.menuBar().addSeparator()

        self.aide = self.menuBar().addMenu("&Aide(A)")
        self.aide.addAction(self.aid)
        self.aide.addAction(self.bug)
        self.aide.addAction(self.apropos)
        self.aide.addAction(self.apropoA)

#programme Principale
if __name__ == "__main__":
  import sys,os
  app = QtWidgets.QApplication(sys.argv)
  ui = main()
  ui.show()     #lancement de l'application
  sys.exit(app.exec_())
