from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

import sys

class SimpleDrawingWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)


    def paintEvent(self, e):
        self.drawKaowphod(e)
        self.drawTada(e)

    def drawTada(self, e):
        pass

    def drawKaowphod(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 25, 51))
        p.setBrush(QColor(0, 25, 51))
        p.drawRect(0, 0, 50, 50)

        p.end()

def main():
    app = QApplication(sys.argv)

    w = SimpleDrawingWindow()
    w.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())