from PyQt5 import QtCore, QtWidgets
import pandas
from PyQt5.QtCore import (QAbstractItemModel, QFile, QIODevice,
        QItemSelectionModel, QModelIndex, Qt, QMimeType)
from PyQt5.QtWidgets import QApplication, QMainWindow

import hplcextractor

class TreeItem(object):
    def __init__(self, data, parent=None):
        self.parentItem = parent
        self.itemData = data
        self.childItems = []

    def child(self, row):
        return self.childItems[row]

    def childCount(self):
        return len(self.childItems)

    def childNumber(self):
        if self.parentItem != None:
            return self.parentItem.childItems.index(self)
        return 0

    def columnCount(self):
        return len(self.itemData)

    def data(self, column):
        return self.itemData[column]

    def insertChildren(self, position, count, columns):
        if position < 0 or position > len(self.childItems):
            return False

        for row in range(count):
            data = [None for v in range(columns)]
            item = TreeItem(data, self)
            self.childItems.insert(position, item)

        return True

    def insertColumns(self, position, columns):
        if position < 0 or position > len(self.itemData):
            return False

        for column in range(columns):
            self.itemData.insert(position, None)

        for child in self.childItems:
            child.insertColumns(position, columns)

        return True

    def parent(self):
        return self.parentItem

    def removeChildren(self, position, count):
        if position < 0 or position + count > len(self.childItems):
            return False

        for row in range(count):
            self.childItems.pop(position)

        return True

    def removeColumns(self, position, columns):
        if position < 0 or position + columns > len(self.itemData):
            return False

        for column in range(columns):
            self.itemData.pop(position)

        for child in self.childItems:
            child.removeColumns(position, columns)

        return True

    def setData(self, column, value):
        if column < 0 or column >= len(self.itemData):
            return False

        self.itemData[column] = value

        return True


class TreeModel(QAbstractItemModel):
    def __init__(self, headers, data, parent=None):
        super(TreeModel, self).__init__(parent)
        self.rootItem = TreeItem(headers)
        parents = [self.rootItem]
        self.dftotree(data, self.rootItem)

    def columnCount(self, parent=QModelIndex()):
        return self.rootItem.columnCount()

    def iterItems(self, root):
        if root is not None:
            stack = [root]
            while stack:
                parent = stack.pop(0)
                for row in range(parent.model().rowCount()):
                    for column in range(parent.model(). columnCount()):
                        child = parent.child(row, column)
                        yield child
                        if child.hasChildren():
                            stack.append(child)

    def data(self, index, role):
        if not index.isValid():
            return None

        if role != Qt.DisplayRole and role != Qt.EditRole:
            return None

        item = self.getItem(index)
        #return item.data
        return item.data(index.column())

    def itemDepth(self, index):
        if not index.isValid():
            return 0

        childItem = self.getItem(index)
        parentItem = childItem.parent()

        depth = 1

        if parentItem == self.rootItem:
            return 1

        else:
            depth+=self.itemDepth(index.parent())
            return depth

    def flags(self, index):
        if not index.isValid():
            return 0 | QtCore.Qt.ItemIsEnabled

        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled

    def getItem(self, index):
        if index.isValid():
            item = index.internalPointer()
            if item:
                return item

        return self.rootItem

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.rootItem.data(section)

        return None

    def index(self, row, column, parent=QModelIndex()):
        if parent.isValid() and parent.column() != 0:
            return QModelIndex()

        parentItem = self.getItem(parent)
        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QModelIndex()

    def insertColumns(self, position, columns, parent=QModelIndex()):
        self.beginInsertColumns(parent, position, position + columns - 1)
        success = self.rootItem.insertColumns(position, columns)
        self.endInsertColumns()

        return success

    def insertRows(self, position, rows, parent=QModelIndex()):
        parentItem = self.getItem(parent)
        self.beginInsertRows(parent, position, position + rows - 1)
        success = parentItem.insertChildren(position, rows,
                self.rootItem.columnCount())
        self.endInsertRows()

        return success

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()

        childItem = self.getItem(index)
        parentItem = childItem.parent()

        if parentItem == self.rootItem:
            return QModelIndex()

        return self.createIndex(parentItem.childNumber(), 0, parentItem)

    def removeColumns(self, position, columns, parent=QModelIndex()):
        self.beginRemoveColumns(parent, position, position + columns - 1)
        success = self.rootItem.removeColumns(position, columns)
        self.endRemoveColumns()

        if self.rootItem.columnCount() == 0:
            self.removeRows(0, self.rowCount())

        return success

    def removeRows(self, position, rows, parent=QModelIndex()):
        parentItem = self.getItem(parent)

        self.beginRemoveRows(parent, position, position + rows - 1)
        success = parentItem.removeChildren(position, rows)
        self.endRemoveRows()

        return success

    def rowCount(self, parent=QModelIndex()):
        parentItem = self.getItem(parent)

        return parentItem.childCount()

    def setData(self, index, value, role=Qt.EditRole):
        if role != Qt.EditRole:
            return False

        item = self.getItem(index)
        result = item.setData(index.column(), value)

        if result:
            self.dataChanged.emit(index, index)

        return result

    def setHeaderData(self, section, orientation, value, role=Qt.EditRole):
        if role != Qt.EditRole or orientation != Qt.Horizontal:
            return False

        result = self.rootItem.setData(section, value)
        if result:
            self.headerDataChanged.emit(orientation, section, section)

        return result

    def mimeTypes(self):
        return ['text/xml']

    def mimeData(self, indexes):
        mimedata = QtCore.QMimeData()
        mimedata.setData('text/xml', 'mimeData')
        return mimedata

    def dropMimeData(self, data, action, row, column, parent):
        print("dropMimeData(%s %s %s %s" % (data.data('text/xml'), action, row, parent))
        return True

    def supportedDropActions(self):
        return QtCore.Qt.CopyAction | QtCore.Qt.MoveAction

    def dftotree(self, df, parent = None):

        self.parent = parent
        parents = []

        for frame in df:
            print(frame.mainmethodframe['experiment'].unique())
            experiments = frame.mainmethodframe['experiment'].unique()

            for experiment in experiments:
                self.parent = self.rootItem
                methodcount = 0
                flaskcount = 0
                self.parent.insertChildren(self.parent.childCount(), 1, 1)
                self.parent.child(self.parent.childCount() - 1).setData(0, "Experiment: " + str(experiment))
                parents.append(self.parent.child(self.parent.childCount() - 1))
                self.parent = parents[-1]
                methods = frame.mainmethodframe[frame.mainmethodframe['experiment'] == experiment]['method'].unique()

                for method in methods:
                    methodcount+=1
                    self.parent = parents[-flaskcount-methodcount]
                    self.parent.insertChildren(self.parent.childCount(), 1, 1)
                    self.parent.child(self.parent.childCount() - 1).setData(0, "Method: " + str(method))
                    parents.append(self.parent.child(self.parent.childCount() - 1))
                    self.parent = parents[-1]
                    flasks = frame.mainmethodframe[frame.mainmethodframe['experiment'] == experiment][frame.mainmethodframe['method'] == method]['flask'].unique()

                    for flask in flasks:
                        flaskcount+=1
                        self.parent = parents[-flaskcount]
                        self.parent.insertChildren(self.parent.childCount(), 1, 1)
                        self.parent.child(self.parent.childCount() - 1).setData(0, "Flask: " + str(flask))
                        parents.append(self.parent.child(self.parent.childCount() - 1))
                        self.parent = parents[-1]
                        samples = list(frame.mainmethodframe[frame.mainmethodframe['experiment'] == experiment][frame.mainmethodframe['method'] == method][frame.mainmethodframe['flask'] == flask]['sample'].index)

                        for sample in samples:
                            self.parent.insertChildren(self.parent.childCount(), 1, 1)
                            self.parent.child(self.parent.childCount() - 1).setData(0, str(sample))
                            #parents.append(self.parent.child(self.parent.childCount() - 1))
                            #self.parent = parents[-1]