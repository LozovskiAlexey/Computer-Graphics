from math import cos, sin, radians
from PyQt5.QtCore import QPoint, QSize, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Canvas(QWidget):

    def __init__(self):
        super().__init__()

        self.radius = 10000

        self.array = None
        self.back_state = None
        self.getFirstState()

        self.pen = QPen()
        self.brush = QBrush(Qt.red, Qt.BDiagPattern)

        p = QPalette()
        p.setColor(QPalette.Background, Qt.black)
        self.setAutoFillBackground(True)
        self.setPalette(p)

    def get_circle(self, y):
        return (self.radius - y*y)**0.5

    def get_parable(self, y):
        return (0.14907 * y)**2

    def minimumSizeHint(self):
        return QSize(800, 639)

    def sizeHint(self):
        return QSize(800, 639)

    def move(self, dx, dy):
        self.back_state = self.array
        dy = -dy
        self.array = [(item[0] + dx, item[1] + dy) for item in self.array]
        self.update()

    def turn(self, xc, yc, fi):
        self.back_state = self.array
        self.array = [(xc + (item[0] - xc) * cos(radians(fi)) + (item[1] - yc) * sin(radians(fi)),
                       yc - (item[0] - xc) * sin(radians(fi)) + (item[1] - yc) * cos(radians(fi)))
                      for item in self.array]

        self.update()

    def scale(self, kx, ky, xm, ym):
        self.back_state = self.array
        self.array = [(kx * item[0] + (1 - kx) * xm,
                       ky * item[1] + (1 - ky) * ym)
                      for item in self.array]
        self.update()

    def getFirstState(self):
        # вернет исходное состояние фигуры
        array = [(self.get_circle(y), y) for y in range(-60, 61)]
        array.extend([(self.get_parable(y), y) for y in range(60, -61, -1)])

        self.array = array
        self.update()

    def stepBack(self):

        if self.back_state is not None:
            self.array = self.back_state
            self.update()
        else:
            print('ddd')

    def paintEvent(self, event):

        pnt = QPainter(self)
        pnt.translate(self.width()/2, self.height()/2)

        figure = QPolygon([QPoint(item[0], item[1]) for item in self.array])
        pnt.setPen(self.pen)
        pnt.setBrush(self.brush)
        pnt.drawPolygon(figure)
        pnt.restore()

        pnt.setPen(self.palette().dark().color())
        pnt.setBrush(Qt.NoBrush)
