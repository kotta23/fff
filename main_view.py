# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_view.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(756, 415)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.browseFile1Lin = QtWidgets.QLineEdit(self.centralwidget)
        self.browseFile1Lin.setObjectName("browseFile1Lin")
        self.gridLayout.addWidget(self.browseFile1Lin, 0, 1, 2, 1)
        self.browseFile1Btn = QtWidgets.QPushButton(self.centralwidget)
        self.browseFile1Btn.setObjectName("browseFile1Btn")
        self.gridLayout.addWidget(self.browseFile1Btn, 0, 2, 2, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 2, 1)
        self.browseFile2Lin = QtWidgets.QLineEdit(self.centralwidget)
        self.browseFile2Lin.setObjectName("browseFile2Lin")
        self.gridLayout.addWidget(self.browseFile2Lin, 2, 1, 1, 1)
        self.browseFile2Btn = QtWidgets.QPushButton(self.centralwidget)
        self.browseFile2Btn.setObjectName("browseFile2Btn")
        self.gridLayout.addWidget(self.browseFile2Btn, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.getDiffBtn = QtWidgets.QPushButton(self.centralwidget)
        self.getDiffBtn.setObjectName("getDiffBtn")
        self.horizontalLayout.addWidget(self.getDiffBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.file1MemTable = QtWidgets.QTableWidget(self.centralwidget)
        self.file1MemTable.setMaximumSize(QtCore.QSize(3000, 16777215))
        self.file1MemTable.setObjectName("file1MemTable")
        self.file1MemTable.setColumnCount(17)
        self.file1MemTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.file1MemTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.file1MemTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.file1MemTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.file1MemTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.file1MemTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.file1MemTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.file1MemTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.file1MemTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.file1MemTable.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.file1MemTable.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.file1MemTable.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.file1MemTable.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.file1MemTable.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.file1MemTable.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.file1MemTable.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.file1MemTable.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.file1MemTable.setHorizontalHeaderItem(16, item)
        self.file1MemTable.horizontalHeader().setVisible(True)
        self.file1MemTable.horizontalHeader().setCascadingSectionResizes(False)
        self.file1MemTable.horizontalHeader().setDefaultSectionSize(40)
        self.file1MemTable.horizontalHeader().setHighlightSections(True)
        self.file1MemTable.horizontalHeader().setSortIndicatorShown(False)
        self.file1MemTable.horizontalHeader().setStretchLastSection(False)
        self.file1MemTable.verticalHeader().setVisible(True)
        self.file1MemTable.verticalHeader().setCascadingSectionResizes(False)
        self.file1MemTable.verticalHeader().setHighlightSections(True)
        self.file1MemTable.verticalHeader().setSortIndicatorShown(False)
        self.file1MemTable.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_2.addWidget(self.file1MemTable)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.save_edite = QtWidgets.QPushButton(self.centralwidget)
        self.save_edite.setObjectName("save_edite")
        self.horizontalLayout_3.addWidget(self.save_edite)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.merge_f1_to_f2 = QtWidgets.QPushButton(self.centralwidget)
        self.merge_f1_to_f2.setObjectName("merge_f1_to_f2")
        self.horizontalLayout_3.addWidget(self.merge_f1_to_f2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 756, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "File 1:"))
        self.browseFile1Btn.setText(_translate("MainWindow", "browse"))
        self.label_2.setText(_translate("MainWindow", "File 2:"))
        self.browseFile2Btn.setText(_translate("MainWindow", "browse"))
        self.getDiffBtn.setText(_translate("MainWindow", "Get Difference"))
        item = self.file1MemTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "0"))
        item = self.file1MemTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "1"))
        item = self.file1MemTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "2"))
        item = self.file1MemTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "3"))
        item = self.file1MemTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "4"))
        item = self.file1MemTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "5"))
        item = self.file1MemTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "6"))
        item = self.file1MemTable.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "7"))
        item = self.file1MemTable.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "__"))
        item = self.file1MemTable.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "0"))
        item = self.file1MemTable.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "1"))
        item = self.file1MemTable.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "2"))
        item = self.file1MemTable.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "3"))
        item = self.file1MemTable.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "4"))
        item = self.file1MemTable.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "5"))
        item = self.file1MemTable.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "6"))
        item = self.file1MemTable.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "7"))
        self.save_edite.setText(_translate("MainWindow", "Save Edit on f-2"))
        self.merge_f1_to_f2.setText(_translate("MainWindow", "Merge & save f-1 to f-2"))
