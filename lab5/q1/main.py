from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

import sys

class SimpleDrawingWindow(QWidget):
    def __init__(self):
        pass

    def paintEvent(self, e):
        self.drawKaowphod(e)
        self.drawTada(e)

    def drawTada(self, e):
        pass

    def drawKaowphod(self, e):
        pass


def main():
    app = QApplication(sys.argv)

    w = SimpleDrawingWindow()
    w.show()

    return app.exec()