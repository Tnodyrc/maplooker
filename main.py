import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from show_map import show_map
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Map(QWidget):
    def __init__(self):
        super().__init__()
        self.lat = 51.119461
        self.lon = 71.431741
        self.spn = 0.01          # default
        self.mode = "sat"
        self.create_map(new=True)
        self.initUI()


    def initUI(self):
        self.setGeometry(300, 300, 700, 700)
        self.setWindowTitle('Координаты')

        self.map = QLabel(self)
        self.map.setPixmap(self.pixmap)
        self.map.resize(700, 700)
        self.map.move(0, 0)
        self.coords = QLabel(self)
        self.coords.setText("Координаты: None, None")
        self.coords.move(0, 0)

    def keyPressEvent(self, event):
        print(1)
        print(self.spn)
        if event.key() == Qt.Key_PageUp:
            self.spn += self.spn / 8
            print(2)
            self.create_map()
        elif event.key() == Qt.Key_PageDown:
            self.spn -= self.spn / 8
            self.create_map()
        if self.spn > 0.05:
            self.spn = 0.05
        elif self.spn < 0.001:
            self.spn = 0.001



    def create_map(self, new = False):
        ll_spn = f"ll={self.lon},{self.lat}&spn={self.spn},{self.spn}"
        show_map(ll_spn, map_type=self.mode)
        self.pixmap = QPixmap('map.png')
        if not new:
            print(self.spn)
            self.map.setPixmap(self.pixmap)
            print(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Map()
    ex.show()
    sys.exit(app.exec())