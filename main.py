import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMenu
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

        self.current_animal = "Penguin"

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

    def change_animal(self,animal):
        self.current_animal=animal

        if animal == "Penguin":
            self.normal_image = QPixmap("assets/Penguin-default")
            self.palette_image = QPixmap("assets/Penguin-paints.png")
        elif animal == "Brown Bear":
            self.normal_image = QPixmap("assets/bear-default")
            self.palette_image = QPixmap("assets/bear-paints.png")
        elif animal == "White Rabbit":
            self.normal_image = QPixmap("assets/white-rabbit-default")
            self.palette_image = QPixmap("assets/white-rabbit-paints.png")
        elif animal == "Black Rabbit":
            self.normal_image = QPixmap("assets/Black-rabbit-default")
            self.palette_image = QPixmap("assets/Black-rabbit-paints.png")
        elif animal == "White Owl":
            self.normal_image = QPixmap("assets/White-owl-default")
            self.palette_image = QPixmap("assets/White-owl-paints.png")
        elif animal == "Black Owl":
            self.normal_image = QPixmap("assets/Black-owl-default")
            self.palette_image = QPixmap("assets/Black-owl-paints.png")
        elif animal == "Fox":
            self.normal_image = QPixmap("assets/fox-default")
            self.palette_image = QPixmap("assets/fox-paints.png")

        self.show_normal_penguin()
        self.palette_mode = False

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

    def contextMenuEvent(self,event):

        #changes penguin-paints to default penguin
        if self.palette_mode:
            self.show_normal_penguin()
            self.palette_mode = False
            self.palette_popup.hide()

            event.accept()
            return

        # default penguin to animal menu
        menu = QMenu(self)

        penguin_action = menu.addAction("Penguin")
        bear_action = menu.addAction("Brown Bear")
        W_rabbit_action = menu.addAction("White Rabbit")
        B_rabbit_action = menu.addAction("Black Rabbit")
        W_owl_action = menu.addAction("White Owl")
        B_owl_action = menu.addAction("Black Owl")
        fox_action = menu.addAction("Fox")

        selected_action = menu.exec_(event.globalPos())

        if selected_action == penguin_action:
            self.change_animal("Penguin")
        elif selected_action == bear_action:
            self.change_animal("Brown Bear")
        elif selected_action == W_rabbit_action:
            self.change_animal("White Rabbit")
        elif selected_action == B_rabbit_action:
            self.change_animal("Black Rabbit")
        elif selected_action == W_owl_action:
            self.change_animal("White Owl")
        elif selected_action == B_owl_action:
            self.change_animal("Black Owl")
        elif selected_action == fox_action:
            self.change_animal("Fox")

        event.accept()
        
    
app = QApplication(sys.argv)

overlay = DrawingOverlay()

penguin = Penguin(overlay)
penguin.show()
penguin.raise_()

sys.exit(app.exec_())