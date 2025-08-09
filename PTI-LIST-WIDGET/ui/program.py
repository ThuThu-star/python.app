from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic
import sys
import json

class AnimeItem(QWidget):   
    def __init__(self, anime:dict):
        super().__init__()
        uic.loadUi("ui/item.ui", self)
        self.setFixedSize(800, 100)

        self.anime = anime
        self.init_ui()


    def init_ui(self):
        self.lb_name = self.findChild(QLabel, "lb_name")
        self.lb_rating = self.findChild(QLabel, "lb_rating")
        self.lb_name.setText(self.anime["name"])
        self.lb_rating.setText(str(self.anime["rating"]))
    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/list.ui", self)
        self.init_ui()

    def init_ui(self):
        self.list_widget = self.findChild(QListWidget, "list_widget")

        data = self.load_json()
        for item in data:
            anime_item = AnimeItem(item)

            list_item = QListWidgetItem(self.list_widget)
            list_item.setSizeHint(QSize(800, 100))

    def load_json(self):
        with open("data/anime.json", "r") as f:
            data = json.load(f)
        return data
    

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())