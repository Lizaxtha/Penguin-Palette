from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QImage

class DrawingOverlay(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.Tool
        )

        # for transparent overlay
        self.setStyleSheet("background-color:white;")
        self.setWindowOpacity(0.15)
        
        self.last_position = None
        self.drawing = False

        self.color = None
        self.brush_size=10
        self.eraser = False

        #to draw on whole screen
        screen = self.screen().geometry()
        self.setGeometry(screen)

        self.canvas = QImage(
            self.size(),
            QImage.Format_ARGB32
        )
        self.canvas.fill(Qt.transparent)

        self.hide()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_position = event.pos()

    def mouseMoveEvent(self, event):

        if self.drawing:
            painter = QPainter(self.canvas)
            painter.setRenderHint(QPainter.Antialiasing)

        if self.eraser:
            painter.setCompositionMode(
                QPainter.CompositionMode_Clear
            )

        else:
            painter.setCompositionMode(
                QPainter.CompositionMode_SourceOver
            )

        painter.setPen(
            QPen(
                self.color,
                self.brush_size,
                Qt.SolidLine,
                Qt.RoundCap,
                Qt.RoundJoin
            )
        )

        painter.drawLine(
            self.last_position,
            event.pos()
        )

        painter.end()
        self.last_position = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False
            self.last_position = None

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.drawImage(
            0,0,self.canvas
        )

        painter.end()

    def save_drawing(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Drawing",
            "My art.png",
            "PNG Images (*.png)"
        )

        if file_path:
            self.canvas.save(file_path)
            print("Drawing Saved!")

    def clear_drawing(self):
        self.canvas.fill(Qt.transparent)
        self.update()
