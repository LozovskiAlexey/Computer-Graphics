from designerGUI import Ui_MainWindow
from figure import *
from PyQt5.QtWidgets import *


class mywindow(QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.canvas = Canvas()
        self.ui.horizontalLayout.addWidget(self.ui.canvas)

        self.setDisabled()  # закрывает доступ к виджетам ввода

        self.ui.scaleRB.toggled.connect(self.openscaleLE)
        self.ui.moveRB.toggled.connect(self.openmoveLE)
        self.ui.turnRB.toggled.connect(self.openturnLE)

        self.ui.doButt.clicked.connect(self.do)
        self.ui.fisrtStateButt.clicked.connect(self.getFirstState)
        self.ui.stepBackButt.clicked.connect(self.stepBack)

    # выполнение операций над фигурой
    def do(self):
        if self.ui.scaleRB.isChecked():
            self.scale()
        elif self.ui.moveRB.isChecked():
            self.move()
        elif self.ui.turnRB.isChecked():
            self.turn()

    def stepBack(self,):
        self.ui.canvas.stepBack()

    def getFirstState(self):
        self.ui.canvas.getFirstState()

    def openscaleLE(self):
        # Открывает ввод для параметров масштабирования
        self.setDisabled()
        self.ui.scxlineEdit.setReadOnly(False)
        self.ui.scylineEdit.setReadOnly(False)
        self.ui.kxlineEdit.setReadOnly(False)
        self.ui.kylineEdit.setReadOnly(False)

    def openmoveLE(self):
        # откровает ввод для параметров переноса
        self.setDisabled()
        self.ui.dxlineEdit.setReadOnly(False)
        self.ui.dylineEdit.setReadOnly(False)

    def openturnLE(self):
        # открывает ввод для переметров поворота
        self.setDisabled()
        self.ui.turnxlineEdit.setReadOnly(False)
        self.ui.turnylineEdit.setReadOnly(False)
        self.ui.anglelineEdit.setReadOnly(False)

    def setDisabled(self):
        # установка на состояние "Только чтение"
        # виждеты ввода текста для масштабирования
        self.ui.scxlineEdit.setReadOnly(True)
        self.ui.scylineEdit.setReadOnly(True)
        self.ui.kxlineEdit.setReadOnly(True)
        self.ui.kylineEdit.setReadOnly(True)

        # виджеты воода для перемещения
        self.ui.dxlineEdit.setReadOnly(True)
        self.ui.dylineEdit.setReadOnly(True)

        # виджеты ввода для вращения
        self.ui.turnxlineEdit.setReadOnly(True)
        self.ui.turnylineEdit.setReadOnly(True)
        self.ui.anglelineEdit.setReadOnly(True)

    def getText(selfб, lineEdit):
        # получает на вход виджет
        # читает из него текст
        # проверяет корректность ввода
        coord = lineEdit.text()
        try:
            float(coord)
        except ValueError:
            result = None
        else:
            result = float(coord)
        return result

    def setPoint(self):
        # отрисовка центров вращения и масштабирования
        pass

    def move(self):
        # перемещение фигуры
        dx = self.getText(self.ui.dxlineEdit)
        dy = self.getText(self.ui.dylineEdit)

        if dx is None or dy is None:
            self.statusBar().showMessage("Некорректный ввод", 3000)
            self.ui.dylineEdit.setText('')  # очистка содержимого виджетов
            self.ui.dxlineEdit.setText('')
        else:
            self.ui.canvas.move(dx, dy)


    def scale(self):
        # масштабирование фигуры
        x = self.getText(self.ui.scxlineEdit)
        y = self.getText(self.ui.scylineEdit)
        kx = self.getText(self.ui.kxlineEdit)
        ky = self.getText(self.ui.kylineEdit)

        if (x is None or y is None or
            kx is None or ky is None):

            self.statusBar().showMessage("Некорректный ввод", 3000)
            self.ui.scxlineEdit.setText('')  # очистка содержимого виджетов
            self.ui.scylineEdit.setText('')
            self.ui.kxlineEdit.setText('')
            self.ui.kylineEdit.setText('')
        else:
            self.ui.canvas.scale(kx, ky, x, y)

    def turn(self):
        # Поворот фигуры
        x = self.getText(self.ui.turnxlineEdit)
        y = self.getText(self.ui.turnylineEdit)
        angle = self.getText(self.ui.anglelineEdit)

        if x is None or y is None or angle is None:

            self.statusBar().showMessage("Некорректный ввод", 3000)
            self.ui.turnxlineEdit.setText('')  # очистка содержимого виджетов
            self.ui.turnylineEdit.setText('')
            self.ui.anglelineEdit.setText('')

        else:
            self.ui.canvas.turn(x, y, angle)