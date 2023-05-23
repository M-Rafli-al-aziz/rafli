import sys
from PyQt4 import QtGui, QtCore
import os
import time

class Screenshot(QtGui.QWidget):
    
    def __init__(self):
        super(Screenshot, self).__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 250, 100)
        self.setWindowTitle('Screenshot')

        self.button = QtGui.QPushButton('Take Screenshot', self)
        self.button.clicked.connect(self.takeScreenshot)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.button)

        self.setLayout(vbox)

        self.show()

    def takeScreenshot(self):
        # Hide the main window
        self.hide()

        # Take the screenshot
        screenshot = QtGui.QPixmap.grabWindow(QtGui.QApplication.desktop().winId())

        # Choose the save directory
        save_directory = str(QtGui.QFileDialog.getExistingDirectory(self, '/home/pi/Pictures/Screenshot'))

        if save_directory:
            # Construct the file path with a unique name based on current time
            current_time = time.strftime('%Y%m%d-%H%M%S')
            file_name = 'screenshot_{}.png'.format(current_time)
            file_path = os.path.join(save_directory, file_name)
            
            # check the file
            counter = 1
            while os.path.exists(file_path):
                file_name = 'screenshot_{}_{}.png'.format(current_time, counter)            
                # Construct the file path with the fixed file name
                file_path = os.path.join(save_directory, file_name)
                counter += 1

            # Save the screenshot to the selected file path
            screenshot.save(file_path, 'png')

            # Show a message box indicating the successful save
            QtGui.QMessageBox.information(self, 'Screenshot Saved', 'Screenshot saved successfully.')

        # Show the main window again
        self.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Screenshot()
    sys.exit(app.exec_())
