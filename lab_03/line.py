from math import cos, sin, radians
from PyQt5.QtCore import QPoint, QSize, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class LineCanvas(QWidget):
    # класс для отрисовки одного отрезка

    def __init__(self):
        super().__init__()

        self.start_point = None
        self.end_point = None

        self.pixmap = QPixmap(self.size()).scaled(625, 660, Qt.IgnoreAspectRatio)
        print(self.pixmap.size())
        self.pixmap.fill(Qt.transparent)

        self.draw = None  # переменная для алгоритма отрисовки
        self.color = [255, 255, 255]  # белый цвет по умолчанию

        self.check = None  # проверка была ли полностью отрисована фигура

    def minimumSizeHint(self):
        return QSize(593, 593)

    def sizeHint(self):
        return QSize(593, 593)

    def clear(self):
        self.pixmap = QPixmap(self.size())
        self.pixmap.fill(Qt.transparent)
        self.update()

    def myDrawLine(self):
        painter = QPainter(self.pixmap)

        if self.draw is not None:
            # отрисовка
            color = QColor(self.color[0], self.color[1], self.color[2])
            painter.translate(self.width() / 2, self.height() / 2)
            painter.setPen(color)

            self.check = self.draw(painter, self.start_point, self.end_point, color)
        self.draw = None

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(QPoint(), self.pixmap)


class LineCmp(LineCanvas):
    # класс для отрисовки узла отрезков

    def __init__(self):
        super().__init__()

        self.start_point = [0, 0]
        self.end_point = [250, 0]
        # self.fi = [30, 45, 60, 90]  # углы наклона
        self.step = 30

    def rotate(self, fi, point):
        x = point[0]
        y = point[1]

        x1 = x * cos(radians(fi)) - y * sin(radians(fi))
        y1 = x * sin(radians(fi)) + y * cos(radians(fi))

        return [int(x1), int(y1)]

    def myDrawLine(self):
        painter = QPainter(self.pixmap)

        if self.draw is not None:
            # отрисовка
            color = QColor(self.color[0], self.color[1], self.color[2])
            painter.translate(self.width() / 2, self.height() / 2)
            painter.setPen(color)

            fi = 0

            while fi <= 360:

                start_point = self.rotate(fi, self.start_point)
                end_point = self.rotate(fi, self.end_point)

                fi += int(self.step)

                self.draw(painter, start_point, end_point, color)

            self.draw = None
        self.update()
'''
===========================================================================
            for fi in self.fi:
                for i in range(4):

                    tmp_fi = fi + 90 * i
                    start_point = self.rotate(tmp_fi, self.start_point)
                    end_point = self.rotate(tmp_fi, self.end_point)

                    self.draw(painter, start_point, end_point, color)

            self.draw = None
        self.update()
        
==========================================================================
            # нарисует цветок
            for fi in range(360):
                start_point = self.rotate(fi, self.start_point)
                end_point = self.rotate(fi, self.end_point)
                self.draw(painter, start_point, end_point, color)
'''
