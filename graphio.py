# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphio.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(944, 560)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.toolbox_view = QtWidgets.QToolBox(self.centralwidget)
        self.toolbox_view.setEnabled(True)
        self.toolbox_view.setObjectName("toolbox_view")
        self.page_matrix = QtWidgets.QWidget()
        self.page_matrix.setEnabled(True)
        self.page_matrix.setGeometry(QtCore.QRect(0, 0, 457, 296))
        self.page_matrix.setObjectName("page_matrix")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page_matrix)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tw_adjmatrix = QtWidgets.QTableWidget(self.page_matrix)
        self.tw_adjmatrix.setEnabled(True)
        self.tw_adjmatrix.setMinimumSize(QtCore.QSize(311, 0))
        self.tw_adjmatrix.setMouseTracking(False)
        self.tw_adjmatrix.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tw_adjmatrix.setGridStyle(QtCore.Qt.SolidLine)
        self.tw_adjmatrix.setCornerButtonEnabled(False)
        self.tw_adjmatrix.setRowCount(0)
        self.tw_adjmatrix.setColumnCount(0)
        self.tw_adjmatrix.setObjectName("tw_adjmatrix")
        self.tw_adjmatrix.horizontalHeader().setCascadingSectionResizes(False)
        self.horizontalLayout.addWidget(self.tw_adjmatrix)
        self.toolbox_view.addItem(self.page_matrix, "")
        self.page_incidence = QtWidgets.QWidget()
        self.page_incidence.setGeometry(QtCore.QRect(0, 0, 98, 88))
        self.page_incidence.setObjectName("page_incidence")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page_incidence)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tw_incmatrix = QtWidgets.QTableWidget(self.page_incidence)
        self.tw_incmatrix.setEnabled(True)
        self.tw_incmatrix.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tw_incmatrix.setObjectName("tw_incmatrix")
        self.tw_incmatrix.setColumnCount(0)
        self.tw_incmatrix.setRowCount(0)
        self.horizontalLayout_4.addWidget(self.tw_incmatrix)
        self.toolbox_view.addItem(self.page_incidence, "")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 98, 88))
        self.page.setObjectName("page")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tw_edges = QtWidgets.QTableWidget(self.page)
        self.tw_edges.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tw_edges.setColumnCount(2)
        self.tw_edges.setObjectName("tw_edges")
        self.tw_edges.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_edges.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_edges.setHorizontalHeaderItem(1, item)
        self.tw_edges.horizontalHeader().setCascadingSectionResizes(False)
        self.tw_edges.horizontalHeader().setMinimumSectionSize(40)
        self.tw_edges.horizontalHeader().setSortIndicatorShown(False)
        self.tw_edges.horizontalHeader().setStretchLastSection(False)
        self.tw_edges.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_5.addWidget(self.tw_edges)
        self.toolbox_view.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 457, 296))
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tw_adjlist = QtWidgets.QTableWidget(self.page_2)
        self.tw_adjlist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tw_adjlist.setObjectName("tw_adjlist")
        self.tw_adjlist.setColumnCount(1)
        self.tw_adjlist.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tw_adjlist.setHorizontalHeaderItem(0, item)
        self.tw_adjlist.horizontalHeader().setStretchLastSection(True)
        self.tw_adjlist.verticalHeader().setCascadingSectionResizes(False)
        self.tw_adjlist.verticalHeader().setDefaultSectionSize(30)
        self.tw_adjlist.verticalHeader().setHighlightSections(True)
        self.tw_adjlist.verticalHeader().setMinimumSectionSize(25)
        self.tw_adjlist.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_6.addWidget(self.tw_adjlist)
        self.toolbox_view.addItem(self.page_2, "")
        self.gridLayout.addWidget(self.toolbox_view, 0, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setToolTipDuration(0)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.cb_nodes = QtWidgets.QComboBox(self.tab)
        self.cb_nodes.setToolTipDuration(0)
        self.cb_nodes.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cb_nodes.setEditable(True)
        self.cb_nodes.setObjectName("cb_nodes")
        self.horizontalLayout_2.addWidget(self.cb_nodes)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.bt_add_node = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_add_node.sizePolicy().hasHeightForWidth())
        self.bt_add_node.setSizePolicy(sizePolicy)
        self.bt_add_node.setToolTipDuration(0)
        self.bt_add_node.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bt_add_node.setObjectName("bt_add_node")
        self.horizontalLayout_2.addWidget(self.bt_add_node)
        self.bt_del_node = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_del_node.sizePolicy().hasHeightForWidth())
        self.bt_del_node.setSizePolicy(sizePolicy)
        self.bt_del_node.setToolTipDuration(0)
        self.bt_del_node.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bt_del_node.setObjectName("bt_del_node")
        self.horizontalLayout_2.addWidget(self.bt_del_node)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.cb_starting_node = QtWidgets.QComboBox(self.tab_2)
        self.cb_starting_node.setEditable(True)
        self.cb_starting_node.setObjectName("cb_starting_node")
        self.horizontalLayout_3.addWidget(self.cb_starting_node)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.cb_ending_node = QtWidgets.QComboBox(self.tab_2)
        self.cb_ending_node.setEditable(True)
        self.cb_ending_node.setObjectName("cb_ending_node")
        self.horizontalLayout_3.addWidget(self.cb_ending_node)
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.sb_weight_edge = QtWidgets.QSpinBox(self.tab_2)
        self.sb_weight_edge.setMinimum(1)
        self.sb_weight_edge.setObjectName("sb_weight_edge")
        self.horizontalLayout_3.addWidget(self.sb_weight_edge)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.bt_add_edge = QtWidgets.QPushButton(self.tab_2)
        self.bt_add_edge.setObjectName("bt_add_edge")
        self.horizontalLayout_3.addWidget(self.bt_add_edge)
        self.bt_del_edge = QtWidgets.QPushButton(self.tab_2)
        self.bt_del_edge.setObjectName("bt_del_edge")
        self.horizontalLayout_3.addWidget(self.bt_del_edge)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 3)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolbox_view.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tw_adjmatrix.setSortingEnabled(False)
        self.toolbox_view.setItemText(self.toolbox_view.indexOf(self.page_matrix), _translate("MainWindow", "Adjacency matrix"))
        self.toolbox_view.setItemText(self.toolbox_view.indexOf(self.page_incidence), _translate("MainWindow", "Incidence matrix"))
        item = self.tw_edges.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "r"))
        item = self.tw_edges.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "t"))
        self.toolbox_view.setItemText(self.toolbox_view.indexOf(self.page), _translate("MainWindow", "List of edges"))
        item = self.tw_adjlist.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Node adjacenct to"))
        self.toolbox_view.setItemText(self.toolbox_view.indexOf(self.page_2), _translate("MainWindow", "Adjacency list"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.bt_add_node.setText(_translate("MainWindow", "Add"))
        self.bt_del_node.setText(_translate("MainWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Node"))
        self.label_2.setText(_translate("MainWindow", "Start node"))
        self.label_3.setText(_translate("MainWindow", "End node"))
        self.label_4.setText(_translate("MainWindow", "Weight"))
        self.bt_add_edge.setText(_translate("MainWindow", "Add"))
        self.bt_del_edge.setText(_translate("MainWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Edge"))

