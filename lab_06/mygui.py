from designerGui import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
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
        self.ui.superPixelButton.clicked.connect(lambda: self.setMagicPoint())

    def clear(self):
        self.ui.pointBox.clear()
        self.ui.fillFR.clear()

    def do(self):
        self.form_data()
        self.ui.fillFR.fill()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Alt:
            self.ui.fillFR.drawLinesFlag = True
        # e.accept()

    def keyReleaseEvent(self, e):
        if e.key() == QtCore.Qt.Key_Alt:
            self.ui.fillFR.drawLinesFlag = False

    def setPoint(self):
        x = int(self.ui.xcrd.text())
        y = int(self.ui.ycrd.text())
        point = Point(x, y)

        self.ui.fillFR.addPointToPointBox(point)  # добавляем точку в листбокс
        self.ui.fillFR.drawByMouse(x, y)

    def setMagicPoint(self):
        self.ui.fillFR.magicPixel = True
        x = int(self.ui.superPixelXEdit.text())
        y = int(self.ui.superPixelYEdit.text())

        if x == 0 and y == 0:
            return
        else:
            self.ui.fillFR.mpX = x
            self.ui.fillFR.mpY = y
            self.ui.fillFR.addPointToPointBox(Point(x, y))
            self.ui.fillFR.magicPixel = False

    def form_data(self):
        # определение задержки
        if self.ui.delayCHB.isChecked():
            self.ui.fillFR.delay_flag = 1
        else:
            self.ui.fillFR.delay_flag = 0

        # выбор цвета
        text = str(self.ui.colorCB.currentText())
        if text == "Белый":
            color = QColor(255, 255, 255)
        elif text == "Синий":
            color = QColor(0, 0, 255)
        else:
            color = QColor(255, 0, 0)

        self.ui.fillFR.fill_color = color


