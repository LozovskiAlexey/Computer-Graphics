from PyQt5.QtCore import QPoint, QSize, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from data import *

# TODO добавить обработку граничных значений, проверку на замкнутость фигуры

class Canvas(QWidget):

    def __init__(self, pb):  # подается виджет с точками
        super().__init__()

        self.pixmap = QPixmap(self.size()).scaled(920, 630, Qt.IgnoreAspectRatio)
        self.pixmap.fill(Qt.transparent)

        self.point_box = pb

        self.border_color = QColor(255, 255, 255)
        self.fill_color = None
        self.drawing = False
        self.drawLinesFlag = False

        self.magicPixel = None
        self.mpX = None
        self.mpY = None

        self.start_x = None  # координаты начала отрисовки
        self.start_y = None
        self.tmp_x = None
        self.tmp_y = None

        self.minX = None
        self.minY = None
        self.maxX = None
        self.maxY = None

        self.setMouseTracking(True)

        self.delay_flag = 0

# параметры окна
# =============================================================
    def minimumSizeHint(self):
        return QSize(920, 630)

    def sizeHint(self):
        return QSize(920, 630)

# основные команды - очистка, заполнение, замыкание
# =============================================================
    def clean(self):
        self.pixmap = QPixmap(self.size())
        self.pixmap.fill(Qt.transparent)
        self.update()

    def clear(self):
        self.clean()
        self.clearPoints()

    def clearPoints(self):
        self.start_x = None
        self.start_y = None
        self.tmp_x = None
        self.tmp_y = None
        self.mpX = None
        self.mpY = None

    def lock(self):
        # замыкаем фигуру
        self.drawByMouse(self.start_x, self.start_y)
        self.clearPoints()

    def fill(self):
        # painter.setPen(self.fill_color)

        print("limits = ", self.minX, self.maxX, self.minY, self.maxY)
        stack = list()

        edge = QColor(255, 255, 255)
        fill = QColor(255, 0, 0)

        if self.mpX is None or self.mpY is None:
            return

        z = Point(self.mpX, self.mpY)
        stack.append(z)

        # пока стек не пуст

        while stack:
            img = self.pixmap.toImage()
            painter = QPainter()
            painter.begin(img)
            painter.setPen(QColor(255, 0, 0))

            # извлечение пикселя (х,у) из стека
            p = stack.pop()
            x = p.X
            y = p.Y

            # tx = x, запоминаем абсицссу
            xt = p.X
            Fl = 0
            # цвет(х,у) = цвет закраски
            painter.drawPoint(x, y)
            # заполняем интервал слева от затравки
            x = x - 1
            while QColor(img.pixel(x, y)) != self.border_color:
                painter.drawPoint(x, y)
                if not self.isOutOflimits(x, y):
                    # print("Вы еблан слева")
                    return
                x = x - 1

            # сохраняем крайний слева пиксел
            xl = x + 1
            x = xt
            # заполняем интервал справа от затравки

            x = x + 1
            while QColor(img.pixel(x, y)) != edge:
                if not self.isOutOflimits(x, y):
                    print("Вы еблан справа")
                    return
                painter.drawPoint(x, y)
                x = x + 1
            # сохраняем крайний справа пиксел
            xr = x - 1
            y = y + 1
            x = xl
            # ищем затравку на строке выше
            while x <= xr:
                Fl = 0
                while QColor(img.pixel(x, y)) != edge and QColor(img.pixel(x, y)) != fill and x <= xr:
                    if Fl == 0:
                        Fl = 1
                    x = x + 1

                if Fl == 1:
                    if x == xr and QColor(img.pixel(x, y)) != fill and QColor(img.pixel(x, y)) != edge:
                        stack.append(Point(x, y))
                    else:
                        stack.append(Point(x - 1, y))
                    Fl = 0

                xt = x
                while (QColor(img.pixel(x, y)) == edge or QColor(img.pixel(x, y)) == fill) and x < xr:
                    x = x + 1

                if x == xt:
                    x = x + 1

            y = y - 2
            x = xl
            while x <= xr:
                Fl = 0
                while QColor(img.pixel(x, y)) != edge and QColor(img.pixel(x, y)) != fill and x <= xr:
                    if Fl == 0:
                        Fl = 1
                    x = x + 1

                if Fl == 1:
                    if x == xr and QColor(img.pixel(x, y)) != fill and QColor(img.pixel(x, y)) != edge:
                        stack.append(Point(x, y))
                    else:
                        stack.append(Point(x - 1, y))
                    Fl = 0

                xt = x
                while (QColor(img.pixel(x, y)) == edge or QColor(img.pixel(x, y)) == fill) and x < xr:
                    x = x + 1

                if x == xt:
                    x = x + 1

            self.pixmap = QPixmap.fromImage(img)
            painter.end()
            self.update()

            if self.delay_flag:
                self.delay()

# =============================================================
    def drawByMouse(self, x, y):

        self.updateLimits(x, y)

        painter = QPainter()
        painter.begin(self.pixmap)
        painter.setPen(self.border_color)

        if self.tmp_x is not None and self.tmp_y is not None:
            painter.drawLine(self.tmp_x, self.tmp_y, x, y)

        self.tmp_x, self.tmp_y = x, y

        painter.end()
        self.update()

    def addPointToPointBox(self, point):
        # добавляет пиксель в пойнтбокс
        if point.X is not None:
            item = QListWidgetItem("x = {0}, y = {1}; ".format(point.X, point.Y))
            self.point_box.addItem(item)

    def isOutOflimits(self, x, y):
        flag = False
        if self.minX < x < self.maxX:
            if self.minY < y < self.maxY:
                flag = True
        return flag

    def updateLimits(self, x, y):
        if self.minX is None or self.minX > x:
            self.minX = x
        if self.minY is None or self.minY > y:
            self.minY = y
        if self.maxX is None or self.maxX < x:
            self.maxX = x
        if self.maxY is None or self.maxY < y:
            self.maxY = y

    def delay(self):
        self.repaint()
        self.repaint()

#
# =============================================================
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.drawPixmap(QPoint(), self.pixmap)

    def mousePressEvent(self, e):
        if self.magicPixel:
            self.mpX = e.x()
            self.mpY = e.y()
            self.addPointToPointBox(Point(self.mpX, self.mpY))
            self.magicPixel = False
            return

        if e.button() == Qt.LeftButton and self.drawLinesFlag:
            tmp_x, tmp_y = e.x(), e.y()
            point = Point(tmp_x, tmp_y)
            self.addPointToPointBox(point)

            if self.start_x is None:
                self.start_x = tmp_x
                self.start_y = tmp_y

            self.drawByMouse(tmp_x, tmp_y)
        elif e.button() == Qt.LeftButton:
            self.drawing = True

    def mouseMoveEvent(self, e):
        if self.drawing:
            tmp_x, tmp_y = e.x(), e.y()
            self.drawByMouse(tmp_x, tmp_y)

            if self.start_x is None:
                self.start_x = tmp_x
                self.start_y = tmp_y

    def mouseReleaseEvent(self, e):
        self.drawing = False
        point = Point(self.tmp_x, self.tmp_y)
        # if e.button() == Qt.LeftButton and not self.drawLinesFlag:
        #     self.addPointToPointBox(point)
