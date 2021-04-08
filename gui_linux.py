# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_linux.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 173)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(MainWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 40, 491, 38))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.browseButton = QtWidgets.QPushButton(self.layoutWidget)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout.addWidget(self.browseButton)
        self.processButton = QtWidgets.QPushButton(MainWindow)
        self.processButton.setGeometry(QtCore.QRect(32, 92, 84, 36))
        self.processButton.setObjectName("processButton")
        self.layoutWidget1 = QtWidgets.QWidget(MainWindow)
        self.layoutWidget1.setGeometry(QtCore.QRect(122, 96, 401, 55))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget1)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.statusProgress = QtWidgets.QLabel(self.layoutWidget1)
        self.statusProgress.setText("")
        self.statusProgress.setObjectName("statusProgress")
        self.verticalLayout.addWidget(self.statusProgress)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dialog"))
        self.label.setText(_translate("MainWindow", "Path"))
        self.browseButton.setText(_translate("MainWindow", "..."))
        self.processButton.setText(_translate("MainWindow", "Proses"))
