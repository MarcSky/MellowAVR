import os
import sys
sys.path.insert(0, 'gui')
from mainwindow import *

app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
