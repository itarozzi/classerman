#coding=iso-8859-15
'''
Created on 11/lug/2011

@author: ivan
'''

from PyQt4 import QtGui
from PyQt4 import QtCore

from  ui.dlgteachermod_ui import Ui_DlgTeacherMod
from utility.usermanager  import UserManager


class DlgTeacherMod(QtGui.QDialog, Ui_DlgTeacherMod):
    def __init__(self, parent):
        super(DlgTeacherMod, self).__init__(parent)
        self.setupUi(self)
        
        # == build the classroom list ==
        for i in range(ord('a'), ord('p')+1):
            for j in range(1, 4):
                class_name = "classe_%d%s" % (j, chr(i))
                
                item = QtGui.QListWidgetItem(class_name)
                item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                #item.setFlags(item.flags() & QtCore.Qt.ItemIsSelectable)
                item.setCheckState(QtCore.Qt.Unchecked)
                self.lstClasses.addItem(item)
                 
                #self.lstClasses.addItems(class_name)

    def buildUsername(self):
        surname=self.editSurname.text().toLower().normalized(0)
        name=self.editName.text().toLower().normalized(0)
                         
        self.editUsername.setText( (surname+name).replace(' ', '') )

        usr_manager = UserManager(self)
        usr_manager.checkUsername(self.editUsername.text())

    
    def accept(self):
        usr_manager = UserManager(self)

           
        # == check for fields ==
        ret = usr_manager.checkUsername(self.editUsername.text())

        classes_list = ''
        for i in range(0, self.lstClasses.count()) :
            item = self.lstClasses.item(i)
            
            if item.checkState() == QtCore.Qt.Checked :
                classes_list = classes_list + item.text() + ' '

        if self.editName.text() and self.editSurname.text() and classes_list != '' :
            if ret == 0:
                script = './scripts/add_teachers.sh'
                #TODO: parametrizzare questo da file cfg!!!
    
                
                
                args = '%s;%s;%s;%s' % (self.editSurname.text().trimmed(), self.editName.text().trimmed(), self.editUsername.text().trimmed(), classes_list)
                cmd =  'echo "' + args +'" | '+ script
    
                print args
                
                #TODO: armonizzare uso di execCommand anche con studentimport e modulo commandexec !!!
                ret = usr_manager.execCommand(cmd)            
                if ret != 0 :
                    QtGui.QMessageBox.critical(self, "Errore", "Errore nell'inserimento dell'utente!\n\nCodice di errore %d" % (ret), QtGui.QMessageBox.Ok)
                    return -1
                else: 
                    QtGui.QMessageBox.information(self, "Gestione Utenti", "Inserimento utente completato con successo!", defaultButton=QtGui.QMessageBox.Ok)
                    QtGui.QMessageBox.information(self, "Gestione Utenti", "Attualmente la password è impostata al valore di default stabilito dalle policy di sistema\nSi consiglia di provvedere alla personalizzazione delle singole password al fine di aumentare la sicurezza dei dati degli utenti!", defaultButton=QtGui.QMessageBox.Ok)
                    self.close()
                    return 0
        
        else:
            QtGui.QMessageBox.warning(self, "Gestione Utenti", "Completare tutti i campi ed associare almeno una classe!", defaultButton=QtGui.QMessageBox.Ok)
    
        
        

