#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, time, os
from PyQt4 import QtGui, QtCore

# Compiled ui classes
from tosUi import Ui_TosWindow

class TosWindow(QtGui.QDialog):
    def __init__(self, callback):
        QtGui.QDialog.__init__(self)

        self.ui=Ui_TosWindow()
        self.ui.setupUi(self)
        self.callback = callback
        self.ui.pushAccept.clicked.connect(self.pushAccept)
        self.ui.pushCancel.clicked.connect(self.pushCancel)

    def show(self):
        QtGui.QDialog.show(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)

    def pushAccept(self):
        self.callback(True)
        self.close()

    def pushCancel(self):
        self.callback(False)
        self.close()