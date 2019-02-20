# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_cycle.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("simplistica/png/64x64/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widgetPic = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetPic.sizePolicy().hasHeightForWidth())
        self.widgetPic.setSizePolicy(sizePolicy)
        self.widgetPic.setObjectName("widgetPic")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widgetPic)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addWidget(self.widgetPic, 1, 0, 1, 1)
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setMinimum(360)
        self.verticalSlider.setMaximum(3600)
        self.verticalSlider.setSingleStep(1)
        self.verticalSlider.setPageStep(90)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setInvertedAppearance(False)
        self.verticalSlider.setInvertedControls(False)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout.addWidget(self.verticalSlider, 1, 1, 1, 1)
        self.widgetChoose = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetChoose.sizePolicy().hasHeightForWidth())
        self.widgetChoose.setSizePolicy(sizePolicy)
        self.widgetChoose.setObjectName("widgetChoose")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widgetChoose)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widgetChoose)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.dateEdit_start = QtWidgets.QDateEdit(self.widgetChoose)
        self.dateEdit_start.setCalendarPopup(True)
        self.dateEdit_start.setObjectName("dateEdit_start")
        self.horizontalLayout.addWidget(self.dateEdit_start)
        self.dateEdit_end = QtWidgets.QDateEdit(self.widgetChoose)
        self.dateEdit_end.setCalendarPopup(True)
        self.dateEdit_end.setObjectName("dateEdit_end")
        self.horizontalLayout.addWidget(self.dateEdit_end)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.checkBoxLog = QtWidgets.QCheckBox(self.widgetChoose)
        self.checkBoxLog.setObjectName("checkBoxLog")
        self.horizontalLayout.addWidget(self.checkBoxLog)
        self.checkBoxRev = QtWidgets.QCheckBox(self.widgetChoose)
        self.checkBoxRev.setObjectName("checkBoxRev")
        self.horizontalLayout.addWidget(self.checkBoxRev)
        self.label = QtWidgets.QLabel(self.widgetChoose)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.widgetChoose)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.spinBox = QtWidgets.QSpinBox(self.widgetChoose)
        self.spinBox.setMinimum(360)
        self.spinBox.setMaximum(3600)
        self.spinBox.setSingleStep(1)
        self.spinBox.setDisplayIntegerBase(10)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.gridLayout.addWidget(self.widgetChoose, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionData = QtWidgets.QAction(MainWindow)
        self.actionData.setObjectName("actionData")
        self.actionBlocks = QtWidgets.QAction(MainWindow)
        self.actionBlocks.setObjectName("actionBlocks")
        self.actionStickers = QtWidgets.QAction(MainWindow)
        self.actionStickers.setObjectName("actionStickers")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cycle Check"))
        self.checkBoxLog.setText(_translate("MainWindow", "Log"))
        self.checkBoxRev.setText(_translate("MainWindow", "Reverse"))
        self.label.setText(_translate("MainWindow", "Cycle:"))
        self.actionData.setText(_translate("MainWindow", "Download Data"))
        self.actionBlocks.setText(_translate("MainWindow", "Refresh Blocks"))
        self.actionStickers.setText(_translate("MainWindow", "Refresh Stickers"))
        self.actionOpen.setText(_translate("MainWindow", "Open File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

