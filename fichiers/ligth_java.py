from PyQt5.QtCore import QFile, QRegExp, Qt
from PyQt5.QtGui import QFont, QSyntaxHighlighter, QTextCharFormat
from PyQt5.QtWidgets import (QApplication, QFileDialog, QMainWindow, QMenu,
        QMessageBox, QTextEdit)
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class Highlighter_java(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(Highlighter_java, self).__init__(parent)

        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(QColor(255, 0, 255))
        #keywordFormat.setFontWeight(QFont.Bold)

        keyword = QTextCharFormat()
        keyword.setForeground(QColor(255, 170, 0))

        keywordPatterns = ["\\bpublic\\b", "\\bclass\\b", "\\bstatic\\b",
                "\\bpackage\\b", "\\bif\\b", "\\belse\\b", "\\breturn\\b","\\bwhile\\b","\\bfor\\b","\\breturn\\b"]

        autres = ["\\bint\\b", "\\blong\\b", "\\bfloat\\b", "\\bchar\\b","\\bstring\\b",
                  "\\bString\\b","\\bvoid\\b","\\b[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?\\b"]

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

        functionFormat = QTextCharFormat()
        functionFormat.setFontItalic(True)
        functionFormat.setForeground(Qt.blue)
        self.highlightingRules.append((QRegExp("\\b[A-Za-z0-9_]+(?=\\()"),
                functionFormat))

        print = QTextCharFormat()
        print.setFontItalic(False)
        print.setForeground(Qt.blue)
        self.highlightingRules.append((QRegExp("\\bprintln\\b"),print))

        out = QTextCharFormat()
        out.setFontItalic(False)
        out.setForeground(Qt.red)
        self.highlightingRules.append((QRegExp("\\bSystem.out\\b"),out))

        self.commentStartExpression = QRegExp("/\\*")
        self.commentEndExpression = QRegExp("\\*/")

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
                    startIndex + commentLength);
