#! /usr/bin/pythonx

from PyQt4.Qt import *
from PyQt4 import QtGui, QtCore
from PyQt4 import  uic
import subprocess
import sys
import os
sys.path.insert(0, '../library')
import compiler
from stylehighliter import *
from np_dialog import *

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi('mainwindow.ui', self)
		self.path_list = []
		self.filepath  = ""
		self.flag_tab = 0
		self.resize(1024, 650)
		self.action_New.activated.connect(self.file_new_func)
		self.action_New_Project.activated.connect(self.file_new_project_func)
		self.action_Open.activated.connect(self.file_open_func)
		self.action_Save.activated.connect(self.file_save_func)
		self.action_Save_As.activated.connect(self.file_saveas_func)
		self.action_Print_Review.activated.connect(self.file_preview_func)
		self.action_Print.activated.connect(self.file_print_func)
		self.action_Quit.activated.connect(self.file_quit_func)
		self.action_Compile.activated.connect(self.build_compile_func)
		self.action_Make.activated.connect(self.build_make_func)
		
		self.tabWidget.setTabsClosable(True)
		self.connect(self.tabWidget, QtCore.SIGNAL('tabCloseRequested(int)'), self.removeTab)
		self.rootpath = QtCore.QDir.rootPath() + "home" # /Linux
		self.window = None
        
	def removeTab(self,index):
		self.tabWidget.removeTab(index)
		self.listWidget.addItem("Close file: " + self.path_list[index])
		if(len(self.path_list) > 0):
			self.path_list.pop(index)
		if(self.tabWidget.count() == 0):
			self.flag_tab = 0
		print "Delete index " + str(index)
		print list(self.path_list)
		print "Now flag " + str(self.flag_tab) 
		
	def file_new_project_func(self):
		self.window = np_Dialog(self)
		if not self.window.exec_():
			fullpath, mainpath = self.window.getInfo()
			if mainpath and fullpath:
			    self.open_file(mainpath)
				
	def file_new_func(self):
		print "Index after: " + str(self.tabWidget.currentIndex())
		self.tabWidget.addTab(QtGui.QTextEdit(''), 'Empty')
		print "Count tab: " + str(self.tabWidget.count())
		if(self.flag_tab == 0):
			indexfortab = 0
			self.flag_tab = 1
		else:
			indexfortab = self.tabWidget.count() - self.tabWidget.currentIndex() - 1
		
		print "Index: " + str(indexfortab)	
		print "Index before: " + str(self.tabWidget.currentIndex())
		self.editor = self.tabWidget.widget(indexfortab)
		self.editor.setTabStopWidth(15) #tab
		self.highlighter = Highlighter(self.editor.document())
		self.path_list.append('Empty')
		self.listWidget.addItem("Open empty file")
		
	def file_open_func(self):
		try:		
			fname = QFileDialog.getOpenFileName(self, 'Open file', self.rootpath, "C/C++ (*.c);; All (*.*);; Makefile (makefile)")	
			f = open(fname, 'r')
			self.filepath = fname
			self.path_list.append(self.filepath)
			fileInfo = QtCore.QFileInfo(fname)
			fileName = fileInfo.baseName()
			
			self.indexfortab = self.tabWidget.count() - self.tabWidget.currentIndex()				
			self.tabWidget.addTab(QtGui.QTextEdit(''), fileName)
			
			if(self.flag_tab == 0):
				self.editor = self.tabWidget.widget(0)
				self.flag_tab = 1
			else:
				self.editor = self.tabWidget.widget(self.tabWidget.currentIndex() + self.indexfortab)

			self.editor.setTabStopWidth(15) #tab
			self.highlighter = Highlighter(self.editor.document())

			with f:        
				data = f.read()
				self.editor.setText(data)					
			
			self.listWidget.addItem("Open file: " + fname)			

		except IOError as (errno, strerror):
			self.listWidget.addItem("Error: " + strerror)			
		except:
			pass
			
	def file_save_func(self):
		try:
			if self.path_list[self.tabWidget.currentIndex()] == 'Empty':
				fname = QFileDialog.getSaveFileName(self, 'Save file',self.rootpath, "C/C++ (*.c);; All(*.*)")		
				self.filepath = fname
				self.stat = 1
			else:
				self.filepath = self.path_list[self.tabWidget.currentIndex()]
				self.stat = 0
			
			self.editor = self.tabWidget.widget(self.tabWidget.currentIndex())
			content  =  self.editor.toPlainText()
			filepath = self.filepath
			self.save_my_file(content,filepath,self.stat)
		except:
			self.listWidget.addItem("Error: Can't save file!")						
		
	def file_saveas_func(self):
		try:			
			fname = QFileDialog.getSaveFileName(self, 'Save file',self.rootpath, "C/C++ (*.c);;Header(*.h);;All(*.*)")		   		
			self.listWidget.addItem(fname)
			self.editor = self.tabWidget.widget(self.tabWidget.currentIndex())
			content  =  self.editor.toPlainText()
			self.save_my_file(content, fname, 1)
		except:
			self.listWidget.addItem("Error: Can't save file!")						
		
	def save_my_file(self,content,filepath,stat = 0):
		try:
			self.listWidget.addItem(filepath)
			if(stat == 0):
				os.remove(filepath)
			f = open(filepath, "w+")
			f.write(content)
			f.close()
			self.listWidget.addItem("Save file: "  + filepath)			
			self.last_saved = content			
		except IOError as (errno, strerror):
			self.listWidget.addItem("Error: " + strerror)			
		except:
			pass

	def file_preview_func(self):
		return 0	        
	def file_print_func(self):
		return 0
	def file_quit_func(self):
		return 0
	def build_compile_func(self):
		if (len(self.path_list) == 0):
			return
		path = self.path_list[self.tabWidget.currentIndex()]
		infopath = QFileInfo(path)
		filePath = str(infopath.path()) + '/'
		output = compiler.build_project(filePath)
		outputdecode = unicode(output, 'UTF-8')
		self.textEdit.setText(outputdecode)
 
	def open_file(self, file_path):
		try:
			f = open(file_path, 'a+')
			self.path_list.append(file_path)
			fileInfo = QtCore.QFileInfo(file_path)
			fileName = fileInfo.baseName()
		
			self.indexfortab = self.tabWidget.count() - self.tabWidget.currentIndex()				
			self.tabWidget.addTab(QtGui.QTextEdit(''), fileName)
		
			if(self.flag_tab == 0):
				self.editor = self.tabWidget.widget(0)
				self.flag_tab = 1
			else:
				self.editor = self.tabWidget.widget(self.tabWidget.currentIndex() + self.indexfortab)

			self.editor.setTabStopWidth(15) #tab
			self.highlighter = Highlighter(self.editor.document())

			with f:        
				data = f.read()
				self.editor.setText(data)					
		
			self.listWidget.addItem("Open file: " + file_path)
		except IOError as (errno, strerror):
			self.listWidget.addItem("Error: " + strerror)
		else:
			f.close()
 
	def build_make_func(self):
		return 0
		
	
app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
