import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from show_map import show_map
from PyQt5.QtGui import QPixmap

class Map(QWidget):
    def __init__(self):
        super().__init__()
        self.lat = 51.119461
        self.lon = 71.431741
        self.spn = 0.01
        self.mode = "sat"
        self.create_map()
        self.initUI()


    def initUI(self):
        self.setGeometry(300, 300, 700, 700)
        self.setWindowTitle('Координаты')
        self.pixmap = QPixmap('map.png')
        self.map = QLabel(self)
        self.map.setPixmap(self.pixmap)
        self.map.resize(700, 700)
        self.map.move(0, 0)
        self.coords = QLabel(self)
        self.coords.setText("Координаты: None, None")
        self.coords.move(0, 0)

    def update(self):
        pass

    def create_map(self):
        ll_spn = f"ll={self.lon},{self.lat}&spn={self.spn},{self.spn}"
        show_map(ll_spn, map_type=self.mode)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Map()
    ex.show()
    sys.exit(app.exec())