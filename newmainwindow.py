# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_flaskManagerUI(object):
    def setupUi(self, flaskManagerUI):
        flaskManagerUI.setObjectName("flaskManagerUI")
        flaskManagerUI.resize(653, 422)
        self.centralWidget = QtWidgets.QWidget(flaskManagerUI)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.experimentsTreeView = QtWidgets.QTreeView(self.splitter)
        self.experimentsTreeView.setMinimumSize(QtCore.QSize(100, 0))
        self.experimentsTreeView.setMaximumSize(QtCore.QSize(20000, 16777215))

        self.experimentsTreeView.setObjectName("experimentsTreeView")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget.setObjectName("tabWidget")
        self.sampletab = QtWidgets.QWidget()
        self.sampletab.setObjectName("sampletab")
        self.formWidget = QtWidgets.QWidget(self.sampletab)
        self.formWidget.setGeometry(QtCore.QRect(10, 10, 160, 301))
        self.formWidget.setObjectName("formWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formWidget)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.columnView = QtWidgets.QColumnView(self.formWidget)
        self.columnView.setObjectName("columnView")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.columnView)
        self.tabWidget.addTab(self.sampletab, "")
        self.overviewtab = QtWidgets.QWidget()
        self.overviewtab.setObjectName("overviewtab")
        self.columnView_2 = QtWidgets.QColumnView(self.overviewtab)
        self.columnView_2.setGeometry(QtCore.QRect(10, 10, 161, 311))
        self.columnView_2.setObjectName("columnView_2")
        self.tabWidget.addTab(self.overviewtab, "")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        flaskManagerUI.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(flaskManagerUI)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 653, 21))
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
        self.tabWidget.setCurrentIndex(0)
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    flaskManagerUI = QtWidgets.QMainWindow()
    ui = Ui_flaskManagerUI()
    ui.setupUi(flaskManagerUI)
    flaskManagerUI.show()
    sys.exit(app.exec_())

