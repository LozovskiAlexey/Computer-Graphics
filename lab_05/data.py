class Polygon(object):
    def __init__(self):
        self.points = list()
        self.maxes = list()

    def count(self):
        return len(self.points)

    def addPoint(self, point):
        self.points.append(point)

    def getLineStart(self):
        return self.points[-1]

    def getFirstPoint(self):
        return self.points[0]


class Borders(object):
    def __init__(self):
        self.xl = None
        self.xr = None

        self.upY = None
        self.downY = None

    def newX(self, x):
        if self.xl is None:
            self.xl = x
            self.xr = x
        elif self.xl > x:
            self.xl = x
        elif self.xr < x:
            self.xr = x

    def newY(self, y):
        if self.upY is None:
            self.downY = y
            self.upY = y
        elif self.downY > y:
            self.downY = y
        elif self.upY < y:
            self.upY = y

class Point(object):
    def __init__(self, x, y):
        self.X = x
        self.Y = y

