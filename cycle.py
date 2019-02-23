import sys
import os
import glob
import gui_cycle
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pytdx.reader import TdxDailyBarReader, TdxFileNotFoundException
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class circle(QMainWindow, gui_cycle.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.sys_init()

    def sys_init(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.verticalLayout.addWidget(self.canvas)

        self.lineEdit.editingFinished.connect(self.editFinished)
        self.dateEdit_start.dateChanged.connect(self.dateChanged)
        self.dateEdit_end.dateChanged.connect(self.dateChanged)
        self.verticalSlider.valueChanged.connect(self.sliderChanged)
        self.spinBox.valueChanged.connect(self.spinChanged)
        self.checkBoxRev.toggled.connect(self.reverseChanged)
        self.checkBoxLog.toggled.connect(self.logChanged)

        paths = []
        with open("./_path") as f:
            for line in f.readlines():
                if "/" in line:
                    paths.append(line.strip('\r\n \t'))

        # 搜索文件列表
        self.tickers = []
        for path in paths:
            if not path.endswith('/'):
                path += "/"
            for name in glob.glob(path + '*.day'):
                self.tickers.append(name)
        # 自动补全
        items_list = [os.path.splitext(os.path.basename(t))[0] for t in self.tickers]
        completer = QCompleter(items_list)
        completer.activated.connect(self.completerActivated)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)
        self.lineEdit.setCompleter(completer)

        self.file = "./sh000000.day"
        self.read_file()

    def read_file(self):
        # 读取数据
        # print ("read_file, {}".format(self.file))
        reader = TdxDailyBarReader()
        self.df = reader.get_df(self.file)
        # print (self.df.index)

        # 更新UI
        self.lineEdit.setText(os.path.splitext(os.path.basename(self.file))[0])
        # 初始化日期
        start = self.df.index[0]
        end = self.df.index[-1]
        self.dateEdit_start.setDate(start)
        self.dateEdit_start.setMinimumDate(start)
        self.dateEdit_start.setMaximumDate(end)
        self.dateEdit_end.setDate(end)
        self.dateEdit_end.setMinimumDate(start)
        self.dateEdit_end.setMaximumDate(end)
        # print ("read_file end, {}, {}".format(start, end))
        self.read_ticker(start, end)

    def read_ticker(self, start, end):
        # 读取指定日期的收盘数据
        # close = self.df['close']
        close = self.df.loc[start:end, 'close']  # 取出start至end之间的close
        self.c = np.array(close)
        self.lenc = len(self.c)

        # 图形显示用相关处理
        minmax = self.c.min()+self.c.max()
        self.ticks = [self.c.min(), minmax * 0.5, self.c.max()]
        self.tickslabel = [self.c.min(), '', self.c.max()]

        self.spinBox.setValue(360)
        self.checkBoxRev.setChecked(False)
        self.checkBoxLog.setChecked(False)

        self.theta = 1
        self.direction = 1
        self.log = False
        self.canvasrefresh()

    def canvasrefresh(self):
        # 计算周期数, 即 self.c 绕一圈的K线个数
        self.label.setText("Cycle:{:0.1f}".format(self.lenc/self.theta))

        # 画图
        self.figure.clear()
        ax = self.figure.add_subplot(111, projection='polar')
        ax.set_yticks(self.ticks, minor=False)
        ax.set_yticklabels(self.tickslabel, minor=False)
        ax.set_theta_direction(self.direction)
        ax.grid('tight', ls='--')
        r = np.linspace(0, self.theta * 2 * np.pi, self.lenc)

        # 彩色显示不同的圈
        for i in range(10):
            if (i > self.theta):
                break
            j = np.where((r >= i*2*np.pi) & (r < (i+1)*2*np.pi))
            # print ("i={}, j={}".format(i,j[0]))
            # ax.plot(r[j[0][0]: j[0][-1]], self.c[j[0][0]: j[0][-1]], alpha=0.5)
            if (self.log):
                ax.plot(r[j[0][0]: j[0][-1]], np.log(self.c[j[0][0]: j[0][-1]]), alpha=0.5)
            else:
                ax.plot(r[j[0][0]: j[0][-1]], self.c[j[0][0]: j[0][-1]], alpha=0.5)

        # 显示
        # ax.plot(r, self.c, alpha=0.5)
        self.canvas.draw()

    def tickerChoosed(self):
        file_back = self.file
        try:
            name = self.lineEdit.text()
            for t in self.tickers:
                if name == os.path.splitext(os.path.basename(t))[0]:
                    self.file = t
                    break
        except:
            self.file = file_back
        finally:
            self.read_file()

    def completerActivated(self):
        self.tickerChoosed()

    def editFinished(self):
        self.tickerChoosed()

    def dateChanged(self):
        start = self.dateEdit_start.date().toString("yyyy-MM-dd")
        end = self.dateEdit_end.date().toString("yyyy-MM-dd")
        self.read_ticker(start, end)

    def sliderChanged(self):
        value = self.verticalSlider.value()
        self.spinBox.setValue(value)
        self.theta = value / 360
        self.canvasrefresh()

    def spinChanged(self):
        value = self.spinBox.value()
        if (value !=  self.verticalSlider.value()):
            self.verticalSlider.setValue(value)

    def wheelEvent(self, event):
        numDegrees = event.angleDelta().y()
        value = self.verticalSlider.value()
        if numDegrees > 0:
            value += 10*self.direction
        else:
            value -= 10*self.direction
        self.verticalSlider.setValue(value)

    def reverseChanged(self):
        if self.direction == 1:
            self.direction = -1
            self.verticalSlider.setInvertedAppearance(True)
            self.verticalSlider.setInvertedControls(True)
        else:
            self.direction = 1
            self.verticalSlider.setInvertedAppearance(False)
            self.verticalSlider.setInvertedControls(False)
        self.canvasrefresh()

    def logChanged(self):
        self.log = self.checkBoxLog.checkState()
        self.canvasrefresh()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui_action = circle()
    gui_action.show()
    sys.exit(app.exec_())