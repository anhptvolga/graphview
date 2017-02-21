#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import graphio
from pygraphviz import AGraph
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap


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

        self.scene_graph = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene_graph)
        self.ui.graphicsView.update()

        self.graph = AGraph(strict=False, directed=True)
        self.graph.layout(prog='dot')

    def add_cb_item(self, label):
        n = self.ui.cb_nodes.count()
        i = 0
        while i < n:
            itext = self.ui.cb_nodes.itemText(i)
            if label == itext:
                return
            elif label < itext:
                break
            i += 1
        # insert item to lists
        self.ui.cb_nodes.insertItem(i, label)
        self.ui.cb_starting_node.insertItem(i, label)
        self.ui.cb_ending_node.insertItem(i, label)

    def reset_combo_boxes(self):
        self.ui.cb_nodes.clearEditText()
        self.ui.cb_starting_node.clearEditText()
        self.ui.cb_ending_node.clearEditText()

    def redraw(self):
        self.graph.draw('graph', 'png', 'dot')
        self.scene_graph.clear()
        self.scene_graph.addItem(QGraphicsPixmapItem(QPixmap('graph')))
        self.ui.graphicsView.update()

    @pyqtSlot()
    def on_bt_add_node_clicked(self):
        """ Slot when click on Add node button """
        label = self.ui.cb_nodes.currentText()
        if not self.graph.has_node(label):
            self.add_cb_item(label)
            self.graph.add_node(label)
            self.redraw()
        self.reset_combo_boxes()

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
        self.reset_combo_boxes()

    @pyqtSlot()
    def on_bt_add_edge_clicked(self):
        """ Slot when click on Add branch button """
        start = self.ui.cb_starting_node.currentText()
        end = self.ui.cb_ending_node.currentText()
        weight = self.ui.sb_weight_edge.value()
        if start and end:
            self.add_cb_item(start)
            self.add_cb_item(end)
            self.graph.add_edge(start, end, label=weight)
            self.redraw()
        self.reset_combo_boxes()

    @pyqtSlot()
    def on_bt_del_edge_clicked(self):
        """ Slot when click on Delete branch button """
        start = self.ui.cb_starting_node.currentText()
        end = self.ui.cb_ending_node.currentText()
        weight = self.ui.sb_weight_edge.value()
        if start and end:
            self.graph.remove_edge(start, end, weight)
            self.redraw()
        self.reset_combo_boxes()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UiGraphio()
    window.show()
    sys.exit(app.exec_())
