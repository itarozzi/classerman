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

from  ui.dlgteachermanager_ui import Ui_DlgTeacherManager

import studentimport
import teachermod

from utility.usermanager  import UserManager

class DlgTeacherManager(QtGui.QDialog, Ui_DlgTeacherManager):
    
    def __init__(self, parent):
        super(DlgTeacherManager, self).__init__(parent)
        self.setupUi(self)

        #assign window's controls
        self.initUI()
        
    def initUI(self):

        # == update system user list ==
        self.userList=pwd.getpwall()
            
        # == table properties ==
        self.tableTeachers.setColumnCount(2)
        self.tableTeachers.setRowCount(0)
        self.tableTeachers.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.tableTeachers.setHorizontalHeaderLabels(['Nome Completo', 'username'])
        self.tableTeachers.setColumnWidth(0,400)
        self.tableTeachers.setColumnWidth(1,300)
        self.tableTeachers.setSortingEnabled(True)
        
        self.updateTable()
        self.tableTeachers.selectRow(0)
        if self.tableTeachers.rowCount() > 0:
            selected_user = self.tableTeachers.selectedItems()[1].text()
            self.updateClassroomList(selected_user)
        
    def tableChanged(self):
        if self.tableTeachers.selectedItems() :
            selected_user = self.tableTeachers.selectedItems()[1].text()
            self.updateClassroomList(selected_user)
        
    def updateTable(self):
        self.userList=pwd.getpwall()

        crow=-1
        self.tableTeachers.clearContents()
        self.tableTeachers.setRowCount(0)

        if grp.getgrnam('teachers') :
            grp_users = grp.getgrnam('teachers').gr_mem
            
            if grp_users:                       
                for usr in self.userList:
                    
                    if grp.getgrgid(usr[3])[0] in grp_users:
                        #self.tableTeachers.setRowCount(100)
                                                                        
                        self.tableTeachers.setRowCount(self.tableTeachers.rowCount()+1)
                        crow += 1
    
                        gecos=usr.pw_gecos.split(',')
    
                        # Nome Completo                    
                        itm=QtGui.QTableWidgetItem(gecos[0])
                        itm.setFlags(itm.flags() & ~QtCore.Qt.ItemIsEditable)
                        
                        
                        self.tableTeachers.setItem(crow,0,itm)
                        
                        # username                    
                        itm=QtGui.QTableWidgetItem(usr[0])
                        itm.setFlags(itm.flags() & ~QtCore.Qt.ItemIsEditable)
                        self.tableTeachers.setItem(crow,1,itm)
                    
        self.tableTeachers.sortByColumn(1, QtCore.Qt.AscendingOrder)        



    def updateClassroomList(self, username):
        # == populate classes list ==
        self.lstClasses.clear()
        
        print username
        
        pos=0
        idx_sel = 0
        
        for i in range(ord('a'), ord('p')+1):
            for j in range(1, 4):
                grp_name = "classe_%d%s" % (j, chr(i))
                
                if grp.getgrnam(grp_name) :
                    grp_users = grp.getgrnam(grp_name).gr_mem

                    if grp_users:
                    
                        if username in grp_users:
                            self.lstClasses.addItem(grp_name)


    def filterOnClass(self,class_name):
        pass

    def assignClassroom(self):
        #TODO: COMPLETARE FUNZIONALITA'!!!
        QtGui.QMessageBox.warning(self, "Warning", "Funzione non ancora implementata!")
        return
    
    
    def fileImport(self):
        #TODO: COMPLETARE FUNZIONALITA'!!!
        QtGui.QMessageBox.warning(self, "Warning", "Funzione non ancora implementata!")
        return
        
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
        if self.tableTeachers.currentRow() >= 0 :
            usr_name = self.tableTeachers.item(self.tableTeachers.currentRow(),1).text()
            
            usr_manager = UserManager(self)
            usr_manager.changePassword(usr_name)
            
        else:
            QtGui.QMessageBox.warning(self, "Modifica Password", "Selezionare un utente nella tabella! ") 
            
        
    def modUser(self):
        pass
        #TODO: completare!!!!
        
    def addUser(self):
        dlg_mod = teachermod.DlgTeacherMod(self)
        dlg_mod.setModal(True)
        ret = dlg_mod.exec_()
        if ret == 0:
            self.updateTable()
            self.tableTeachers.selectRow(0)
        
        
    def delUser(self):
        if self.tableTeachers.currentRow() >= 0 :
            usr_name = self.tableTeachers.item(self.tableTeachers.currentRow(),1).text()
            
            usr_manager = UserManager(self)
            ret = usr_manager.deleteUser(usr_name)
            
            if ret == 0 :
                self.updateTable()
            
            
        else:
            QtGui.QMessageBox.warning(self, "Modifica Password", "Selezionare un utente nella tabella! ") 
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWindow = DlgTeacherManager(None)
    mainWindow.show()
    sys.exit(app.exec_())
