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

           self.drag_position = event.globalPos()
           

           self.show_palette_penguin()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:

            self.move(
                event.globalPos() - self.drag_position
            )

    def mouseReleaseEvent(self, event):
        self.drag_position = None
    
app = QApplication(sys.argv)

penguin = Penguin()
penguin.show()

sys.exit(app.exec_())