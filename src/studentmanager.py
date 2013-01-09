#coding=iso-8859-15
'''
Created on 30/giu/2011

@author: ivan
'''

import sys
import pwd
import grp

from PyQt4 import QtGui
from PyQt4 import QtCore

from  ui.dlgstudentmanager_ui import Ui_DlgStudentManager

import studentimport
import studentmod

from utility.usermanager  import UserManager

class DlgStudentManager(QtGui.QDialog, Ui_DlgStudentManager):
    
    def __init__(self, parent, class_sel):
        super(DlgStudentManager, self).__init__(parent)
        self.setupUi(self)

        #assign window's controls
        self.initUI(class_sel)
        
    def initUI(self, class_sel):

        # == update system user list ==
        self.userList=pwd.getpwall()
    
        # == populate classed combo ==
        self.lstClasses.clear()
        pos=0
        idx_sel = 0
        
        for i in range(ord('a'), ord('p')+1):
            
            self.lstClasses.addItem("classe_1%s"%chr(i))
            self.lstClasses.addItem("classe_2%s"%chr(i))
            self.lstClasses.addItem("classe_3%s"%chr(i))
            pos=pos+1
            
        # == table properties ==
        self.tableStudents.setColumnCount(2)
        self.tableStudents.setRowCount(0)
        self.tableStudents.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.tableStudents.setHorizontalHeaderLabels(['Nome Completo', 'username'])
        self.tableStudents.setColumnWidth(0,400)
        self.tableStudents.setColumnWidth(1,300)
        self.tableStudents.setSortingEnabled(True)
        
        
        # == update table with last class ==
        if class_sel != '' :
            pos = self.lstClasses.findText(class_sel)
            if pos >= 0 :
                self.lstClasses.setCurrentIndex(pos)
        self.updateTable()

    def updateTable(self):
        self.userList=pwd.getpwall()
        self.filterOnClass(self.lstClasses.currentText())
        


    def filterOnClass(self,class_name):
        
        if class_name == '': return
        crow=-1
        self.tableStudents.clearContents()
        self.tableStudents.setRowCount(0)

        lst_grp_students = grp.getgrnam('students').gr_mem

        if grp.getgrnam(class_name) :
            grp_users = grp.getgrnam(class_name).gr_mem
        
            if grp_users:                       
                for usr in self.userList:
                    
                    if grp.getgrgid(usr[3])[0] in grp_users and grp.getgrgid(usr[3])[0] in lst_grp_students:
                        #self.tableStudents.setRowCount(100)
                                                                        
                        self.tableStudents.setRowCount(self.tableStudents.rowCount()+1)
                        crow += 1
    
                        gecos=usr.pw_gecos.split(',')
    
                        # Nome Completo                    
                        itm=QtGui.QTableWidgetItem(gecos[0])
                        itm.setFlags(itm.flags() & ~QtCore.Qt.ItemIsEditable)
                        
                        
                        self.tableStudents.setItem(crow,0,itm)
                        
                        # username                    
                        itm=QtGui.QTableWidgetItem(usr[0])
                        itm.setFlags(itm.flags() & ~QtCore.Qt.ItemIsEditable)
                        self.tableStudents.setItem(crow,1,itm)
                    
        self.tableStudents.sortByColumn(1, QtCore.Qt.AscendingOrder)        
    def fileImport(self):
        
        filename = QtGui.QFileDialog.getOpenFileName(self, "Selezionare il file", filter='*.csv') 
        
        if filename :
            print filename
            
            dlgImport = studentimport.DlgStudentImport(self, self.lstClasses.currentText(), filename)
            dlgImport.setModal(True)
            dlgImport.exec_()
            
            # == update system user list ==
            print "DBG >> update!"
            self.userList=pwd.getpwall()
            self.updateTable()
            
            
    def modPasswd(self):
        if self.tableStudents.currentRow() >= 0 :
            usr_name = self.tableStudents.item(self.tableStudents.currentRow(),1).text()
            
            usr_manager = UserManager(self)
            usr_manager.changePassword(usr_name)
            
        else:
            QtGui.QMessageBox.warning(self, "Modifica Password", "Selezionare un utente nella tabella! ") 
            
        
    def modUser(self):
        pass
        #TODO: completare!!!!
        
    def addUser(self):
        dlg_mod = studentmod.DlgStudentMod(self, self.lstClasses.currentText())
        dlg_mod.setModal(True)
        ret = dlg_mod.exec_()
        if ret == 0:
            self.updateTable()
        
        
    def delUser(self):
        if self.tableStudents.currentRow() >= 0 :
            usr_name = self.tableStudents.item(self.tableStudents.currentRow(),1).text()
            
            usr_manager = UserManager(self)
            ret = usr_manager.deleteUser(usr_name)
            
            if ret == 0 :
                self.updateTable()
            
            
        else:
            QtGui.QMessageBox.warning(self, "Modifica Password", "Selezionare un utente nella tabella! ") 
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWindow = DlgStudentManager(None,  sys.argv[1])
    mainWindow.show()
    sys.exit(app.exec_())
