# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Tue May  6 11:00:39 2014
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
        Dialog.resize(663, 450)
        Dialog.setMinimumSize(QtCore.QSize(663, 450))
        Dialog.setMaximumSize(QtCore.QSize(663, 450))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 661, 361))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 341, 91))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.mcu_box = QtGui.QComboBox(self.groupBox)
        self.mcu_box.setGeometry(QtCore.QRect(60, 20, 271, 27))
        self.mcu_box.setObjectName(_fromUtf8("mcu_box"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.freq_box = QtGui.QComboBox(self.groupBox)
        self.freq_box.setGeometry(QtCore.QRect(60, 60, 271, 27))
        self.freq_box.setObjectName(_fromUtf8("freq_box"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 110, 331, 201))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.WallBox = QtGui.QCheckBox(self.groupBox_2)
        self.WallBox.setGeometry(QtCore.QRect(10, 30, 97, 22))
        self.WallBox.setObjectName(_fromUtf8("WallBox"))
        self.WerrorBox = QtGui.QCheckBox(self.groupBox_2)
        self.WerrorBox.setGeometry(QtCore.QRect(10, 60, 97, 22))
        self.WerrorBox.setObjectName(_fromUtf8("WerrorBox"))
        self.gdwarfBox = QtGui.QCheckBox(self.groupBox_2)
        self.gdwarfBox.setGeometry(QtCore.QRect(10, 90, 97, 22))
        self.gdwarfBox.setObjectName(_fromUtf8("gdwarfBox"))
        self.funsignedBox = QtGui.QCheckBox(self.groupBox_2)
        self.funsignedBox.setGeometry(QtCore.QRect(10, 120, 131, 22))
        self.funsignedBox.setObjectName(_fromUtf8("funsignedBox"))
        self.gnu99Box = QtGui.QCheckBox(self.groupBox_2)
        self.gnu99Box.setGeometry(QtCore.QRect(10, 150, 101, 22))
        self.gnu99Box.setObjectName(_fromUtf8("gnu99Box"))
        self.wundefBox = QtGui.QCheckBox(self.groupBox_2)
        self.wundefBox.setGeometry(QtCore.QRect(10, 180, 97, 22))
        self.wundefBox.setObjectName(_fromUtf8("wundefBox"))
        self.fpackBox = QtGui.QCheckBox(self.groupBox_2)
        self.fpackBox.setGeometry(QtCore.QRect(170, 30, 111, 22))
        self.fpackBox.setObjectName(_fromUtf8("fpackBox"))
        self.fshortBox = QtGui.QCheckBox(self.groupBox_2)
        self.fshortBox.setGeometry(QtCore.QRect(170, 60, 121, 22))
        self.fshortBox.setObjectName(_fromUtf8("fshortBox"))
        self.wstrictBox = QtGui.QCheckBox(self.groupBox_2)
        self.wstrictBox.setGeometry(QtCore.QRect(170, 90, 161, 22))
        self.wstrictBox.setObjectName(_fromUtf8("wstrictBox"))
        self.funsignBox = QtGui.QCheckBox(self.groupBox_2)
        self.funsignBox.setGeometry(QtCore.QRect(170, 120, 151, 22))
        self.funsignBox.setObjectName(_fromUtf8("funsignBox"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(370, 10, 281, 91))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.optimizBox = QtGui.QComboBox(self.groupBox_3)
        self.optimizBox.setGeometry(QtCore.QRect(110, 20, 161, 27))
        self.optimizBox.setObjectName(_fromUtf8("optimizBox"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 101, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 271, 121))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_5 = QtGui.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 66, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 66, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 66, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.portBox = QtGui.QComboBox(self.groupBox_4)
        self.portBox.setGeometry(QtCore.QRect(80, 20, 181, 27))
        self.portBox.setObjectName(_fromUtf8("portBox"))
        self.speedBox = QtGui.QComboBox(self.groupBox_4)
        self.speedBox.setGeometry(QtCore.QRect(80, 50, 181, 27))
        self.speedBox.setObjectName(_fromUtf8("speedBox"))
        self.parityBox = QtGui.QComboBox(self.groupBox_4)
        self.parityBox.setGeometry(QtCore.QRect(80, 80, 181, 27))
        self.parityBox.setObjectName(_fromUtf8("parityBox"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.saveButton = QtGui.QPushButton(Dialog)
        self.saveButton.setGeometry(QtCore.QRect(460, 370, 98, 27))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.cancelButton = QtGui.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(560, 370, 98, 27))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Основное", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "MCU:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Freq:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Флаги", None, QtGui.QApplication.UnicodeUTF8))
        self.WallBox.setText(QtGui.QApplication.translate("Dialog", "-Wall", None, QtGui.QApplication.UnicodeUTF8))
        self.WerrorBox.setText(QtGui.QApplication.translate("Dialog", "-Werror", None, QtGui.QApplication.UnicodeUTF8))
        self.gdwarfBox.setText(QtGui.QApplication.translate("Dialog", "-gdwarf-2", None, QtGui.QApplication.UnicodeUTF8))
        self.funsignedBox.setText(QtGui.QApplication.translate("Dialog", "-funsigned-char", None, QtGui.QApplication.UnicodeUTF8))
        self.gnu99Box.setText(QtGui.QApplication.translate("Dialog", "-std=gnu99", None, QtGui.QApplication.UnicodeUTF8))
        self.wundefBox.setText(QtGui.QApplication.translate("Dialog", "-Wundef", None, QtGui.QApplication.UnicodeUTF8))
        self.fpackBox.setText(QtGui.QApplication.translate("Dialog", "-fpack-struct", None, QtGui.QApplication.UnicodeUTF8))
        self.fshortBox.setText(QtGui.QApplication.translate("Dialog", "-fshort-enums", None, QtGui.QApplication.UnicodeUTF8))
        self.wstrictBox.setText(QtGui.QApplication.translate("Dialog", "-Wstrict-prototypes", None, QtGui.QApplication.UnicodeUTF8))
        self.funsignBox.setText(QtGui.QApplication.translate("Dialog", "-funsigned-bitfields", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Dialog", "Оптимизация", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Optimization:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Dialog", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Dialog", "Основное", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Скорость", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Четность", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Порт", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("Dialog", "SerialPort", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Dialog", "Programmator", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("Dialog", "Fuse", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("Dialog", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
