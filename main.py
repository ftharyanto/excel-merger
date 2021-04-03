from PyQt5 import QtWidgets, QtCore, QtGui, uic
from PyQt5.QtWidgets import QMessageBox
import pandas as pd
import sys, os

qtCreatorFile = "gui_linux.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class ExcelProcessor(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):

        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        # Required by Qt5 to initialize the UI
        self.setupUi(self)

        # Set the title for the app
        self.setWindowTitle("Excel Processor")

        self.browseButton.clicked.connect(self.openFileNameDialog)
        self.processButton.clicked.connect(self.mergeExcelFiles)

    def mergeExcelFiles(self):
        if self.lineEdit.text() == '':
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Silakan isi direktori")
            msgBox.setWindowTitle("Pemberitahuan")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()

        cwd = self.lineEdit.text()
        files = os.listdir(cwd)
        files.sort()
        total_data = len(files)
        counter = 0

        df = pd.DataFrame()
        self.statusProgress.setText('Processing...')
        for i in range(total_data):
            if files[i].endswith('.xlsx') and not files[i].startswith('merged'):
                df = df.append(pd.read_excel(files[i]), ignore_index=True)
            counter = counter + (i+1)/total_data * 100
            self.progressBar.setValue(counter)

        df.to_excel('merged.xlsx')
        self.statusProgress.setText('Finished')
        self.progressBar.setValue(100)

    def openFileNameDialog(self):
        path = QtWidgets.QFileDialog.getExistingDirectory()
        self.lineEdit.setText('{}'.format(path))

def main(argv):
    # create Qt application
    app = QtWidgets.QApplication(argv)

    # create main window
    wnd = ExcelProcessor()
    
    # Move the app window to upper left
    wnd.move(100,100)
    wnd.show()

    # run!
    retval = app.exec_()

    # exit
    sys.exit(retval)


if __name__ == "__main__":
    main(sys.argv)
