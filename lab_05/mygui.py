from designerGui import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTime, QEventLoop
from canvas import *


class myWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # виджет на котором отрисовка
        self.ui.fillFR = Canvas(self.ui.pointBox)
        self.ui.gridLayout.addWidget(self.ui.fillFR, 1, 1, 1, 1)

        # кнопки
        self.ui.clearButt.clicked.connect(self.clear)
        self.ui.lockButt.clicked.connect(lambda: self.ui.fillFR.lock())
        self.ui.doButt.clicked.connect(lambda: self.do())
        self.ui.addPointButt.clicked.connect(lambda: self.setPoint())

    def clear(self):
        self.ui.pointBox.clear()
        self.ui.fillFR.clear()

    def do(self):
        self.form_data()
        self.ui.fillFR.fill()

    def setPoint(self):
        x = int(self.ui.xcrd.text())
        y = int(self.ui.ycrd.text())
        point = Point(x, y)

        self.ui.fillFR.addPointToPointBox(point)  # добавляем точку в листбокс
        self.ui.fillFR.updateFigure(point)  # рисуем добавленную часть
        self.ui.fillFR.polygon.addPoint(point)

    def form_data(self):
        if self.ui.delayCHB.isChecked():
            self.ui.fillFR.delay_flag = 1
        else:
            self.ui.fillFR.delay_flag = 0

        if self.ui.drawBorderCHB.isChecked():
            self.ui.fillFR.border_flag = 1
        else:
            self.ui.fillFR.border_flag = 0

        text = str(self.ui.colorCB.currentText())
        if text == "Белый":
            color = QColor(255, 255, 255)
        elif text == "Синий":
            color = QColor(0, 0, 255)
        else:
            color = QColor(255, 0, 0)

        self.ui.fillFR.fill_color = color


