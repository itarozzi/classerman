# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/mainwindow.ui'
#
# Created: Fri Feb 15 16:08:54 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1024, 768)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(200, 200))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/logo/pixmaps/logo.jpg")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.labelServerId = QtGui.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 116, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 116, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.labelServerId.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelServerId.setFont(font)
        self.labelServerId.setAlignment(QtCore.Qt.AlignCenter)
        self.labelServerId.setObjectName(_fromUtf8("labelServerId"))
        self.verticalLayout_2.addWidget(self.labelServerId)
        self.labelYear = QtGui.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 116, 113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelYear.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(37)
        font.setBold(True)
        font.setWeight(75)
        self.labelYear.setFont(font)
        self.labelYear.setTextFormat(QtCore.Qt.PlainText)
        self.labelYear.setAlignment(QtCore.Qt.AlignCenter)
        self.labelYear.setObjectName(_fromUtf8("labelYear"))
        self.verticalLayout_2.addWidget(self.labelYear)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(200, 200))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/logo/pixmaps/Stampa-silicone-tondo-fi55.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtGui.QFrame.Raised)
        self.line.setLineWidth(4)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnNewYear = QtGui.QToolButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(11)
        sizePolicy.setHeightForWidth(self.btnNewYear.sizePolicy().hasHeightForWidth())
        self.btnNewYear.setSizePolicy(sizePolicy)
        self.btnNewYear.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnNewYear.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/pixmaps/planner.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNewYear.setIcon(icon)
        self.btnNewYear.setIconSize(QtCore.QSize(128, 128))
        self.btnNewYear.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnNewYear.setAutoRaise(False)
        self.btnNewYear.setArrowType(QtCore.Qt.NoArrow)
        self.btnNewYear.setObjectName(_fromUtf8("btnNewYear"))
        self.horizontalLayout.addWidget(self.btnNewYear)
        self.btnCloseYear = QtGui.QToolButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(11)
        sizePolicy.setHeightForWidth(self.btnCloseYear.sizePolicy().hasHeightForWidth())
        self.btnCloseYear.setSizePolicy(sizePolicy)
        self.btnCloseYear.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnCloseYear.setFont(font)
        self.btnCloseYear.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/pixmaps/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCloseYear.setIcon(icon1)
        self.btnCloseYear.setIconSize(QtCore.QSize(128, 128))
        self.btnCloseYear.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnCloseYear.setObjectName(_fromUtf8("btnCloseYear"))
        self.horizontalLayout.addWidget(self.btnCloseYear)
        self.btnTeachers = QtGui.QToolButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(11)
        sizePolicy.setHeightForWidth(self.btnTeachers.sizePolicy().hasHeightForWidth())
        self.btnTeachers.setSizePolicy(sizePolicy)
        self.btnTeachers.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnTeachers.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/pixmaps/education.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnTeachers.setIcon(icon2)
        self.btnTeachers.setIconSize(QtCore.QSize(128, 128))
        self.btnTeachers.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnTeachers.setObjectName(_fromUtf8("btnTeachers"))
        self.horizontalLayout.addWidget(self.btnTeachers)
        self.btnStudents = QtGui.QToolButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(11)
        sizePolicy.setHeightForWidth(self.btnStudents.sizePolicy().hasHeightForWidth())
        self.btnStudents.setSizePolicy(sizePolicy)
        self.btnStudents.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnStudents.setFont(font)
        self.btnStudents.setStyleSheet(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/pixmaps/System-users.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStudents.setIcon(icon3)
        self.btnStudents.setIconSize(QtCore.QSize(128, 128))
        self.btnStudents.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnStudents.setObjectName(_fromUtf8("btnStudents"))
        self.horizontalLayout.addWidget(self.btnStudents)
        self.btnAdvanced = QtGui.QToolButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(11)
        sizePolicy.setHeightForWidth(self.btnAdvanced.sizePolicy().hasHeightForWidth())
        self.btnAdvanced.setSizePolicy(sizePolicy)
        self.btnAdvanced.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnAdvanced.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/pixmaps/advanced_options.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAdvanced.setIcon(icon4)
        self.btnAdvanced.setIconSize(QtCore.QSize(128, 128))
        self.btnAdvanced.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnAdvanced.setObjectName(_fromUtf8("btnAdvanced"))
        self.horizontalLayout.addWidget(self.btnAdvanced)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuImpostazioni = QtGui.QMenu(self.menubar)
        self.menuImpostazioni.setEnabled(False)
        self.menuImpostazioni.setObjectName(_fromUtf8("menuImpostazioni"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setEnabled(False)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuArchivi = QtGui.QMenu(self.menubar)
        self.menuArchivi.setObjectName(_fromUtf8("menuArchivi"))
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionPreferenze = QtGui.QAction(MainWindow)
        self.actionPreferenze.setObjectName(_fromUtf8("actionPreferenze"))
        self.actionArchivioAnniPrec = QtGui.QAction(MainWindow)
        self.actionArchivioAnniPrec.setObjectName(_fromUtf8("actionArchivioAnniPrec"))
        self.menuImpostazioni.addAction(self.actionPreferenze)
        self.menuHelp.addAction(self.actionAbout)
        self.menuArchivi.addAction(self.actionArchivioAnniPrec)
        self.menubar.addAction(self.menuArchivi.menuAction())
        self.menubar.addAction(self.menuImpostazioni.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.btnAdvanced, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.execAdvancedUserManager)
        QtCore.QObject.connect(self.btnCloseYear, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.execYearEnd)
        QtCore.QObject.connect(self.btnNewYear, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.execYearNew)
        QtCore.QObject.connect(self.actionArchivioAnniPrec, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.showArchBackup)
        QtCore.QObject.connect(self.btnStudents, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.showStudentsManager)
        QtCore.QObject.connect(self.btnTeachers, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.showTeachersManager)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Pannello di Amministrazione del Server", None, QtGui.QApplication.UnicodeUTF8))
        self.labelServerId.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.labelYear.setText(QtGui.QApplication.translate("MainWindow", "Anno -", None, QtGui.QApplication.UnicodeUTF8))
        self.btnNewYear.setText(QtGui.QApplication.translate("MainWindow", "Nuovo Anno", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCloseYear.setText(QtGui.QApplication.translate("MainWindow", "Chiusura Anno", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTeachers.setText(QtGui.QApplication.translate("MainWindow", "Gestione Insegnanti", None, QtGui.QApplication.UnicodeUTF8))
        self.btnStudents.setText(QtGui.QApplication.translate("MainWindow", "Gestione Alunni", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdvanced.setText(QtGui.QApplication.translate("MainWindow", "Gestione Avanzata", None, QtGui.QApplication.UnicodeUTF8))
        self.menuImpostazioni.setTitle(QtGui.QApplication.translate("MainWindow", "Impostazioni", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuArchivi.setTitle(QtGui.QApplication.translate("MainWindow", "Archivi", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferenze.setText(QtGui.QApplication.translate("MainWindow", "Preferenze", None, QtGui.QApplication.UnicodeUTF8))
        self.actionArchivioAnniPrec.setText(QtGui.QApplication.translate("MainWindow", "Archivio anni precedenti", None, QtGui.QApplication.UnicodeUTF8))

import classerman_rc
