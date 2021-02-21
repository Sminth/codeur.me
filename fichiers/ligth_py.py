# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:07:06) [MSC v.1900 32 bit (Intel)]
# Embedded file name: C:\Users\utilisateur\Desktop\pfff\codeur\fichiers\ligth_py.py
# Compiled at: 2019-09-13 17:59:16
# Size of source mod 2**32: 3667 bytes
from PyQt5.QtCore import QFile, QRegExp, Qt
from PyQt5.QtGui import QFont, QSyntaxHighlighter, QTextCharFormat
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QMenu, QMessageBox, QTextEdit
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Highlighter_py(QSyntaxHighlighter):

    def __init__(self, parent=None):
        super(Highlighter_py, self).__init__(parent)
        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(QColor(255, 85, 0))
        keyword = QTextCharFormat()
        keyword.setForeground(QColor(255, 0, 255))
        keywordPatterns = [
         '\\bdef\\b', '\\bclass\\b', '\\bNone\\b',
         '\\bfor\\b', '\\bif\\b', '\\belse\\b', '\\belif\\b',
         '\\bin\\b', '\\bTrue\\b', '\\bFalse\\b',
         '\\bfrom\\b', '\\bimport\\b', '\\bwhile\\b', '\\breturn\\b']
        autres = [
         '\\bsuper\\b', '\\bprint\\b', '\\bint\\b', '\\bfloat\\b', '\\bstr\\b',
         '\\brange\\b', '\\blen\\b']
        self.highlightingRules = [(QRegExp(pattern), keywordFormat) for pattern in keywordPatterns]
        self.highlightingRules = self.highlightingRules + [(QRegExp(pattern), keyword) for pattern in autres]
        print('ok')
        classFormat = QTextCharFormat()
        classFormat.setFontWeight(QFont.Bold)
        classFormat.setForeground(Qt.darkMagenta)
        self.highlightingRules.append((QRegExp('\\bQ[A-Za-z]+\\b'), classFormat))
        singleLineCommentFormat = QTextCharFormat()
        singleLineCommentFormat.setForeground(Qt.red)
        self.highlightingRules.append((QRegExp('#[^\n]*'), singleLineCommentFormat))
        self.multiLineCommentFormat = QTextCharFormat()
        self.multiLineCommentFormat.setForeground(Qt.green)
        quotationFormat = QTextCharFormat()
        quotationFormat.setForeground(Qt.green)
        self.highlightingRules.append((QRegExp('".*"'), quotationFormat))
        functionFormat = QTextCharFormat()
        functionFormat.setFontItalic(True)
        functionFormat.setForeground(Qt.blue)
        self.highlightingRules.append((QRegExp('\\b[A-Za-z0-9_]+(?=\\()'), functionFormat))
        self.commentStartExpression = QRegExp('""".*[^\n]')
        self.commentEndExpression = QRegExp('.*[^\n]"""')

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
            self.setFormat(startIndex, commentLength, self.multiLineCommentFormat)
            startIndex = self.commentStartExpression.indexIn(text, startIndex + commentLength)