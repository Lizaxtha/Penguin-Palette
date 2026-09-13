import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from palette import generate_palette

print(generate_palette())

class Penguin(QLabel):
    def __init__(self):
        super().__init__()

        self.normal_image = QPixmap("assets/Penguin-default.png")
        self.palette_image =QPixmap("assets/Penguin-paints.png")

        self.drag_position = None

        self.show_normal_penguin()

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.drag_position=None
        self.is_dragging=False

    def show_normal_penguin(self):
        self.setPixmap(self.normal_image)
        self.adjustSize()

    def show_palette_penguin(self):
        self.setPixmap(self.palette_image)
        self.adjustSize()

# "use it later to center all images if not centered"
        # center =  self.geometry().center()  
        # self.move(
            # center.x() - self.width // 2,
            # center.y() - self.height //2
        # )

    def mousePressEvent(self, event):
       if event.button() == Qt.LeftButton:

           self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
           self.is_dragging = False

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.is_dragging = True
            self.move(
                event.globalPos()-self.drag_position
            )

    def mouseReleaseEvent(self, event):
        if event.button()==Qt.LeftButton:
            if not self.is_dragging:
                self.show_palette_penguin()
            self.is_dragging = False
    
app = QApplication(sys.argv)

penguin = Penguin()
penguin.show()

sys.exit(app.exec_())