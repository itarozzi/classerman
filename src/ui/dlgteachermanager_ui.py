# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgteachermanager.ui'
#
# Created: Tue Jul 12 16:59:38 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DlgTeacherManager(object):
    def setupUi(self, DlgTeacherManager):
        DlgTeacherManager.setObjectName("DlgTeacherManager")
        DlgTeacherManager.resize(1000, 619)
        DlgTeacherManager.setBaseSize(QtCore.QSize(800, 600))
        self.verticalLayout = QtGui.QVBoxLayout(DlgTeacherManager)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblTeacher = QtGui.QLabel(DlgTeacherManager)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.lblTeacher.setFont(font)
        self.lblTeacher.setScaledContents(False)
        self.lblTeacher.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTeacher.setObjectName("lblTeacher")
        self.horizontalLayout.addWidget(self.lblTeacher)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableTeachers = QtGui.QTableWidget(DlgTeacherManager)
        self.tableTeachers.setMinimumSize(QtCore.QSize(750, 0))
        self.tableTeachers.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tableTeachers.setProperty("showDropIndicator", True)
        self.tableTeachers.setAlternatingRowColors(True)
        self.tableTeachers.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableTeachers.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableTeachers.setRowCount(0)
        self.tableTeachers.setColumnCount(2)
        self.tableTeachers.setObjectName("tableTeachers")
        self.tableTeachers.setColumnCount(2)
        self.tableTeachers.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableTeachers.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableTeachers.setHorizontalHeaderItem(1, item)
        self.tableTeachers.horizontalHeader().setCascadingSectionResizes(False)
        self.tableTeachers.horizontalHeader().setMinimumSectionSize(30)
        self.tableTeachers.horizontalHeader().setSortIndicatorShown(False)
        self.tableTeachers.verticalHeader().setCascadingSectionResizes(False)
        self.tableTeachers.verticalHeader().setDefaultSectionSize(30)
        self.tableTeachers.verticalHeader().setMinimumSectionSize(30)
        self.tableTeachers.verticalHeader().setSortIndicatorShown(False)
        self.horizontalLayout_4.addWidget(self.tableTeachers)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(DlgTeacherManager)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lstClasses = QtGui.QListWidget(DlgTeacherManager)
        self.lstClasses.setObjectName("lstClasses")
        self.verticalLayout_2.addWidget(self.lstClasses)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.groupBox = QtGui.QGroupBox(DlgTeacherManager)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 40))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnAdd = QtGui.QToolButton(self.groupBox)
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout_2.addWidget(self.btnAdd)
        self.btnDelete = QtGui.QToolButton(self.groupBox)
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout_2.addWidget(self.btnDelete)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btnChengePasswd = QtGui.QToolButton(self.groupBox)
        self.btnChengePasswd.setMinimumSize(QtCore.QSize(150, 0))
        self.btnChengePasswd.setObjectName("btnChengePasswd")
        self.horizontalLayout_2.addWidget(self.btnChengePasswd)
        self.btnClassroom = QtGui.QToolButton(self.groupBox)
        self.btnClassroom.setMinimumSize(QtCore.QSize(150, 0))
        self.btnClassroom.setObjectName("btnClassroom")
        self.horizontalLayout_2.addWidget(self.btnClassroom)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btnImport = QtGui.QToolButton(self.groupBox)
        self.btnImport.setObjectName("btnImport")
        self.horizontalLayout_2.addWidget(self.btnImport)
        self.verticalLayout.addWidget(self.groupBox)
        self.line = QtGui.QFrame(DlgTeacherManager)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buttonBox = QtGui.QDialogButtonBox(DlgTeacherManager)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(DlgTeacherManager)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DlgTeacherManager.reject)
        QtCore.QObject.connect(self.btnImport, QtCore.SIGNAL("clicked()"), DlgTeacherManager.fileImport)
        QtCore.QObject.connect(self.btnChengePasswd, QtCore.SIGNAL("clicked()"), DlgTeacherManager.modPasswd)
        QtCore.QObject.connect(self.btnDelete, QtCore.SIGNAL("clicked()"), DlgTeacherManager.delUser)
        QtCore.QObject.connect(self.btnAdd, QtCore.SIGNAL("clicked()"), DlgTeacherManager.addUser)
        QtCore.QObject.connect(self.btnClassroom, QtCore.SIGNAL("clicked()"), DlgTeacherManager.assignClassroom)
        QtCore.QObject.connect(self.tableTeachers, QtCore.SIGNAL("itemSelectionChanged()"), DlgTeacherManager.tableChanged)
        QtCore.QMetaObject.connectSlotsByName(DlgTeacherManager)

    def retranslateUi(self, DlgTeacherManager):
        DlgTeacherManager.setWindowTitle(QtGui.QApplication.translate("DlgTeacherManager", "Gestione Utenti", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTeacher.setText(QtGui.QApplication.translate("DlgTeacherManager", "Gestione degli Insegnanti", None, QtGui.QApplication.UnicodeUTF8))
        self.tableTeachers.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("DlgTeacherManager", "Nome Completo", None, QtGui.QApplication.UnicodeUTF8))
        self.tableTeachers.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("DlgTeacherManager", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DlgTeacherManager", "Elenco Classi", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd.setText(QtGui.QApplication.translate("DlgTeacherManager", "Aggiungi", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDelete.setText(QtGui.QApplication.translate("DlgTeacherManager", "Elimina", None, QtGui.QApplication.UnicodeUTF8))
        self.btnChengePasswd.setText(QtGui.QApplication.translate("DlgTeacherManager", "Modifica Password", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClassroom.setText(QtGui.QApplication.translate("DlgTeacherManager", "Assegna le Classi", None, QtGui.QApplication.UnicodeUTF8))
        self.btnImport.setText(QtGui.QApplication.translate("DlgTeacherManager", "Importa elenco da file", None, QtGui.QApplication.UnicodeUTF8))

