# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1236, 704)
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(5, 0))
        self.frame_4.setStyleSheet("background-color: rgb(135, 135, 135)\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout.addWidget(self.frame_4, 1, 2, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(300, 0))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setStyleSheet("background-color: rgb(181, 181, 181)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_11 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(0, 40))
        self.label_11.setStyleSheet("font: bold 16px;")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setStyleSheet("background-color: rgb(135, 135, 135);\n"
"font: bold 14px;")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setContentsMargins(10, -1, 10, -1)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.colorCB = QtWidgets.QComboBox(self.groupBox_3)
        self.colorCB.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: white;\n"
"font: bold 14px;\n"
"min-width: 10em;\n"
"padding: 4px;")
        self.colorCB.setObjectName("colorCB")
        self.colorCB.addItem("")
        self.colorCB.addItem("")
        self.colorCB.addItem("")
        self.gridLayout_2.addWidget(self.colorCB, 2, 0, 1, 1)
        self.drawBorderCHB = QtWidgets.QCheckBox(self.groupBox_3)
        self.drawBorderCHB.setStyleSheet("font: bold 14px;")
        self.drawBorderCHB.setObjectName("drawBorderCHB")
        self.gridLayout_2.addWidget(self.drawBorderCHB, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setStyleSheet("font: bold 14px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.delayCHB = QtWidgets.QCheckBox(self.groupBox_3)
        self.delayCHB.setStyleSheet("font: bold 14px;")
        self.delayCHB.setObjectName("delayCHB")
        self.gridLayout_2.addWidget(self.delayCHB, 6, 0, 1, 1)
        self.pointBox = QtWidgets.QListWidget(self.groupBox_3)
        self.pointBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: bold 16px;\n"
"border-color: black;")
        self.pointBox.setObjectName("pointBox")
        self.gridLayout_2.addWidget(self.pointBox, 1, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.groupBox_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayout = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.xcrd = QtWidgets.QSpinBox(self.frame_2)
        self.xcrd.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: white;\n"
"font: bold 14px;\n"
"min-width: 10em;\n"
"padding: 4px;")
        self.xcrd.setMinimum(-1000)
        self.xcrd.setMaximum(1000)
        self.xcrd.setObjectName("xcrd")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.xcrd)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.ycrd = QtWidgets.QSpinBox(self.frame_2)
        self.ycrd.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: white;\n"
"font: bold 14px;\n"
"min-width: 10em;\n"
"padding: 4px;")
        self.ycrd.setMinimum(-1000)
        self.ycrd.setMaximum(1000)
        self.ycrd.setObjectName("ycrd")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ycrd)
        self.gridLayout_2.addWidget(self.frame_2, 3, 0, 1, 1)
        self.addPointButt = QtWidgets.QPushButton(self.groupBox_3)
        self.addPointButt.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(113, 0, 0);\n"
"font: bold 16px;")
        self.addPointButt.setObjectName("addPointButt")
        self.gridLayout_2.addWidget(self.addPointButt, 4, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.doButt = QtWidgets.QPushButton(self.frame)
        self.doButt.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(113, 0, 0);\n"
"font: bold 16px;")
        self.doButt.setObjectName("doButt")
        self.verticalLayout_2.addWidget(self.doButt)
        self.lockButt = QtWidgets.QPushButton(self.frame)
        self.lockButt.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgb(50, 0, 0);\n"
"font: bold 16px;")
        self.lockButt.setObjectName("lockButt")
        self.verticalLayout_2.addWidget(self.lockButt)
        self.clearButt = QtWidgets.QPushButton(self.frame)
        self.clearButt.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: bold 16px;")
        self.clearButt.setObjectName("clearButt")
        self.verticalLayout_2.addWidget(self.clearButt)
        self.gridLayout.addWidget(self.frame, 0, 0, 2, 1)
        self.fillFR = QtWidgets.QFrame(self.centralwidget)
        self.fillFR.setAutoFillBackground(False)
        self.fillFR.setStyleSheet("background-color: rgb(29, 29, 29)")
        self.fillFR.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fillFR.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fillFR.setObjectName("fillFR")
        self.gridLayout.addWidget(self.fillFR, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(0, 40))
        self.label_12.setStyleSheet("background-color: rgb(181, 181, 181);\n"
"font: bold 16px;")
        self.label_12.setTextFormat(QtCore.Qt.AutoText)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_11.setText(_translate("MainWindow", "Управление "))
        self.colorCB.setItemText(0, _translate("MainWindow", "Белый"))
        self.colorCB.setItemText(1, _translate("MainWindow", "Красный"))
        self.colorCB.setItemText(2, _translate("MainWindow", "Синий"))
        self.drawBorderCHB.setText(_translate("MainWindow", "Отрисовать границы"))
        self.label.setText(_translate("MainWindow", "Введенные точки "))
        self.delayCHB.setText(_translate("MainWindow", "Выполнить задержку"))
        self.label_2.setText(_translate("MainWindow", "x"))
        self.label_3.setText(_translate("MainWindow", "y"))
        self.addPointButt.setText(_translate("MainWindow", "Добавить точку"))
        self.doButt.setText(_translate("MainWindow", "Выполнить"))
        self.lockButt.setText(_translate("MainWindow", "Замкнуть"))
        self.clearButt.setText(_translate("MainWindow", "Очистить"))
        self.label_12.setText(_translate("MainWindow", "Поле для отрисовки"))

