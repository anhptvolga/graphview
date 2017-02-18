#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import graphio

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import networkx as nx

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot


class UiGraphio(QMainWindow):
    """
        Main window for application
    """

    def __init__(self):
        """
        Constructor
        """
        QMainWindow.__init__(self)
        self.ui = graphio.Ui_MainWindow()
        self.ui.setupUi(self)

        self.figure = plt.figure()
        self.ui.graphicsView = FigureCanvasQTAgg(self.figure)
        self.ui.gridLayout.addWidget(self.ui.graphicsView, 0, 1, 1, 1)

        self.graph = nx.MultiDiGraph()

    def add_node(self, label):
        if not self.graph.has_node(label):
            self.graph.add_node(label)
            self.redraw()
            self.add_cb_item(label)

    def add_cb_item(self, label):
        self.ui.cb_nodes.addItem(label)
        self.ui.cb_starting_node.addItem(label)
        self.ui.cb_ending_node.addItem(label)

    def redraw(self):
        self.figure.clf()
        # nx.draw(self.graph, hold=True, with_labels=True)
        nx.draw_circular(self.graph, hold=True, with_labels=True)
        self.ui.graphicsView.draw()

    @pyqtSlot()
    def on_bt_add_node_clicked(self):
        """ Slot when click on Add node button """
        self.add_node(self.ui.cb_nodes.currentText())

    @pyqtSlot()
    def on_bt_del_node_clicked(self):
        """ Slot when click on Delete node button """
        index = self.ui.cb_nodes.currentIndex()
        label = self.ui.cb_nodes.currentText()
        if index > -1 and self.graph.has_node(label):
            self.graph.remove_node(label)
            self.redraw()
            self.ui.cb_nodes.removeItem(index)
            self.ui.cb_starting_node.removeItem(index)
            self.ui.cb_ending_node.removeItem(index)

    @pyqtSlot()
    def on_bt_add_edge_clicked(self):
        """ Slot when click on Add branch button """
        start = self.ui.cb_starting_node.currentText()
        end = self.ui.cb_ending_node.currentText()
        print('adding:', start, end)
        if start and end:
            self.add_cb_item(start)
            self.add_cb_item(end)
            self.graph.add_edge(start, end)
            self.redraw()

    @pyqtSlot()
    def on_bt_del_edge_clicked(self):
        """ Slot when click on Delete branch button """
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UiGraphio()
    window.show()
    sys.exit(app.exec_())
