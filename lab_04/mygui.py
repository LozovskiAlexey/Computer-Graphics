from designerGui import Ui_MainWindow
from PyQt5.QtWidgets import *
from figure import *
from canvas import *


class myWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.circleFR = CircleCanvas()  # для отрисовки линии
        self.ui.cmpFR = CircleCmp()  # для отрисовки узла лучей

        self.ui.gridLayout.addWidget(self.ui.circleFR, 1, 1, 1, 1)
        self.ui.gridLayout.addWidget(self.ui.cmpFR, 1, 3, 1, 1)

        # Привязка функций к pushButt
        self.ui.doButt.clicked.connect(self.do)
        self.ui.clearButt.clicked.connect(self.clear)

    def do(self):
        cmpflag = 0
        figureflag = 1
        if self.ui.cmpCHB.isChecked():
            cmpflag = 1

        # выбор фигуры (окружность/эллипс)
        if self.ui.circleRB.isChecked():

            #  определяем радиус
            radius = self.getPoint(self.ui.radEdit)

            if radius is not None:
                self.ui.circleFR.figure = Circle(radius)
            else:
                if cmpflag == 0:
                    self.ui.statusbar.showMessage('Введите радиус', 2000)
                    return
                else:
                    figureflag = 0
                    self.ui.circleFR.figure = Circle(radius)

        #  если выбран эллипс
        elif self.ui.ellipseRB.isChecked():
            #  определяем полуоси
            Ox = self.getPoint(self.ui.oxEdit)
            Oy = self.getPoint(self.ui.oyEdit)

            if Ox is not None and Oy is not None:
                self.ui.circleFR.figure = Ellipse(Ox, Oy)
            else:
                if cmpflag == 0:
                    self.ui.statusbar.showMessage('Введите полуоси', 2000)
                    return
                else:
                    figureflag = 0
                    self.ui.circleFR.figure = Ellipse(0, 0)

        # если фигура не выбрана
        else:
            self.ui.statusbar.showMessage('Фигура не выбрана', 2000)
            return

        # выбор цвета
        color = self.getColor()

        if color:
            self.ui.circleFR.color = color
            self.ui.cmpFR.color = color
        else:
            self.ui.circleFR.color = [255, 255, 255]
            self.ui.cmpFR.color = [255, 255, 255]

        if self.ui.colorCHB.isChecked():
            print("lol")
            self.ui.circleFR.color = [29, 29, 29]
            self.ui.cmpFR.color = [29, 29, 29]

        # выбор алгоритма
        if self.ui.brezenRB.isChecked():
            self.ui.circleFR.figure.alg = 1
        elif self.ui.midpointRB.isChecked():
            self.ui.circleFR.figure.alg = 2
        elif self.ui.canonRB.isChecked():
            self.ui.circleFR.figure.alg = 3
        elif self.ui.paramRB.isChecked():
            self.ui.circleFR.figure.alg = 4
        elif self.ui.libRB.isChecked():
            self.ui.circleFR.figure.alg = 5
        else:
            self.ui.statusbar.showMessage('Алгоритм не выбран', 2000)
            return

        # отрисовка одной фигуры
        if figureflag:
            self.ui.circleFR.myDrawCircle()

        # сравнение отрисовки
        if self.ui.cmpCHB.isChecked():

            self.ui.cmpFR.figure = self.ui.circleFR.figure

            # считывание параметров для отрисовки
            d = self.ui.distEdit.text()  # расстояние между эллипсами
            st = self.ui.stepEdit.text()  # количество(да, я назвал это шагом)
            ox = self.ui.minOX.text()  # минимальный размер полуосей
            oy = self.ui.minOY.text()

            self.ui.cmpFR.figure.Ox = int(ox)
            self.ui.cmpFR.figure.Oy = int(oy)
            self.ui.cmpFR.figure.step = int(st)
            self.ui.cmpFR.figure.dist = int(d)

            self.ui.cmpFR.myDrawCircle()

    def clear(self):
        self.clearPoints()
        self.clearColorBox()
        self.ui.circleFR.clear()
        self.ui.cmpFR.clear()

    # обработка виджетов
# ============================================================

    def getPoint(self, entry):
        # считывает из полей ввода текст
        # если текст считан успешно, возвращает значения типа int
        # иначе None
        point_x = entry.text()  # начало отрезка

        if self.isInt([point_x]):
            return int(point_x)
        else:
            # self.clearPointsBox()
            return None

    def getColor(self):
        # считывает цвета из виджета
        # если ошибка очистит поля ввода
        r = self.ui.rEdit.text()
        g = self.ui.gEdit.text()
        b = self.ui.bEdit.text()

        if self.isInt([r, g, b]):
            return [int(r), int(g), int(b)]
        else:
            self.clearColorBox()
            return None

    def isInt(self, args):
        # проверяет число на целость
        # в случае ошибки в виджет будет записано сообщение
        return_value = 1

        for i in args:
            try:
                float(i)
                if float(i) - float(int(i)) != 0.0:
                    raise ValueError
            except ValueError:
                return_value = 0
                break

        return return_value

        # Очистка виджетов
        # ================================================================

    def clearColorBox(self):
        # очищает поля ввода цветов
        self.ui.rEdit.setText('')
        self.ui.gEdit.setText('')
        self.ui.bEdit.setText('')

    def clearPoints(self):
        self.ui.radEdit.setText('')
        self.ui.oxEdit.setText('')
        self.ui.oyEdit.setText('')
