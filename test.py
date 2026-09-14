import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen

class Test(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowFlags(
             Qt.FramelessWindowHint |
             Qt.WindowStaysOnTopHint |
             Qt.Tool
        )

        self.setAttribute(Qt.WA_TranslucentBackground, True)

        print("Translucent:", self.testAttribute(Qt.WA_TranslucentBackground))

        screen = self.screen().geometry()
        self.setGeometry(screen)

        self.show()

    def paintEvent(self, event):
        painter =QPainter(self)
        pen = QPen(Qt.red, 10)
        painter.setPen(pen)
        painter.drawLine(200,200,500,400)
        painter.end()

app = QApplication(sys.argv)
window = Test()
sys.exit(app.exec_())