from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

import sys

class SimpleDrawingWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.johnny_depp = QPixmap("images/johnny_depp.jpg")

    def paintEvent(self, e):
        self.drawKaowphod(e)
        self.drawTada(e)

    def drawTada(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))

        p.drawPixmap(QRect(300, 0, 200, 200), self.johnny_depp)
        p.drawPie(300, 0, 100, 100, 0, 180 * 16)
        p.end()


    def drawKaowphod(self, e):
        pass


def main():
    app = QApplication(sys.argv)

    w = SimpleDrawingWindow()
    w.show()

    return app.exec()

if __name__ == "__main__":
    main()