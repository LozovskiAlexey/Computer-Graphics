from math import cos, sin, sqrt, pi
from PyQt5.QtCore import QPoint

class Figure(object):
    def __init__(self):

        self.alg = None
        self.draw = {1: self.brezenAlg,
                     2: self.midPointAlg,
                     3: self.canonAlg,
                     4: self.paramAlg,
                     5: self.libAlg}

        self.step = 50
        self.dist = 50

    def brezenAlg(self, painter): pass

    def midPointAlg(self, painter): pass

    def canonAlg(self, painter): pass

    def paramAlg(self, painter): pass

    def libAlg(self, painter): pass

    def cmpCircle(self, painter): pass


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()

        self.Ox = radius
        self.step = 50
        self.dist = 50

    def brezenAlg(self, painter):

        r = self.Ox *2
        x = 0
        y = r

        di = 2 - 2*r
        y_end = 0
        while y >= y_end:

            # отрисовка
            painter.drawPoint(x, y)
            painter.drawPoint(-x, -y)
            painter.drawPoint(x, -y)
            painter.drawPoint(-x, y)

            # выделение случая расположения пикселя
            # относительно окружности
            if di < 0:  # пиксель внутри окружности
                b = 2*di + 2*y - 1
                x += 1

                if b <= 0:  # шаг вправо
                    di += 2*x + 1
                else:  # шаг по диагонали
                    y -= 1
                    di += 2*x - 2*y + 2

            elif di > 0:  # пиксель вне окружности
                b = 2*di - 2*x - 1  # сомнительно
                y -= 1

                if b <= 0:  # шаг по диагонали
                    x += 1
                    di += 2*x - 2*y + 2
                else:  # шаг вниз
                    di += - 2*y + 1

            else:  # пиксель совпал с окружностью
                x += 1
                y -= 1
                di += 2*x - 2*y + 2

    def midPointAlg(self, painter):
        r = self.Ox*2
        x, y = 0, r
        # d = 5/4 - r  # (x + 1)^2 + (y - 1/2)^2 - r^2
        d = 1 - r

        # Отрисовка 1/8 части окружности
        while x <= y:
            painter.drawPoint(x, y)
            painter.drawPoint(-x, -y)
            painter.drawPoint(x, -y)
            painter.drawPoint(-x, y)

            painter.drawPoint(y, x)
            painter.drawPoint(-y, -x)
            painter.drawPoint(y, -x)
            painter.drawPoint(-y, x)

            x += 1

            if d < 0:  # пиксель внутри окружности
                d += 2*x + 1
            else:  # пиксель вне или на окружности
                y -= 1
                d += 2*x - 2*y + 1  # 5

    def canonAlg(self, painter):

        r = self.Ox *2
        dx = round(r / sqrt(2))
        x = 0
        while x <= dx:
            y = round(sqrt(r*r - x*x))

            painter.drawPoint(x, y)
            painter.drawPoint(x, -y)
            painter.drawPoint(-x, y)
            painter.drawPoint(-x, -y)
            painter.drawPoint(y, x)
            painter.drawPoint(-y, -x)
            painter.drawPoint(y, -x)
            painter.drawPoint(-y, x)

            x += 1

    def paramAlg(self, painter):
        r = self.Ox *2
        # l = round(pi*r)

        d = 1/r
        fi = pi/2
        while fi >= pi/4:
            x = round(r * cos(fi))
            y = round(r * sin(fi))

            painter.drawPoint(x, y)
            painter.drawPoint(x, -y)
            painter.drawPoint(-x, y)
            painter.drawPoint(-x, -y)
            painter.drawPoint(y, x)
            painter.drawPoint(-y, -x)
            painter.drawPoint(y, -x)
            painter.drawPoint(-y, x)
            fi -= d

    def libAlg(self, painter):
        r = self.Ox
        painter.drawEllipse(QPoint(0, 0), r*2, r*2)

    def cmpCircle(self, painter):
        if self.alg is None:
            return

        i = 0

        while i < int(self.step):
            self.draw[self.alg](painter)
            self.Ox += int(self.dist)

            i += 1


class Ellipse(Figure):
    def __init__(self, ox, oy):
        super().__init__()

        self.Ox = ox*2  # какого размера
        self.Oy = oy*2

        self.st_ox = 0
        self.st_oy = 0

        self.step = 50

    def brezenAlg(self, painter):
        b = self.Oy
        x = 0  # начальные значения
        y = b

        a = self.Ox

        sqr_a = a*a
        sqr_b = b*b

        d = round((sqr_a + sqr_b) / 2 - 2*sqr_a*b)
        while y >= 0:

            painter.drawPoint(x, y)
            painter.drawPoint(x, -y)
            painter.drawPoint(-x, y)
            painter.drawPoint(-x, -y)

            if d < 0:  # пиксель лежит внутри эллипса
                buf = 2*d + 2*sqr_a*y - sqr_a
                x += 1
                if buf <= 0:  # горизотальный шаг
                    d += 2*sqr_b*x + sqr_b
                else:  # диагональный шаг
                    y -= 1
                    d += 2*sqr_b*x - 2*sqr_a*y + sqr_a + sqr_b

            elif d > 0:  # пиксель лежит вне эллипса
                buf = 2*d - 2*sqr_b*x - sqr_b
                y -= 1

                if buf > 0:  # вертикальный шаг
                    d += sqr_a - 2*y*sqr_a
                else:  # диагональный шаг
                    x += 1
                    d += 2*x*sqr_b - 2*y*sqr_a + sqr_a + sqr_b

            else:  # пиксель лежит на окружности
                x += 1  # диагональный шаг
                y -= 1
                d += 2*x*sqr_b - 2*y*sqr_a + sqr_a + sqr_b

    def midPointAlg(self, painter):
        a = self.Ox
        b = self.Oy
        a2 = a*a
        b2 = b*b
        x = 0  # начальные положения
        y = b
        delta = b2 + a2 * (y - 0.5) * (y - 0.5) - a2 * b2  # начальное значение параметра принятия решения в области tg<1
        border = int(a2 / sqrt(b2 + a2))
        while x <= border:  # пока тангенс угла наклона меньше 1
            painter.drawPoint(x, y)
            painter.drawPoint(x, -y)
            painter.drawPoint(-x, y)
            painter.drawPoint(-x, -y)

            x += 1
            if delta > 0:  # средняя точка внутри эллипса, ближе верхний пиксел, горизонтальный шаг
                y -= 1
                delta += a2 * (-2 * y)
            delta += b2 * (2 * x + 1)

        delta += 0.75 * (a2 - b2) - (b2 * x + a2 * y)
        # начальное значение параметра принятия решения в области tg>1 в точке (х + 0.5, y - 1) полседнего положения

        while y >= 0:
            painter.drawPoint(x, y)
            painter.drawPoint(x, -y)
            painter.drawPoint(-x, y)
            painter.drawPoint(-x, -y)

            y -= 1
            if delta < 0:
                x += 1
                delta += b2 * (2 * x)
            delta += a2 * (-2 * y + 1)

    def canonAlg(self, painter):
        a = self.Ox
        b = self.Oy

        a2 = a*a
        b2 = b*b
        dx = round(a2/sqrt(a2+b2))
        bDivA = b/a

        x = 0
        while x <= dx:
            y = round(sqrt(a2 - x * x) * bDivA)
            painter.drawPoint(x, y)
            painter.drawPoint(x, -y)
            painter.drawPoint(-x, y)
            painter.drawPoint(-x, -y)
            x += 1

        dy = round(b2/sqrt(a2 + b2))
        y = 0
        while y <= dy:
            x = round(sqrt((b2 - y * y)) / bDivA)
            painter.drawPoint(x, y)
            painter.drawPoint(x, -y)
            painter.drawPoint(-x, y)
            painter.drawPoint(-x, -y)
            y += 1

    def paramAlg(self, painter):
        a = self.Ox
        b = self.Oy

        m = max(a, b)
        d = 1/m

        i = pi/2
        while i >= 0:
            x = round(a * cos(i))
            y = round(b * sin(i))

            painter.drawPoint(x, y)
            painter.drawPoint(x, -y)
            painter.drawPoint(-x, y)
            painter.drawPoint(-x, -y)

            i -= d

    def libAlg(self, painter):
        ox = self.Ox
        oy = self.Oy

        painter.drawEllipse(QPoint(0, 0), ox, oy)

    def cmpCircle(self, painter):
        if self.alg is None:
            return

        dx = 1.0
        dy = 1.0

        if self.Ox > self.Oy:
            dx = self.Ox / self.Oy
        else:
            dy = self.Oy / self.Ox

        i = 0
        self.Ox *= 2
        self.Oy *= 2
        tmp_ox, tmp_oy = 0.0, 0.0
        while i < self.step:
            self.draw[self.alg](painter)
            tmp_ox += dx * self.dist
            tmp_oy += dy * self.dist

            self.Ox += round(dx * self.dist)
            self.Oy += round(dy * self.dist)

            i += 1

        self.Ox = 50
        self.Oy = 25
