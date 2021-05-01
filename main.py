from PyQt5 import QtWidgets, QtCore, QtGui, uic
from PyQt5.QtWidgets import QMessageBox
import pandas as pd
import sys, os

# set status to dev to use .ui file or stable to use .py file
status = 'stable'
qtCreatorFile = "gui_linux.ui"

if status == 'dev':
    Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
elif status == 'stable':
    from gui_linux import Ui_MainWindow

class ExcelMerger(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):

        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        # Required by Qt5 to initialize the UI
        self.setupUi(self)

        # Set the title for the app
        self.setWindowTitle("Excel Merger")

        self.browseButton.clicked.connect(self.openFileNameDialog)
        self.processButton.clicked.connect(self.mergeFiles)

    def mergeFiles(self):
        if self.lineEdit.text() == '':
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Silakan isi direktori")
            msgBox.setWindowTitle("Pemberitahuan")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

        cwd = self.lineEdit.text()
        files = os.listdir(cwd)
        files.sort()
        files = [cwd + '/' + sub for sub in files]
        total_data = len(files)
        counter = 0

        df = pd.DataFrame()

        if self.radioExcel.isChecked():
            for i in range(total_data):
                self.statusProgress.setText('Merging Data...')
                if files[i].endswith('.xlsx') or files[i].endswith('.xls'):
                    if files[i].endswith('merged.xlsx'):
                        continue
                    df = df.append(pd.read_excel(files[i]), ignore_index=True)
                counter = int(counter + (i+1)/total_data * 100)
                self.progressBar.setValue(counter)

            df.to_excel(cwd + '/merged.xlsx')
            self.statusProgress.setText('Finished')
            self.progressBar.setValue(100)

        elif self.radioCsv.isChecked():
            for i in range(total_data):
                self.statusProgress.setText('Merging Data...')
                if files[i].endswith('.csv'):
                    if files[i].endswith('merged.csv'):
                        continue
                    df = df.append(pd.read_csv(files[i]), ignore_index=True)
                counter = int(counter + (i+1)/total_data * 100)
                self.progressBar.setValue(counter)

            df.to_csv(cwd + '/merged.csv')
            self.statusProgress.setText('Finished')
            self.progressBar.setValue(100)

    def openFileNameDialog(self):
        path = QtWidgets.QFileDialog.getExistingDirectory()
        self.lineEdit.setText('{}'.format(path))

def main(argv):
    # create Qt application
    app = QtWidgets.QApplication(argv)

    # create main window
    wnd = ExcelMerger()
    
    # Move the app window to upper left
    wnd.move(100,100)
    wnd.show()

    # run!
    retval = app.exec_()

    # exit
    sys.exit(retval)


if __name__ == "__main__":
    main(sys.argv)
