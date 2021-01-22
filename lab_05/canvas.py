from PyQt5.QtCore import QPoint, QSize, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from data import *


class Canvas(QWidget):

    def __init__(self, pb):  # подается виджет с точками
        super().__init__()

        self.pixmap = QPixmap(self.size()).scaled(920, 630, Qt.IgnoreAspectRatio)
        self.pixmap.fill(Qt.transparent)

        self.point_box = pb
        self.border_color = QColor(255, 255, 255)
        self.fill_color = None

        self.setMouseTracking(True)
        self.figure = list()
        self.polygon = Polygon()
        self.borders = Borders()

        self.delay_flag = 0
        self.border_flag = 0

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
        self.figure = list()
        self.polygon = Polygon()

    def lock(self):
        if self.polygon.count() == 0:
            return

        # замыкаем фигуру
        lock_point = self.polygon.getFirstPoint()
        self.updateFigure(lock_point)
        self.figure.append(self.polygon)  # добавляем к фигуре

        self.polygon = Polygon()  # создаем новый полигон

    def fill(self):
        self.clean()
        self.drawFigure(1)
        self.fillFigure()
        if self.border_flag:
            self.drawFigure(0)
            self.update()

    def fillFigure(self):
        y_st, y_end = self.borders.upY, self.borders.downY-1
        x_st, x_end = self.borders.xl, self.borders.xr

        for y in range(y_st, y_end, -1):

            painter = QPainter()
            img = self.pixmap.toImage()
            painter.begin(img)
            painter.setPen(self.fill_color)

            flag = False
            for x in range(x_st, x_end):
                color = img.pixel(x, y)
                if QColor(color) == self.border_color:
                    flag = not flag
                if flag:
                    painter.drawPoint(x, y)

            self.pixmap = QPixmap.fromImage(img)
            self.update()
            if self.delay_flag == 1:
                self.delay()

# работа с точкой, при формировании данных
# принимает точку, берет ее координаты, добавляет как вершину
# в фигуру и обновляет рисунок
# =============================================================
    def mousePressEvent(self, event):
        pixel = event.pos()           # позиция курсора
        point = self.getPoint(pixel)  # получаем координаты пикселя

        self.addPointToPointBox(point)  # добавляем точку в листбокс
        self.updateFigure(point)        # рисуем добавленную часть
        self.polygon.addPoint(point)    # добавляем вершину в полигон

    def getPoint(self, pixel):
        # получает координаты пикселя к экрана
        point = Point(pixel.x(), pixel.y())
        return point

    def addPointToPointBox(self, point):
        # добавляет пиксель в пойнтбокс
        item = QListWidgetItem("x = {0}, y = {1}; ".format(point.X, point.Y))
        self.point_box.addItem(item)

    def drawBrezenInt(self, start, end):
        painter = QPainter(self.pixmap)
        painter.setPen(self.border_color)

        x0, y0 = start.X, start.Y
        x1, y1 = end.X, end.Y
        xchng = 0  # флаг для смены dx dy

        # если линия вырождена
        if start == end:
            painter.drawPoint(x0, y0)
            return

        x, y = x0, y0
        dx = x1 - x0
        dy = y1 - y0

        sx, sy = sign(dx), sign(dy)  # направление отрисовки
        dx, dy = abs(dx), abs(dy)

        # проверка на перестановку dx dy
        if dx <= dy:
            dx, dy = dy, dx
            xchng = 1
        e = 2 * dy - dx

        for i in range(1, dx + 1):
            painter.drawPoint(x, y)

            if e >= 0:
                if not xchng:
                    y += sy
                else:
                    x += sx
                e -= 2 * dx
            if not xchng:
                x += sx
            else:
                y += sy
            e += 2 * dy

    def updateFigure(self, end):
        # дорисовывает фигуру с новой точкой
        if self.polygon.count() == 0:
            return

        start_p = self.polygon.getLineStart()  # получает координаты прямой которую надо дорисовать
        end_p = end

        self.drawBrezenInt(start_p, end_p)  # рисует прямую
        self.update()

    def delay(self):
        self.repaint()
        self.repaint()

#
# =============================================================
    def setPixel(self, point, img, painter):
        # рисует пиксель на экране по координатам
        color = img.pixel(point.X, point.Y)
        if QColor(color) == self.border_color:
            painter.drawPoint(point.X + 1, point.Y)
        else:
            painter.drawPoint(point.X, point.Y)

    def setPixel(self, x, y, img, painter):
        # рисует пиксель на экране по координатам
        color = img.pixel(x, y)
        if QColor(color) == self.border_color:
            painter.drawPoint(x + 1, y)
        else:
            painter.drawPoint(x, y)

    def drawFigure(self, flag):
        if len(self.figure) == 0:
            return

        for polygon in self.figure:
            self.drawPolygon(polygon, flag)

    def drawPolygon(self, polygon, flag):
        l = polygon.count()
        for i in range(l):
            start = polygon.points[i]
            end = polygon.points[(i+1) % l]

            if flag == 1:
                self.newBorder(start, end)
            else:
                self.drawBrezenInt(start, end)

    def newBorder(self, start, end):
        pix = self.pixmap
        img = pix.toImage()
        painter = QPainter()
        painter.begin(img)
        painter.setPen(self.border_color)

        x0, y0 = start.X, start.Y
        x1, y1 = end.X, end.Y
        L = 0

        if y1 < y0:
            x0, y0, x1, y1 = x1, y1, x0, y0

        x, y = x0, y0

        dx = x1 - x0
        dy = y1 - y0

        self.borders.newX(start.X)
        self.borders.newY(start.Y)

        Dx, Dy = abs(dx), abs(dy)
        if Dx > Dy:
            L = Dx
        else:
            L = Dy

        dx = dx / L
        dy = dy / L

        lasty = y0
        self.setPixel(round(x), round(y), img, painter)

        for i in range(0, L):
            if lasty != round(y):
                lasty = round(y)
                self.setPixel(round(x), round(y), img, painter)
            x += dx  # округлить
            y += dy  # округлить

            if round(y) == y1:
                break

        if y0 == y1:
            self.setPixel(round(x), round(y), img, painter)

        painter.end()
        pixmap = QPixmap.fromImage(img)
        self.pixmap = pixmap
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(QPoint(), self.pixmap)


def sign(coord):
    # определение направления изменения координаты
    # при отрисовке
    if coord > 0:
        return 1
    elif coord < 0:
        return -1
    else:
        return 0
