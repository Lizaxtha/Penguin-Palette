import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
from palette_popup import PalettePopup
from drawing_overlay import DrawingOverlay
class Penguin(QLabel):
    def __init__(self, overlay):
        super().__init__()
        self.overlay = overlay

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
        self.is_dragging=False
        self.palette_mode = False

        self.palette_popup = PalettePopup(self, self.overlay)

        self.hide_timer = QTimer()
        self.hide_timer.setSingleShot(True)
        self.hide_timer.timeout.connect(self.palette_popup.hide)


    def show_normal_penguin(self):
        self.setPixmap(self.normal_image)
        self.adjustSize()

    def show_palette_penguin(self):
        self.setPixmap(self.palette_image)
        self.adjustSize()

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
                self.palette_mode = True

            self.is_dragging = False

    def enterEvent(self, event):
        if self.palette_mode:
            self.hide_timer.stop()

            self.palette_popup.move(
                self.x() + self.width() + 10,
                self.y()
            )
            self.palette_popup.show()

    def leaveEvent(self, event):
        if self.palette_mode:
            self.hide_timer.start(1500)
    
app = QApplication(sys.argv)

overlay = DrawingOverlay()

penguin = Penguin(overlay)
penguin.show()

sys.exit(app.exec_())