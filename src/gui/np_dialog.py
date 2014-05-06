from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *
from PyQt4.QtGui import QDialog 
from subprocess import Popen, PIPE
from new_project import Ui_Dialog
import sys
import os
sys.path.insert(0, '../library')
from pars_makefile import *

class np_Dialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.nameProject = ""
        self.pathProject = ""
        self.fullpath = ""
        self.mainpath = ""
        self.connect(self.find, SIGNAL("clicked()"), self.findPathHandler)
        self.connect(self.ok, SIGNAL("clicked()"), self.okHandler)
        self.connect(self.cancel, SIGNAL("clicked()"), self.exitHandler)
        self.main_mcu = ['atmega8', 'atmega16', 'atmega32', 'atmega64', 'atmega128']
        self.freq_mcu = ['8000000','16000000']
        self.freq_box.addItems(self.freq_mcu)
        self.mcu_box.addItems(self.main_mcu)

    def okHandler(self):
		if self.nameEdit.text() and self.pathEdit.text():
			self.nameProject = self.nameEdit.text()
			directory = QtCore.QDir(self.pathProject)
			directory.mkdir(self.nameProject)
			self.fullpath = self.pathProject + '/' + self.nameProject
			directory = QtCore.QDir(self.fullpath)
			directory.mkdir("src")
			directory.mkdir("header")
			self.mainpath = self.fullpath + '/main.c'
			makefile = open("../files/make_file", "r")
			text = makefile.readlines()
			makefile.close()
			data = {}
			data['MCU'] = self.mcu_box.currentText()
			data['F_CPU'] = self.freq_box.currentText() + "UL"
			texts = change_makefile(text, data)
			makefile = open(self.fullpath + '/makefile', "w+")
			makefile.write(str(texts))
			makefile.close()
			config = open(self.fullpath + '/mellow.mcf', "w+")
			config.write(self.create_config())
			config.close()
			self.close()
		else:
			self.close()
        
    def findPathHandler(self):
		filepath = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
		self.pathEdit.setText(filepath)
		self.pathProject = filepath
		       
    def getInfo(self):
		return self.fullpath, self.mainpath

    def create_config(self):
		content = "[config]\n" + "project_name=" + self.nameProject + "\n" + "default_mcu=" + self.mcu_box.currentText() + "\n"
		return content		

    def exitHandler(self):
		self.close()		

#app = QApplication(sys.argv)
#main = np_Dialog()
#main.show()
#sys.exit(app.exec_())