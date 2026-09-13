from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from palette import generate_palette

class PalettePopup(QWidget):

    def __init__(self, penguin):
        super().__init__(penguin)

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.create_palette()
        self.hide()

    def create_palette(self):
        colors = generate_palette()
        layout = QHBoxLayout()
        layout.setSpacing(8)

        for color in colors:
            color_button = QPushButton()
            color_button.setFixedSize(45,45)

            color_button.setStyleSheet(
                f"""
                QPushButton{{
                background-color:{color}; 
                border:none; 
                border-radius:22px;
                }}
                """
            )

            layout.addWidget(color_button)
        self.setLayout(layout)
        self.adjustSize()

    def enterEvent(self, event):
        self.parent().hide_timer.stop()

