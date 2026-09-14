from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QColor

class DrawingOverlay(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )

        # for transparent overlay
        self.setStyleSheet("background-color:white;")
        self.setWindowOpacity(0.15)
        

        self.last_position = None
        self.drawing = False

        self.color = QColor("red")
        self.brush_size=10
        self.strokes = []

        #to draw on whole screen
        screen = self.screen().geometry()
        self.setGeometry(screen)

        self.hide()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:

            # print("mouse pressed on overlay")

            self.drawing = True
            self.last_position = event.pos()

    def mouseMoveEvent(self, event):
        if self.drawing:

            # print("drawing")
            
            self.strokes.append(
                (
                    self.last_position,
                    event.pos(),
                )
            )

            self.last_position = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False
            self.last_position = None

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)

        pen = QPen(
            self.color,
            self.brush_size,
            Qt.SolidLine,
            Qt.RoundCap,
            Qt.RoundJoin
        )
        painter.setPen(pen)

        for start, end in self.strokes:
            painter.drawLine(start,end)    

        painter.end()


