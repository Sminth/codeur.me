from PyQt5.QtCore import QFile, QRegExp, Qt
from PyQt5.QtGui import QFont, QSyntaxHighlighter, QTextCharFormat
from PyQt5.QtWidgets import (QApplication, QFileDialog, QMainWindow, QMenu,
        QMessageBox, QTextEdit)
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class Highlighter_algo(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(Highlighter_algo, self).__init__(parent)

        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(QColor(255, 0, 255))
        #keywordFormat.setFontWeight(QFont.Bold)

        keyword = QTextCharFormat()
        keyword.setForeground(QColor(255, 170, 0))

        keywordPatterns = ["\\bDEBUT\\b", "\\bFIN\\b", "\\bFONCTION\\b",
                  "\\bSI\\b", "\\bSINON\\b", "\\bTANTQUE\\b","\\bRETOURNE\\b","\\bPOUR\\b","\\FAIRE\\b","\\bSAISIR\\b","\\bVARIABLE\\b","\\bPROCEDURE\\b"]

        autres = ["\\bENTIER\\b", "\\bREEL\\b", "\\bCHAINE\\b","\\bstring\\b",
                  "\\bvoid\\b"]

        self.highlightingRules = [(QRegExp(pattern), keywordFormat)
                for pattern in keywordPatterns]
        self.highlightingRules=self.highlightingRules+[(QRegExp(pattern), keyword) for pattern in autres]


        classFormat = QTextCharFormat()
        classFormat.setFontWeight(QFont.Bold)
        classFormat.setForeground(Qt.darkMagenta)
        self.highlightingRules.append((QRegExp("\\bQ[A-Za-z]+\\b"),
                classFormat))

        singleLineCommentFormat = QTextCharFormat()
        singleLineCommentFormat.setForeground(Qt.darkGreen)
        self.highlightingRules.append((QRegExp("//[^\n]*"),
                singleLineCommentFormat))

        self.multiLineCommentFormat = QTextCharFormat()
        self.multiLineCommentFormat.setForeground(QColor(0, 255, 255))

        quotationFormat = QTextCharFormat()
        quotationFormat.setForeground(Qt.green)
        self.highlightingRules.append((QRegExp("\".*\""), quotationFormat))

        simplequotationFormat = QTextCharFormat()
        simplequotationFormat.setForeground(Qt.darkGreen)
        #self.highlightingRules.append((QRegExp("'.*'"), simplequotationFormat))

        fleche = QTextCharFormat()
        fleche.setFontItalic(False)
        fleche.setForeground(QColor(255, 170, 0))
        self.highlightingRules.append((QRegExp("\\<\\-\\-"),fleche))

        afficher = QTextCharFormat()
        afficher.setFontItalic(False)
        afficher.setForeground(Qt.blue)
        self.highlightingRules.append((QRegExp("\\bAFFICER\\b"),afficher))


        self.commentStartExpression = QRegExp("\\(\\*")
        self.commentEndExpression = QRegExp("\\*\\)")


    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = self.commentStartExpression.indexIn(text)

        while startIndex >= 0:
            endIndex = self.commentEndExpression.indexIn(text, startIndex)

            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = len(text) - startIndex
            else:
                commentLength = endIndex - startIndex + self.commentEndExpression.matchedLength()

            self.setFormat(startIndex, commentLength,
                    self.multiLineCommentFormat)
            startIndex = self.commentStartExpression.indexIn(text,
                    startIndex + commentLength)
