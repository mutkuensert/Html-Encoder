# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'htmlencoderscreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(879, 783)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEditUnencoded = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEditUnencoded.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEditUnencoded.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEditUnencoded.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.textEditUnencoded.setObjectName("textEditUnencoded")
        self.verticalLayout.addWidget(self.textEditUnencoded)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.encodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.encodeButton.setObjectName("encodeButton")
        self.horizontalLayout.addWidget(self.encodeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textEditEncoded = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEditEncoded.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEditEncoded.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEditEncoded.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.textEditEncoded.setObjectName("textEditEncoded")
        self.verticalLayout.addWidget(self.textEditEncoded)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 879, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HTML Encoder"))
        self.encodeButton.setText(_translate("MainWindow", "Encode"))
