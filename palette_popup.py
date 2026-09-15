from PyQt5.QtWidgets import QWidget, QHBoxLayout,QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QGuiApplication, QColor
from palette import (primary_colors, secondary_colors, other_colors)
class PalettePopup(QWidget):

    def __init__(self, penguin, overlay):
        super().__init__(penguin)

        self.overlay = overlay

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.create_palette()

        self.hide()

    def create_palette(self):

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10,10,10,10)
        main_layout.setSpacing(8)

        #primary colors
        primary_label = QLabel("Primary")
        primary_label.setStyleSheet(
            "color:white; font-weight:bold;"
        )

        main_layout.addWidget(primary_label)
        primary_layout = QHBoxLayout()
        primary_layout.setSpacing(8)

        for color in primary_colors:
            self.add_color_button(primary_layout, color)

        main_layout.addLayout(primary_layout)

        #secondary colors
        secondary_label = QLabel("Secondary")
        secondary_label.setStyleSheet(
            "color: white; font-weight:bold;"
        )

        main_layout.addWidget(secondary_label)
        secondary_layout = QHBoxLayout()
        secondary_layout.setSpacing(8)

        for color in secondary_colors:
            self.add_color_button(secondary_layout, color)

        main_layout.addLayout(secondary_layout)

        #other colors
        other_label = QLabel("Other Colors")
        other_label.setStyleSheet(
            "color: white; font-weight:bold;"
        )

        main_layout.addWidget(other_label)
        other_layout = QHBoxLayout()
        other_layout.setSpacing(8)

        for color in other_colors:
            self.add_color_button(other_layout, color)

        main_layout.addLayout(other_layout)

        #save and close buttons + eraser button
        button_layout = QHBoxLayout()
        button_layout.setSpacing(8)

        save_btn=QPushButton("Save")
        eraser_btn = QPushButton("Eraser")
        close_btn=QPushButton("Close")

        save_btn.setFixedHeight(28)
        close_btn.setFixedHeight(28)

        save_btn.clicked.connect(self.save_drawing)
        eraser_btn.clicked.connect(self.toggle_eraser)
        close_btn.clicked.connect(self.close_drawing)

        save_btn.setStyleSheet("""
            QPushButton{
            background-color:rgba(255,255,255,0.4);
            border:none;
            border-radius:8px;
            padding: 4px 12px;
            }
            QPushButton:hover{
            background-color:#eeeeee;
            }
        """)
        close_btn.setStyleSheet("""
            QPushButton{
            background-color:rgba(255,255,255,0.4);
            border:none;
            border-radius:8px;
            padding: 4px 12px;
            }
            QPushButton:hover{
            background-color:#eeeeee;
            }
        """)

        button_layout.addWidget(save_btn)
        button_layout.addWidget(eraser_btn)
        button_layout.addWidget(close_btn)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        #color palette(popup)
        self.setStyleSheet("""
            QWidget{
            background-color: rgba(40,40,40,230);
            border:none;
            border-radius: 12px;
            }
            QPushButton{
            border: none;
            border-radius:8px;
            background-color: white;
            padding: 4px 12px;
            }
            QPushButton:hover{
            background-color:#eeeeee;
            }
        """)

        self.adjustSize()

    def add_color_button(self,layout,color):

        color_button = QPushButton()
        color_button.setFixedSize(30,30)
          
        color_button.setStyleSheet(
            f"""
            QPushButton{{
            background-color:{color}; 
            border:none; 
            border-radius:20px;
            }}
            QPushButton:hover {{
            border:2px solid white;
            }}
            """
        )
        
        # to make each button remember its own color
        color_button.clicked.connect(
        lambda checked, c=color: self.copy_color(c)
        )

        layout.addWidget(color_button)

    def copy_color(self, color):
        QGuiApplication.clipboard().setText(color)

        # print("COLOR CLICKED:", color)

        self.overlay.color = QColor(color)

        self.overlay.show()
        self.hide()

    def save_drawing(self):
        self.overlay.save_drawing()

    def close_drawing(self):
        self.overlay.hide()
        self.hide()

    def toggle_eraser(self):
        self.overlay.eraser = not self.overlay.eraser

        if self.overlay.eraser:
            print("Eraser On")
        else:
            print("Eraser OFF")

