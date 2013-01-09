# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgstudentmanager.ui'
#
# Created: Tue Jul 12 16:59:45 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DlgStudentManager(object):
    def setupUi(self, DlgStudentManager):
        DlgStudentManager.setObjectName("DlgStudentManager")
        DlgStudentManager.resize(806, 619)
        DlgStudentManager.setBaseSize(QtCore.QSize(800, 600))
        self.verticalLayout = QtGui.QVBoxLayout(DlgStudentManager)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(DlgStudentManager)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lstClasses = QtGui.QComboBox(DlgStudentManager)
        self.lstClasses.setObjectName("lstClasses")
        self.lstClasses.addItem("")
        self.lstClasses.addItem("")
        self.lstClasses.addItem("")
        self.horizontalLayout.addWidget(self.lstClasses)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableStudents = QtGui.QTableWidget(DlgStudentManager)
        self.tableStudents.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tableStudents.setProperty("showDropIndicator", True)
        self.tableStudents.setAlternatingRowColors(True)
        self.tableStudents.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableStudents.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableStudents.setRowCount(0)
        self.tableStudents.setColumnCount(2)
        self.tableStudents.setObjectName("tableStudents")
        self.tableStudents.setColumnCount(2)
        self.tableStudents.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableStudents.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableStudents.setHorizontalHeaderItem(1, item)
        self.tableStudents.horizontalHeader().setCascadingSectionResizes(False)
        self.tableStudents.horizontalHeader().setMinimumSectionSize(30)
        self.tableStudents.horizontalHeader().setSortIndicatorShown(False)
        self.tableStudents.verticalHeader().setCascadingSectionResizes(False)
        self.tableStudents.verticalHeader().setDefaultSectionSize(30)
        self.tableStudents.verticalHeader().setMinimumSectionSize(30)
        self.tableStudents.verticalHeader().setSortIndicatorShown(False)
        self.verticalLayout.addWidget(self.tableStudents)
        self.groupBox = QtGui.QGroupBox(DlgStudentManager)
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
        self.btnChengePasswd.setObjectName("btnChengePasswd")
        self.horizontalLayout_2.addWidget(self.btnChengePasswd)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btnImport = QtGui.QToolButton(self.groupBox)
        self.btnImport.setObjectName("btnImport")
        self.horizontalLayout_2.addWidget(self.btnImport)
        self.verticalLayout.addWidget(self.groupBox)
        self.line = QtGui.QFrame(DlgStudentManager)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buttonBox = QtGui.QDialogButtonBox(DlgStudentManager)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(DlgStudentManager)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DlgStudentManager.reject)
        QtCore.QObject.connect(self.btnImport, QtCore.SIGNAL("clicked()"), DlgStudentManager.fileImport)
        QtCore.QObject.connect(self.lstClasses, QtCore.SIGNAL("currentIndexChanged(QString)"), DlgStudentManager.updateTable)
        QtCore.QObject.connect(self.btnChengePasswd, QtCore.SIGNAL("clicked()"), DlgStudentManager.modPasswd)
        QtCore.QObject.connect(self.btnDelete, QtCore.SIGNAL("clicked()"), DlgStudentManager.delUser)
        QtCore.QObject.connect(self.btnAdd, QtCore.SIGNAL("clicked()"), DlgStudentManager.addUser)
        QtCore.QMetaObject.connectSlotsByName(DlgStudentManager)

    def retranslateUi(self, DlgStudentManager):
        DlgStudentManager.setWindowTitle(QtGui.QApplication.translate("DlgStudentManager", "Gestione Utenti", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DlgStudentManager", "Classe ", None, QtGui.QApplication.UnicodeUTF8))
        self.lstClasses.setItemText(0, QtGui.QApplication.translate("DlgStudentManager", "classe_1a", None, QtGui.QApplication.UnicodeUTF8))
        self.lstClasses.setItemText(1, QtGui.QApplication.translate("DlgStudentManager", "classe_2a", None, QtGui.QApplication.UnicodeUTF8))
        self.lstClasses.setItemText(2, QtGui.QApplication.translate("DlgStudentManager", "classe_3a", None, QtGui.QApplication.UnicodeUTF8))
        self.tableStudents.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("DlgStudentManager", "Nome Completo", None, QtGui.QApplication.UnicodeUTF8))
        self.tableStudents.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("DlgStudentManager", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd.setText(QtGui.QApplication.translate("DlgStudentManager", "Aggiungi", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDelete.setText(QtGui.QApplication.translate("DlgStudentManager", "Elimina", None, QtGui.QApplication.UnicodeUTF8))
        self.btnChengePasswd.setText(QtGui.QApplication.translate("DlgStudentManager", "Modifica Password", None, QtGui.QApplication.UnicodeUTF8))
        self.btnImport.setText(QtGui.QApplication.translate("DlgStudentManager", "Importa elenco da file", None, QtGui.QApplication.UnicodeUTF8))
