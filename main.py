import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

penguin =QLabel()

image = QPixmap("assets/Penguin-default.png")
penguin.setPixmap(image)

penguin.setWindowFlags(
    Qt.FramelessWindowHint |
    Qt.WindowStaysOnTopHint |
    Qt.Tool
)

penguin.setAttribute(Qt.WA_TranslucentBackground)

penguin.show()

sys.exit(app.exec_())