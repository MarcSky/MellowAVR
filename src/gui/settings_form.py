from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *
from PyQt4.QtGui import QDialog 
from subprocess import Popen, PIPE
from settings import Ui_Dialog
import sys
import os
sys.path.insert(0, '../library')
from pars_makefile import *

class settings_form(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.main_mcu = ['atmega8', 'atmega16', 'atmega32', 'atmega64', 'atmega128']
        self.freq_mcu = ['8000000','16000000']
        self.optimization = ['-Os','-O1','-O2','-O3']
        self.freq_box.addItems(self.freq_mcu)
        self.mcu_box.addItems(self.main_mcu)
        self.optimizBox.addItems(self.optimization)
        self.our_flags = {}
        self.cflags = ""
        self.now_mcu = ""
        self.now_freq = ""
        self.connect(self.WallBox, QtCore.SIGNAL('stateChanged(int)'), self.wallbox_func)
        self.connect(self.WerrorBox, QtCore.SIGNAL('stateChanged(int)'), self.werrorbox_func)
        self.connect(self.gdwarfBox, QtCore.SIGNAL('stateChanged(int)'), self.gdwarf_func)
        self.connect(self.funsignedBox, QtCore.SIGNAL('stateChanged(int)'), self.funsigned_func)
        self.connect(self.gnu99Box, QtCore.SIGNAL('stateChanged(int)'), self.gnu99_func)
        self.connect(self.wundefBox, QtCore.SIGNAL('stateChanged(int)'), self.wundef_func)
        self.connect(self.fpackBox, QtCore.SIGNAL('stateChanged(int)'), self.fpack_func)
        self.connect(self.fshortBox, QtCore.SIGNAL('stateChanged(int)'), self.fshort_func)
        self.connect(self.wstrictBox, QtCore.SIGNAL('stateChanged(int)'), self.wstrict_func)
        self.connect(self.funsignBox, QtCore.SIGNAL('stateChanged(int)'), self.funsign_func)
        self.connect(self.saveButton, QtCore.SIGNAL("clicked()"), self.saveHandler)
        self.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), self.cancelHandler)

    def saveHandler(self):
        self.parse_flags()
        makefile = open("../files/make_file", "r")
        text = makefile.readlines()
        makefile.close()        
        data = {}
        data['CFLAGS'] = self.cflags
        texts = change_makefile(text, data)
        makefile = open('makefile', "w+")
        makefile.write(str(texts))
        makefile.close()
        print "ok"
        return 0

    def cancelHandler(self):
        return 0

    def wallbox_func(self):
    	self.our_flags['-Wall'] = 1 if self.WallBox.isChecked() else 0
    
    def werrorbox_func(self):
    	self.our_flags['-Werror'] = 1 if self.WerrorBox.isChecked() else 0
    
    def gdwarf_func(self):
    	self.our_flags['-gdwarf-2'] = 1 if self.gdwarfBox.isChecked() else 0

    def funsigned_func(self):
    	self.our_flags['-funsigned-char'] = 1 if self.funsignedBox.isChecked() else 0

    def gnu99_func(self):
    	self.our_flags['-std=gnu99'] = 1 if self.gnu99Box.isChecked() else 0

    def wundef_func(self):
    	self.our_flags['-Wundef'] = 1 if self.wundefBox.isChecked() else 0

    def fpack_func(self):
    	self.our_flags['-fpack-struct'] = 1 if self.fpackBox.isChecked() else 0

    def fshort_func(self):
    	self.our_flags['-fshort-enums'] = 1 if self.fshortBox.isChecked() else 0

    def wstrict_func(self):
    	self.our_flags['-Wstrict-prototypes'] = 1 if self.wstrictBox.isChecked() else 0

    def funsign_func(self):
    	self.our_flags['-funsigned-bitfields'] = 1 if self.funsignBox.isChecked() else 0

    def parse_flags(self):
        for x in self.our_flags.keys():
            if self.our_flags[x]:
                self.cflags += ' ' + x
        self.cflags+=' ' + self.optimizBox.currentText()
        self.now_mcu = self.mcu_box.currentText()
        self.now_freq = self.freq_box.currentText()

app = QApplication(sys.argv)
main = settings_form()
main.show()
sys.exit(app.exec_())