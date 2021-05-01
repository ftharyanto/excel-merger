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
        MainWindow.resize(543, 185)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioCsv = QtWidgets.QRadioButton(self.centralwidget)
        self.radioCsv.setGeometry(QtCore.QRect(158, 18, 61, 24))
        self.radioCsv.setObjectName("radioCsv")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 104, 401, 55))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.statusProgress = QtWidgets.QLabel(self.layoutWidget)
        self.statusProgress.setText("")
        self.statusProgress.setObjectName("statusProgress")
        self.verticalLayout.addWidget(self.statusProgress)
        self.radioExcel = QtWidgets.QRadioButton(self.centralwidget)
        self.radioExcel.setGeometry(QtCore.QRect(78, 18, 71, 24))
        self.radioExcel.setChecked(True)
        self.radioExcel.setObjectName("radioExcel")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(28, 48, 491, 38))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.browseButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout.addWidget(self.browseButton)
        self.processButton = QtWidgets.QPushButton(self.centralwidget)
        self.processButton.setGeometry(QtCore.QRect(30, 100, 84, 36))
        self.processButton.setObjectName("processButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout_2 = QtWidgets.QAction(MainWindow)
        self.actionAbout_2.setObjectName("actionAbout_2")
        self.actionAbout_3 = QtWidgets.QAction(MainWindow)
        self.actionAbout_3.setObjectName("actionAbout_3")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioCsv.setText(_translate("MainWindow", "CSV"))
        self.radioExcel.setText(_translate("MainWindow", "Excel"))
        self.label.setText(_translate("MainWindow", "Path"))
        self.browseButton.setText(_translate("MainWindow", "..."))
        self.processButton.setText(_translate("MainWindow", "Proses"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout_2.setText(_translate("MainWindow", "About"))
        self.actionAbout_3.setText(_translate("MainWindow", "About"))
