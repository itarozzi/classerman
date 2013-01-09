#coding=iso-8859-15
'''
Created on 11/lug/2011

@author: ivan
'''

from PyQt4 import QtGui
from PyQt4 import QtCore

from  ui.dlgstudentmod_ui import Ui_DlgStudentMod
from utility.usermanager  import UserManager


class DlgStudentMod(QtGui.QDialog, Ui_DlgStudentMod):
    def __init__(self, parent, class_name):
        super(DlgStudentMod, self).__init__(parent)
        self.setupUi(self)
        
        self.className = class_name

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

        if ret == 0:
            script = './scripts/add_students.sh'
            #TODO: parametrizzare questo da file cfg!!!
            
            args = '%s;%s;%s;%s' % (self.editSurname.text().trimmed(), self.editName.text().trimmed(), self.editUsername.text().trimmed(), self.className.trimmed())

            cmd =  'echo "' + args +'" | '+ script

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
        
    
        
        

