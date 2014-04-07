#from PyQt4.Qt import *
from PyQt4 import QtGui, QtCore
from mainwind import Ui_MainWindow
import sys
import os
import os.path
sys.path.insert(0, '../library')
import compiler
import parser_config
from stylehighliter import *
from np_dialog import *
from parser_config import *

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.setupUi(self)
		self.path_list = []
		self.filepath  = ""
		self.flag_tab = 0
		self.resize(1024, 650)
		self.parser = parser_config()
		#self.parser.set_path('/home/juster/test')
		#print self.parser.get_param('project_name')
		self.model = QtGui.QFileSystemModel(self)
		self.treeView.doubleClicked.connect(self.on_treeView_clicked)
		
		self.action_New.activated.connect(self.file_new_func)
		self.action_New_Project.activated.connect(self.file_new_project_func)
		self.action_Open.activated.connect(self.file_open_func)
		self.action_Save.activated.connect(self.file_save_func)
		self.action_Save_As.activated.connect(self.file_saveas_func)
		self.action_Quit.activated.connect(self.closeEvent)
		self.action_Compile.activated.connect(self.build_compile_func)
		self.action_Make.activated.connect(self.build_make_func)
		self.actionGCC_version.activated.connect(self.gcc_version_func)
		self.actionClean.activated.connect(self.build_clean_func)
		self.actionDisassembler.activated.connect(self.build_disasm_func)
		self.tabWidget.setTabsClosable(True)
		self.connect(self.tabWidget, QtCore.SIGNAL('tabCloseRequested(int)'), self.removeTab)
		self.rootpath = QtCore.QDir.rootPath() + "home/juster/" # /Linux
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
	
	#check path for file.
	def check_path(self, path):
		flag = 1 #not found
		for x in range(len(self.path_list)):
			if(self.path_list[x] == path):
				flag = 0 #found
				break
		return flag		
		
	def file_open_func(self, path = 0):
		try:
			self.filepath = 0;
			if not path:		
				self.filepath = QFileDialog.getOpenFileName(self, 'Open file', self.rootpath, "C/C++ (*.c);; All (*.*);; Makefile (makefile)")	
			else:
				self.filepath = path
			
			if not self.check_path(self.filepath):
				self.listWidget.addItem("This file is open: " + self.filepath)
				return
						
			f = open(self.filepath, 'a+')
			self.path_list.append(self.filepath)
			fileInfo = QtCore.QFileInfo(self.filepath)
			fileName = fileInfo.baseName()
			
			absolutePath = fileInfo.path()
			path_config = self.find_config(self.filepath)

			self.indexfortab = self.tabWidget.count() - self.tabWidget.currentIndex()				
			self.tabWidget.addTab(QtGui.QTextEdit(''), fileName)
			
			if(self.flag_tab == 0):
				self.editor = self.tabWidget.widget(0)
				self.flag_tab = 1
			else:
				self.editor = self.tabWidget.widget(self.tabWidget.currentIndex() + self.indexfortab)

			self.editor.setTabStopWidth(15)
			self.highlighter = Highlighter(self.editor.document())

			with f:        
				data = f.read()
				self.editor.setText(data)
				f.close() #new					
						
			if path_config and path_config == absolutePath:
				self.model.setRootPath(absolutePath)
				self.indexRoot = self.model.index(self.model.rootPath())
				self.treeView.setModel(self.model)
				self.treeView.setRootIndex(self.indexRoot)
			
			self.listWidget.addItem("Open file: " + self.filepath)
			
		except IOError as (errno, strerror):
			self.listWidget.addItem("Error: " + strerror)			
		except:
			pass
		
	def find_config(self, path):
		dic = list(str(path).split('/'))
		size = len(dic)
		count = 1
		while (size - count > 1):
			new_path = '/'.join(dic[1:size - count])
			count = count + 1
			a = '/' + new_path
			if os.path.isfile(a + '/mellow.mcf'):
				return a
		return 0
		
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
		
	def closeEvent(self, event):
		ask = QtGui.QMessageBox.question(self, 'Exit', 'Are you sure to quit?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
		if ask == QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()
			
	def build_compile_func(self):
		if (len(self.path_list) == 0):
			self.listWidget.addItem("Project not opened")
			return

		path = self.path_list[self.tabWidget.currentIndex()]
		infopath = QFileInfo(path)
		filePath = str(infopath.path()) + '/'
		output, check = compiler.build_project(filePath)
		outputdecode = unicode(output, 'UTF-8')
		self.textEdit.setText(outputdecode)
		if check:
			self.listWidget.addItem("succes compile")
		else:
			self.listWidget.addItem("not success compile, check your makefile")
 
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
	
	def build_clean_func(self):
		if (len(self.path_list) == 0):
			return
		path = self.path_list[self.tabWidget.currentIndex()]
		infopath = QFileInfo(path)
		filePath = str(infopath.path()) + '/'
		output, check = compiler.build_clean(filePath)
		outputdecode = unicode(output, 'UTF-8')
		self.textEdit.setText(outputdecode)
		if not check:
			self.listWidget.addItem("succes clean")
		else:
			self.listWidget.addItem("file *.hex exist")

	def build_disasm_func(self):
		if (len(self.path_list) == 0):
			return
		path = self.path_list[self.tabWidget.currentIndex()]
		infopath = QFileInfo(path)
		filePath = str(infopath.path()) + '/'
		output, check = compiler.build_disasm(filePath)
		outputdecode = unicode(output, 'UTF-8')
		self.textEdit.setText(outputdecode)
		if check:
			self.file_open_func(filePath + 'bin/main.asm')
			self.listWidget.addItem("succes clean")
		else:
			self.listWidget.addItem("file *.hex exist")

	def gcc_version_func(self):
		self.listWidget.addItem(compiler.build_version_gcc())
		return 0
		
	def on_treeView_clicked(self, index):
		indexItem = self.model.index(index.row(), 0, index.parent())
		fileName = self.model.fileName(indexItem)
		filePath = self.model.filePath(indexItem)
		self.file_open_func(filePath)

	
#app = QApplication(sys.argv)
#main = MainWindow()
#main.show()
#sys.exit(app.exec_())
