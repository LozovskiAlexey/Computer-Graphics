from PyQt5.QtCore import QPoint, QSize, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class CircleCanvas(QWidget):
    # класс для отрисовки одного отрезка

    def __init__(self):
        super().__init__()

        self.figure = None  # для класса фигуры

        self.pixmap = QPixmap(self.size()).scaled(700, 700, Qt.IgnoreAspectRatio)
        self.pixmap.fill(Qt.transparent)
        self.color = [255, 255, 255]

    def minimumSizeHint(self):
        return QSize(687, 689)

    def sizeHint(self):
        return QSize(687, 689)

    def clear(self):
        self.pixmap = QPixmap(self.size())
        self.pixmap.fill(Qt.transparent)
        self.update()

    def myDrawCircle(self):
        painter = QPainter(self.pixmap)

        if self.figure is not None:
            # отрисовка
            color = QColor(self.color[0], self.color[1], self.color[2])
            painter.translate(self.width() / 2, self.height() / 2)
            painter.setPen(color)

            alg = self.figure.alg
            self.figure.draw[alg](painter)  # отрисовка фигуры

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(QPoint(), self.pixmap)


class CircleCmp(CircleCanvas):
    # класс для отрисовки узла отрезков

    def __init__(self):
        super().__init__()

    def myDrawCircle(self):
        painter = QPainter(self.pixmap)

        if self.figure is not None:
            # отрисовка
            color = QColor(self.color[0], self.color[1], self.color[2])
            painter.translate(self.width() / 2, self.height() / 2)
            painter.setPen(color)

            # отрисовка окружности и эллипса

            self.figure.cmpCircle(painter)

        self.update()
