import sys
from PyQt4 import QtGui, QtCore
import os

class Screenshot(QtGui.QWidget):
    
    def __init__(self):
        super(Screenshot, self).__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 100)
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

        # Save the screenshot to a file
        screenshot.save('screenshot.png', 'png')

        # Show the main window again
        self.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Screenshot()
    sys.exit(app.exec_())
