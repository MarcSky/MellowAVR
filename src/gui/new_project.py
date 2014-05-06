# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_project.ui'
#
# Created: Fri May  2 11:41:07 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(428, 221)
        self.nameEdit = QtGui.QLineEdit(Dialog)
        self.nameEdit.setGeometry(QtCore.QRect(70, 20, 341, 31))
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.pathEdit = QtGui.QLineEdit(Dialog)
        self.pathEdit.setGeometry(QtCore.QRect(70, 60, 271, 31))
        self.pathEdit.setObjectName(_fromUtf8("pathEdit"))
        self.find = QtGui.QPushButton(Dialog)
        self.find.setGeometry(QtCore.QRect(350, 60, 61, 31))
        self.find.setObjectName(_fromUtf8("find"))
        self.cancel = QtGui.QPushButton(Dialog)
        self.cancel.setGeometry(QtCore.QRect(240, 180, 81, 31))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.ok = QtGui.QPushButton(Dialog)
        self.ok.setGeometry(QtCore.QRect(330, 180, 81, 31))
        self.ok.setDefault(True)
        self.ok.setFlat(False)
        self.ok.setObjectName(_fromUtf8("ok"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.mcu_box = QtGui.QComboBox(Dialog)
        self.mcu_box.setGeometry(QtCore.QRect(70, 100, 341, 27))
        self.mcu_box.setObjectName(_fromUtf8("mcu_box"))
        self.freq_box = QtGui.QComboBox(Dialog)
        self.freq_box.setGeometry(QtCore.QRect(70, 140, 341, 27))
        self.freq_box.setObjectName(_fromUtf8("freq_box"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 66, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 66, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "New project", None, QtGui.QApplication.UnicodeUTF8))
        self.find.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.ok.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Path:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "MCU:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Freq:", None, QtGui.QApplication.UnicodeUTF8))

