from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

import sys

class SimpleDrawingWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
<<<<<<< Updated upstream


        self.johnny_depp = QPixmap("images/johnny_depp.jpg")
=======
>>>>>>> Stashed changes

    def paintEvent(self, e):
        self.drawKaowphod(e)
        self.drawTada(e)
        self.drawDiyaan(e)

    def drawTada(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))

        p.drawPixmap(QRect(300, 0, 200, 200), self.johnny_depp)
        p.drawPie(300, 0, 100, 100, 0, 180 * 16)
        p.end()


    def drawKaowphod(self, e):
        p = QPainter()
        p.begin(self)

<<<<<<< Updated upstream
        p.setPen(QColor(0, 25, 51))
        p.setBrush(QColor(0, 25, 51))
        p.drawRect(0, 0, 50, 50)

        p.end()
=======
    def drawDiyaan(self, e):
        p = QPainter()

        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(255, 165, 0))

        p.drawPolygon([
            QPoint(180, 120), QPoint(60, 80),
            QPoint(60, 110), QPoint(40, 20),
            QPoint(100, 200)
        ])
        p.end()

>>>>>>> Stashed changes

def main():
    app = QApplication(sys.argv)

    w = SimpleDrawingWindow()
    w.show()

    return app.exec()

<<<<<<< Updated upstream
if __name__ == "__main__":
    main()
=======
sys.exit(main())
>>>>>>> Stashed changes
