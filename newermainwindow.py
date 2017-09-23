# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from numpy import linspace
from matplotlib.pyplot import cm
import matplotlib.colors as colors
import matplotlib.pyplot as plt

class Ui_flaskManagerUI(object):
    def setupUi(self, flaskManagerUI):
        flaskManagerUI.setObjectName("flaskManagerUI")
        flaskManagerUI.resize(1031, 739)
        self.centralWidget = QtWidgets.QWidget(flaskManagerUI)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.experimentsTreeView = QtWidgets.QTreeView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.experimentsTreeView.sizePolicy().hasHeightForWidth())
        self.experimentsTreeView.setSizePolicy(sizePolicy)
        self.experimentsTreeView.setMinimumSize(QtCore.QSize(100, 0))
        self.experimentsTreeView.setMaximumSize(QtCore.QSize(400, 16777215))

        self.experimentsTreeView.setObjectName("experimentsTreeView")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget.setMaximumSize(QtCore.QSize(4000, 4000))
        self.tabWidget.setObjectName("tabWidget")
        self.sampletab = QtWidgets.QWidget()
        self.sampletab.setObjectName("sampletab")
        #self.matplotspot = QtWidgets.QWidget(self.sampletab)
        self.matplotspot = PlotCanvas(self.sampletab)
        self.matplotspot.setGeometry(QtCore.QRect(10, 10, 581, 621))
        self.matplotspot.setObjectName("matplotspot")
        self.formLayout = QtWidgets.QFormLayout(self.matplotspot)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.tabWidget.addTab(self.sampletab, "Data")
        self.overviewtab = QtWidgets.QWidget()
        self.overviewtab.setObjectName("overviewtab")
        self.dataframespot = QtWidgets.QColumnView(self.overviewtab)
        self.dataframespot.setGeometry(QtCore.QRect(10, 10, 581, 621))
        self.dataframespot.setObjectName("dataframespot")
        self.tabWidget.addTab(self.overviewtab, "Settings")
        self.horizontalLayout.addWidget(self.splitter)
        flaskManagerUI.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(flaskManagerUI)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1031, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        flaskManagerUI.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(flaskManagerUI)
        self.mainToolBar.setObjectName("mainToolBar")
        flaskManagerUI.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(flaskManagerUI)
        self.statusBar.setObjectName("statusBar")
        flaskManagerUI.setStatusBar(self.statusBar)
        self.actionNew = QtWidgets.QAction(flaskManagerUI)
        self.actionNew.setObjectName("actionNew")
        self.actionExport = QtWidgets.QAction(flaskManagerUI)
        self.actionExport.setObjectName("actionExport")
        self.actionSave = QtWidgets.QAction(flaskManagerUI)
        self.actionSave.setObjectName("actionSave")
        self.actionImport = QtWidgets.QAction(flaskManagerUI)
        self.actionImport.setObjectName("actionImport")
        self.actionExit = QtWidgets.QAction(flaskManagerUI)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(flaskManagerUI)
        self.tabWidget.setCurrentIndex(1)
        self.actionExit.triggered.connect(flaskManagerUI.close)
        QtCore.QMetaObject.connectSlotsByName(flaskManagerUI)

    def retranslateUi(self, flaskManagerUI):
        _translate = QtCore.QCoreApplication.translate
        flaskManagerUI.setWindowTitle(_translate("flaskManagerUI", "Flask Manager"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sampletab), _translate("flaskManagerUI", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.overviewtab), _translate("flaskManagerUI", "Tab 2"))
        self.menuFile.setTitle(_translate("flaskManagerUI", "File"))
        self.actionNew.setText(_translate("flaskManagerUI", "New"))
        self.actionExport.setText(_translate("flaskManagerUI", "Export"))
        self.actionSave.setText(_translate("flaskManagerUI", "Save"))
        self.actionImport.setText(_translate("flaskManagerUI", "Import"))
        self.actionExit.setText(_translate("flaskManagerUI", "Exit"))

class MplCanvas(Canvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)


class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.canvas = MplCanvas()


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=7, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)

        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.figure.tight_layout()

    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('Data')
        self.draw()

    def replot(self):
        self.axes.clear()
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('Data')
        self.draw()

    def lineplotter(self, flask, method, experiment, compounds, df):
        self.axes.clear()
        N = len(df.index)
        print("compounds")
        print(compounds)
        time = range(1,len(df[compounds[0]].tolist())+1)
        print(time)
        ax = self.figure.add_subplot(111)

        start = 0.0
        stop = 1.0
        number_of_lines = len(compounds)
        cm_subsection = linspace(start, stop, number_of_lines)

        colors = [cm.rainbow(x) for x in cm_subsection]
        markers = ["o", "v", "^", "s", "p", "*", "D", "+", "X", "8", "."]
        x = 0

        for compound in compounds:
            print(df[compound])
            ax.plot(time, df[compound].tolist(), color=colors[x], marker=markers[x], markersize=10, label=str(compound))  # blue and symbol o
            ax.plot(time, df[compound].tolist(), '-', linewidth=3.0, color=colors[x])
            x+=1
        ax.set_xlabel('Time', fontsize=15)
        ax.set_ylabel('g/L', fontsize=15)
        ax.tick_params(direction="in", labelsize=14, size=5)
        ax.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.5, fontsize=10)
        self.figure.tight_layout()
        self.draw()

    def barplot(self, text, compounds, values):
        self.axes.clear()
        N = len(compounds)
        ind = np.arange(N)
        width = 0.4

        ax = self.figure.add_subplot(111)
        rects = ax.bar(ind + 0.5*width, values, width, color='r')

        ax.set_ylabel('g/L')
        ax.set_title(text)
        ax.set_xticks(ind + width / 2)
        ax.set_xticklabels(compounds)

        for tick in ax.get_xticklabels():
            tick.set_rotation(90)

        self.figure.tight_layout()
        self.draw()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    flaskManagerUI = QtWidgets.QMainWindow()
    ui = Ui_flaskManagerUI()
    ui.setupUi(flaskManagerUI)
    flaskManagerUI.show()
    sys.exit(app.exec_())

