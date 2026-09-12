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

    def mousePressEvent(self, event):
       if event.button() == Qt.LeftButton:
           self.show_palette_penguin()
    
app = QApplication(sys.argv)

penguin = Penguin()
penguin.show()

sys.exit(app.exec_())