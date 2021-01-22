from designerGui import Ui_MainWindow
from line import LineCanvas, LineCmp
from draw_algorithms import *
from PyQt5.QtWidgets import *


class myWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.LineFR = LineCanvas()  # для отрисовки линии
        self.ui.cmpFR = LineCmp()  # для отрисовки узла лучей

        self.ui.gridLayout.addWidget(self.ui.LineFR, 1, 1, 1, 1)
        self.ui.gridLayout.addWidget(self.ui.cmpFR, 1, 3, 1, 1)

        # Привязка функций к pushButt
        self.ui.doButt.clicked.connect(self.do)
        self.ui.clearButt.clicked.connect(self.clear)

    # выполнение отрисовки
    def do(self):
        color = self.getColor()  # выбор цвета

        if self.ui.colorCHB.isChecked():  # цвет фона
            self.ui.LineFR.color = [29, 29, 29]
        elif color is not None:
            self.ui.LineFR.color = color  # выбранный пользователем цвет
        else:
            self.ui.LineFR.color = [255, 255, 255]  # цвет линии по умолчанию

        # выбор алгоритма
        if self.ui.ddaRB.isChecked():
            self.ui.LineFR.draw = ddaAlg  # ЦДА

        elif self.ui.decimalRB.isChecked():
            self.ui.LineFR.draw = decimalAlg  # с вещественными числами

        elif self.ui.intRB.isChecked():
            self.ui.LineFR.draw = intAlg  # на целых числах

        elif self.ui.deleteStepRB.isChecked():
            self.ui.LineFR.draw = deleteStepAlg  # удаление ступенек

        elif self.ui.libRB.isChecked():
            self.ui.LineFR.draw = libAlg  # библиотечный

        # отрисовка узла, если кнопка активирована
        if self.ui.cmpCHB.isChecked():

            self.ui.cmpFR.draw = self.ui.LineFR.draw  # присвоение алгоритма отрисовки
            self.ui.cmpFR.color = self.ui.LineFR.color  # присвоение цвета
            self.ui.cmpFR.step = self.get_step()  # получили шаг с которым отрисуется узел

            self.ui.cmpFR.myDrawLine()  # отрисовка узла лучей

        # Получение координат прямой
        if self.ui.lineCHB.isChecked():
            start_point = self.getPoints(self.ui.xstartEdit, self.ui.ystartEdit)
            end_point = self.getPoints(self.ui.xendEdit, self.ui.yendEdit)

            if end_point is not None and start_point is not None:

                # если все координаты введены корректно
                # отрисовка линии
                self.ui.LineFR.start_point = start_point
                self.ui.LineFR.end_point = end_point
                self.ui.LineFR.myDrawLine()

                # Вывод текста о результате отрисовки
                if self.ui.LineFR.check == 1:
                    self.ui.statusbar.showMessage('Прямая была полностью отображена.',
                                                  2000)
                else:
                    self.ui.statusbar.showMessage('Прямая отображена не полностью.',
                                                  2000)
            else:
                self.ui.statusbar.showMessage('Некорректный ввод. Пожалуйста,'
                                              'заполните все поля целыми числами.')

    # обработка виджетов
    # ============================================================
    def getPoints(self, x, y):
        # считывает из полей ввода текст
        # если текст считан успешно, возвращает значения типа int
        # иначе None
        point_x = x.text()  # начало отрезка
        point_y = y.text()  # конец отрезка

        if self.isInt([point_x, point_y]):
            return [int(point_x), int(point_y)*(-1)]
        else:
            self.clearPointsBox()
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

        if not return_value:
            # self.ui.statusbar.showMessage("Некорректный ввод", 2000)
            pass

        return return_value

    def get_step(self):
        step = self.ui.stepEdit.text()
        if self.isInt([step]):
            return step
        else:
            return 30

    # Очистка виджетов
    # ================================================================
    def clearColorBox(self):
        # очищает поля ввода цветов
        self.ui.rEdit.setText('')
        self.ui.gEdit.setText('')
        self.ui.bEdit.setText('')

    def clearPointsBox(self):
        # очищает поля ввода координат отрезка
        self.ui.xstartEdit.setText('')
        self.ui.ystartEdit.setText('')
        self.ui.xendEdit.setText('')
        self.ui.yendEdit.setText('')

    def clear(self):
        # очищает все поля
        self.clearColorBox()
        self.clearPointsBox()
        self.ui.LineFR.clear()
        self.ui.cmpFR.clear()

