#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    from PyQt5.QtWidgets import QApplication, QMainWindow
    from PyQt5.QtCore import pyqtSlot
except:


import graphio


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

    @pyqtSlot()
    def on_bt_add_node_clicked(self):
        """ Slot when click on Add node button """
        print("add node worked")

    @pyqtSlot()
    def on_bt_del_node_clicked(self):
        """ Slot when click on Delete node button """
        pass

    @pyqtSlot()
    def on_bt_add_branch_clicked(self):
        """ Slot when click on Add branch button """
        pass

    @pyqtSlot()
    def on_bt_del_branch_clicked(self):
        """ Slot when click on Delete branch button """
        pass


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = UiGraphio()
    window.show()
    sys.exit(app.exec_())
