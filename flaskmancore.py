__author__ = 'Stephan'

import PyQt5, sys, newermainwindow, hplcextractor, treemodel
from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
import pandas


class flaskManagerUI(PyQt5.QtWidgets.QMainWindow, newermainwindow.Ui_flaskManagerUI):

    def test(self):
        print("woah")

    def __init__(self, parent=None):
        super(flaskManagerUI, self).__init__(parent)
        self.setupUi(self)

        self.actionImport.triggered.connect(self.importer)
        self.actionExport.triggered.connect(self.exporter)

        self.experimentsTreeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.experimentsTreeView.customContextMenuRequested.connect(self.openMenu)
        headers = ["Data"]

        importeddata = hplcextractor.extract(str(QFileDialog.getExistingDirectory(self, "Select Directory")))
        global data
        data = importeddata
        self.expTreeModel = treemodel.TreeModel(headers, importeddata)
        print(importeddata)
        self.experimentsTreeView.setSelectionMode(self.experimentsTreeView.ExtendedSelection)
        self.experimentsTreeView.setModel(self.expTreeModel)
        self.experimentsTreeView.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.experimentsTreeView.doubleClicked.connect(self.graphdata)
        self.experimentsTreeView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.setStyleSheet("QTreeView::branch:has-siblings:!adjoins-item {\n"
        "    border-image: url(stylesheet-vline.png) 0;\n"
        "}\n"
        "\n"
        "QTreeView::branch:has-siblings:adjoins-item {\n"
        "    border-image: url(stylesheet-branch-more.png) 0;\n"
        "}\n"
        "\n"
        "QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
        "    border-image: url(stylesheet-branch-end.png) 0;\n"
        "}\n"
        "\n"
        "QTreeView::branch:has-children:!has-siblings:closed,\n"
        "QTreeView::branch:closed:has-children:has-siblings {\n"
        "        border-image: none;\n"
        "        image: url(stylesheet-branch-closed.png);\n"
        "}\n"
        "\n"
        "QTreeView::branch:open:has-children:!has-siblings,\n"
        "QTreeView::branch:open:has-children:has-siblings  {\n"
        "        border-image: none;\n"
        "        image: url(stylesheet-branch-open.png);\n"
        "}")



    def importer(self):
        datapoints = hplcextractor.extract(str(QFileDialog.getExistingDirectory(self, "Select Directory")))
        self.expTreeModel.import2Tree(datapoints)

    def openMenu(self, position):
        menu = QMenu()
        menu.addAction(self.tr("New Experiment")).triggered.connect(self.newExperiment)
        menu.exec_(self.experimentsTreeView.viewport().mapToGlobal(position))

    def exporter(self):
        print("exporting")

    def newExperiment(self):
        self.expTreeModel.newExperiment("DK")

    def graphdata(self, index):
        text = index.model().data(index, role=Qt.DisplayRole)
        depth = index.model().itemDepth(index)

        if depth==1:
            #whole experiment
            print(text[12:])
            self.matplotspot.replot()

        if depth==2:
            #whole method
            print(text[8:])

        if depth==3:
            #one flask

            method = index.parent()
            experiment = method.parent()
            flasktext = text[7:]
            methodtext = method.model().data(method, role=Qt.DisplayRole)[8:]
            experimenttext = experiment.model().data(experiment, role=Qt.DisplayRole)[12:]

            try: flasktext = int(flasktext)
            except: pass

            for frame in data:
                if frame.name == methodtext:
                    compounds = list(frame.mainmethodframe.columns[4:])
                    df = frame.mainmethodframe[frame.mainmethodframe['experiment'] == experimenttext][frame.mainmethodframe['method'] == methodtext][frame.mainmethodframe['flask'] == flasktext]
                    print(df)
                    self.matplotspot.lineplotter(flasktext, methodtext, experimenttext, compounds, df)


        if depth==4:
            #one sample

            flask = index.parent()
            method = flask.parent()
            experiment = method.parent()

            flasktext = flask.model().data(flask, role=Qt.DisplayRole)[7:]
            methodtext = method.model().data(method, role=Qt.DisplayRole)[8:]
            experimenttext = experiment.model().data(experiment, role=Qt.DisplayRole)[12:]

            for frame in data:
                if frame.name == methodtext:
                    compounds = list(frame.mainmethodframe.columns[4:])
                    values = frame.mainmethodframe.loc[text].tolist()[4:]
                    self.matplotspot.barplot(text, compounds, values)

    def sampleplotter(self):
        return



def main():
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    form = flaskManagerUI()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()


def imp(dir):
    print(dir)
