from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *
from PyQt4.QtGui import QDialog 
from subprocess import Popen, PIPE
from new_project import Ui_Dialog
import sys
import os

class np_Dialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        #self.ui = Ui_Dialog()
        self.setupUi(self)
        self.nameProject = ""
        self.pathProject = ""
        self.fullpath = ""
        self.mainpath = ""
        self.connect(self.find, SIGNAL("clicked()"), self.findPathHandler)
        self.connect(self.ok, SIGNAL("clicked()"), self.okHandler)
        self.connect(self.cancel, SIGNAL("clicked()"), self.exitHandler)
 
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
			#print self.fullpath
			main = open(self.mainpath, "a+")
			main.close()
			#comm_string = "cd .. && cd files && cp makefile "  + self.fullpath + '/'
			#print comm_string
			#comm_string = "uname -a"
			#Popen(comm_string, executable='/bin/bash', shell=True).communicate()
			makefile = open("../files/makefile", "r")
			data = makefile.read()
			makefile.close()
			print data
			makefile = open(self.fullpath + '/makefile', "w+")
			makefile.write(data)
			makefile.close()
			self.close()
		else:
			self.close()
        
    def findPathHandler(self):
		filepath = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
		self.pathEdit.setText(filepath)
		self.pathProject = filepath
		       
    def getInfo(self):
		return self.fullpath, self.mainpath

    def exitHandler(self):
		self.close()
	
#app = QApplication(sys.argv)
#main = np_Dialog()
#main.show()
#sys.exit(app.exec_())
