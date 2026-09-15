import sys
import os
from PyQt5.QtWidgets import QApplication, QLabel, QMenu
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
from palette_popup import PalettePopup
from drawing_overlay import DrawingOverlay

def asset_path(filename):
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, "assets", filename)
class SpeechBubble(QLabel):
    def __init__ (self):
        super().__init__()

        self.cloud_image = QPixmap(asset_path("message.png"))

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.Tool |
            Qt.WindowStaysOnTopHint
        )

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.quote_label = QLabel(self)

        self.quote_label.setStyleSheet("""
        QLabel {
        color: black;
        font-size:14px;
        font-weight: bold;
        background: transparent;
        }
        """)

        self.hide()

    def show_quote(self, quote):
        self.setPixmap(self.cloud_image)
        self.adjustSize()

        self.quote_label.setText(quote)
        self.quote_label.adjustSize()

        x = (self.width() - self.quote_label.width()) // 2
        y = (self.height() - self.quote_label.height()) -85

        self.quote_label.move(x,y)

        self.show()
        self.raise_()

        QTimer.singleShot(1800, self.hide)
class Penguin(QLabel):
    def __init__(self, overlay):
        super().__init__()
        self.overlay = overlay

        self.normal_image = QPixmap(asset_path("Penguin.png"))
        self.palette_image =QPixmap(asset_path("Penguin-paints.png"))

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
        self.speech_bubble = SpeechBubble()

        self.palette_popup = PalettePopup(self, self.overlay)

        self.hide_timer = QTimer()
        self.hide_timer.setSingleShot(True)
        self.hide_timer.timeout.connect(self.palette_popup.hide)

        self.quotes = {
            "Penguin":"Ready to make \n something nice?!",
            "Brown Bear":"Alright. \nLet's make art.",
            "White Rabbit":"Ready?Let's hop\n right into it.",
            "Black Rabbit":"Let's make something\n worth hiding",
            "White Owl":"Hmm..\nLet me see \nwhat you create.",
            "Black Owl":"Make art \nright now!",
            "Fox":"Hehe, Do you like \nFishy arts?!",
            "Dog":"Yay! Let's make \nsomething together!",
            "Cat":"Alright, show me \nwhat you got.",
            "Panda":"Relax. Let's make\n something chill."
        }

    def show_normal_penguin(self):
        self.setPixmap(self.normal_image)
        self.adjustSize()

    def show_palette_penguin(self):
        self.setPixmap(self.palette_image)
        self.adjustSize()

    def change_animal(self,animal):
        self.current_animal=animal

        if animal == "Penguin":
            self.normal_image = QPixmap(asset_path("Penguin.png"))
            self.palette_image = QPixmap(asset_path("Penguin-paints.png"))
        elif animal == "Brown Bear":
            self.normal_image = QPixmap(asset_path("bear.png"))
            self.palette_image = QPixmap(asset_path("bear-paints.png"))
        elif animal == "White Rabbit":
            self.normal_image = QPixmap(asset_path("white-rabbit.png"))
            self.palette_image = QPixmap(asset_path("white-rabbit-paints1.png"))
        elif animal == "Black Rabbit":
            self.normal_image = QPixmap(asset_path("Black-rabbit.png"))
            self.palette_image = QPixmap(asset_path("Black-rabbit-paints1.png"))
        elif animal == "White Owl":
            self.normal_image = QPixmap(asset_path("White-owl.png"))
            self.palette_image = QPixmap(asset_path("White-owl-paints.png"))
        elif animal == "Black Owl":
            self.normal_image = QPixmap(asset_path("Black-owl.png"))
            self.palette_image = QPixmap(asset_path("Black-owl-paints.png"))
        elif animal == "Fox":
            self.normal_image = QPixmap(asset_path("fox.png"))
            self.palette_image = QPixmap(asset_path("fox-paints.png"))
        elif animal == "Dog":
            self.normal_image = QPixmap(asset_path("dog.png"))
            self.palette_image = QPixmap(asset_path("dog-paints.png"))
        elif animal == "Cat":
            self.normal_image = QPixmap(asset_path("cat.png"))
            self.palette_image = QPixmap(asset_path("cat-paints.png"))
        elif animal == "Panda":
            self.normal_image = QPixmap(asset_path("panda.png"))
            self.palette_image = QPixmap(asset_path("panda-paints.png"))


        self.show_normal_penguin()
        self.palette_mode = False
        self.show_animal_quote()

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
        white_rabbit_action = menu.addAction("White Rabbit")
        black_rabbit_action = menu.addAction("Black Rabbit")
        white_owl_action = menu.addAction("White Owl")
        black_owl_action = menu.addAction("Black Owl")
        fox_action = menu.addAction("Fox")
        dog_action = menu.addAction("Dog")
        cat_action = menu.addAction("Cat")
        panda_action = menu.addAction("Panda")

        menu.addSeparator()
        quit_action = menu.addAction("Quit Extension")

        selected_action = menu.exec_(event.globalPos())

        if selected_action == penguin_action:
            self.change_animal("Penguin")
        elif selected_action == bear_action:
            self.change_animal("Brown Bear")
        elif selected_action == white_rabbit_action:
            self.change_animal("White Rabbit")
        elif selected_action == black_rabbit_action:
            self.change_animal("Black Rabbit")
        elif selected_action == white_owl_action:
            self.change_animal("White Owl")
        elif selected_action == black_owl_action:
            self.change_animal("Black Owl")
        elif selected_action == fox_action:
            self.change_animal("Fox")
        elif selected_action == dog_action:
            self.change_animal("Dog")
        elif selected_action == cat_action:
            self.change_animal("Cat")
        elif selected_action == panda_action:
            self.change_animal("Panda")
        elif selected_action == quit_action:
            QApplication.quit()

        event.accept()

    def show_animal_quote(self):
        quote = self.quotes[self.current_animal]

        self.speech_bubble.show_quote(quote)
        self.speech_bubble.move(
            self.x() - self.width() - 80,
            self.y() - self.speech_bubble.height() //3
        )
        
    
app = QApplication(sys.argv)

overlay = DrawingOverlay()

penguin = Penguin(overlay)
penguin.show()
penguin.raise_()

sys.exit(app.exec_())