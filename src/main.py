#! /usr/bin/env python
#coding=iso-8859-15



'''
  Copyright 2011 Ivan Tarozzi <itarozzi@gmail.com>  
  All rights reserved.

 This file is part of classerman project.

    classerman is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    classerman is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with classerman.  If not, see <http://www.gnu.org/licenses/>.
'''

'''
Created on 21/giu/2011

@author: ivan
'''




import sys
import subprocess
import ctypes, os

import commandexec

import datetime

from utility.systemsecurity import SystemSecurity

from PyQt4 import QtGui
from PyQt4 import QtCore


from  ui.mainwindow_ui import Ui_MainWindow

from studentmanager import DlgStudentManager 
from teachermanager import DlgTeacherManager 


class MainWindow(QtGui.QMainWindow, Ui_MainWindow) :
    ROOT_CHECK = False
    
    scripts = {'endyear_backup':'./scripts/endyear_backup.sh',
               'newyear':'./scripts/newyear.sh','test1':'./scripts/testscript1.sh' }
    CUR_STATE={'init':0, 'active':1, 'saved':2}
        
    def __init__(self, parent):

        self.version='beta20120116'
        self.title = ""
        self.curYear = ""
        self.curState = 0
        self.cmdAdvUser = ""
        self.serverId = ""
        self.lastClass = ''
        
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


        #self.dlgStudentManager = DlgStudentManager(self)

        
        if self.ROOT_CHECK :    
            if os.getuid() != 0 :
                QtGui.QMessageBox.warning(self, "Attenzione", "Questo programma puo' essere eseguito solo con i privilegi di amminstratore!", QtGui.QMessageBox.Ok)
                sys.exit(1)


        #load configuration file
        self.loadConf()
        
        #assign window's controls
        self.initUI()
        
    def initUI(self):
        # Window Size and Position
        screen = QtGui.QDesktopWidget().screenGeometry()
        QtGui.QDesktopWidget().availableGeometry(1)

        # Set main windows properties        
        self.resize(1024,768)
        self.setWindowTitle(self.title + ' - Versione: %s' % self.version)
        
        
        self.labelServerId.setText(self.serverId)
        self.updateUI()
    
    def updateUI(self):
        if (self.curYear != "") and (self.curState != 0) :
            self.labelYear.setText("Anno %s "%self.curYear) 
        else :
            self.labelYear.setText("Anno ---")
        
        # == check for state ==
        self.btnNewYear.setEnabled(self.curState != self.CUR_STATE['active'])
        self.btnCloseYear.setEnabled(self.curState > self.CUR_STATE['init'])
        self.btnStudents.setEnabled(self.curState > self.CUR_STATE['init'])
        self.btnTeachers.setEnabled(self.curState > self.CUR_STATE['init'])
        
        #TODO: assign status bar
        
        
    def loadConf(self):
        settings = QtCore.QSettings( "classerman.conf", QtCore.QSettings.NativeFormat );
        
        self.title = settings.value("Global/title", "classerman").toString()
        self.serverId = settings.value("Global/server_id", "--").toString()
        self.curYear = settings.value("Current/year", "").toString()
        self.curState = settings.value("Current/state", 0).toInt()[0]
        
        self.cmdAdvUser = settings.value("Commands/user_manager", "kuser").toString()
        
        self.pathBackup = settings.value("Path/backup", "/backup").toString()
        
        
        #TODO: controllo la presenza di kuser


    def saveConf(self, key, value):
        settings = QtCore.QSettings( "classerman.conf", QtCore.QSettings.NativeFormat );
        settings.setValue(key, value)
        if settings.status() != QtCore.QSettings.NoError :
                QtGui.QMessageBox.critical(self, "Errore", "Errore nell ascrittura del file di configurazione \n [%s ]\n\nCodice di errore 255" % (key), QtGui.QMessageBox.Ok)
         
        
    def execAdvancedUserManager(self):
        retcode = 0
        try:
            subprocess.Popen("%s" % self.cmdAdvUser)
        except :
            retcode = 255
            
        if retcode != 0 :
            
            QtGui.QMessageBox.warning(self, "Errore", "Errore nell'esecuzione del comando [%s]\nCodice di errore %d" % (self.cmdAdvUser,retcode), QtGui.QMessageBox.Ok)

    def execYearNew(self):
        retcode = QtGui.QMessageBox.warning(self, "Attenzione", "L'avvio di un nuovo anno cancelelrà  tutti i dati dell'anno precedente!\nAccertarsi di avere eseguito il backup dell'anno precedente/in corso prima di procedere!\n\nSicuri di voler procedere?", QtGui.QMessageBox.Ok|QtGui.QMessageBox.Cancel)
        
        if retcode == QtGui.QMessageBox.Ok:
            
            # == build tear list == 
            year_list = QtCore.QStringList()
            for y in range (2010, 2050):
                year_list.append(str(y))

            # == search for current year ==
            now = datetime.datetime.now()

            year_sel, ok = QtGui.QInputDialog.getItem(self, "Nuovo Anno Scolatico", "Selezionare l'anno di inizio anno scolastico: ", year_list, current=now.year-2010 )
            year_sel = year_sel.toInt()[0]

            if ok:
                # == ask if sure :) ==
                retcode = QtGui.QMessageBox.critical(self, "Attenzione", "Sicuri di voler procedere alla creazione del nuovo anno scolastico %d-%d ?\n\nTutti i dati attuali verranno cancellati!" % (year_sel, year_sel+1), QtGui.QMessageBox.Ok|QtGui.QMessageBox.Cancel)        
                if retcode == QtGui.QMessageBox.Ok:
            
                    password, ok = QtGui.QInputDialog.getText(self, "Nuovo Anno Scolatico", "Inserire la password di amministrazione: ", QtGui.QLineEdit.Password) 

                    if ok:
                        # == check for password and execute the script ==
                        
                        sec = SystemSecurity()
                        
                        #FIXME: debug!!!!
                        #ret = True
                        ret = sec.checkCurrentUserPassword(password)
                        
                        
                        if not ret:
                            QtGui.QMessageBox.critical(self, "Errore", "Password non corretta! ", QtGui.QMessageBox.Ok)    
                            return
                            #TODO: ciclare nella richiesta password
                        
                        exe = commandexec.execCommand()
                        args='%s-%s a p' % (year_sel, year_sel+1) #per il momento sono gestite solo le sezioni dalla a alla p
                        retcode = exe.execute(self.scripts['newyear'], args)
                        if retcode != 0 :
                            QtGui.QMessageBox.critical(self, "Errore", "Errore nell'esecuzione dello script di avvio nuovo anno [%s %s]\n\nCodice di errore %d" % (self.scripts['newyear'], args, retcode), QtGui.QMessageBox.Ok)
                        else: 
                            QtGui.QMessageBox.information(self, "Comando OK", "Comando completato con successo!\n\nOra configurare insegnanti ed alunni delle singole classi", defaultButton=QtGui.QMessageBox.Ok)
                            
                            # == update configuration file and gui ==
                            self.curState = self.CUR_STATE['active']
                            self.saveConf('Current/state', self.curState)
                                                        
                            self.curYear = '%s-%s' % (year_sel, year_sel+1)
                            self.saveConf('Current/year', self.curYear)
                            
                            self.updateUI()
                        
                                
            
    def execYearEnd(self):
        retcode = QtGui.QMessageBox.warning(self, "Attenzione", "La chiusura dell'anno scolastico deve essere eseguita\nsolo al termine delle attività  annuali\n\nSicuri di voler procedere?", QtGui.QMessageBox.Ok|QtGui.QMessageBox.Cancel)
        
        if retcode == QtGui.QMessageBox.Ok:
            exe = commandexec.execCommand(self)
            
            args = '%s/%s' % (self.pathBackup, self.curYear)
            retcode = exe.execute(self.scripts['endyear_backup'], args)
            #retcode = exe.execute(self.scripts['test1'], '3')
            
            if retcode != 0 :
                QtGui.QMessageBox.critical(self, "Errore", "Errore nell'esecuzione dello script di chiusura anno [%s %s]\n\nCodice di errore %d" % (self.scripts['endyear_backup'], args, retcode), QtGui.QMessageBox.Ok)
            else: 
                QtGui.QMessageBox.information(self, "Comando OK", "Comando completato con successo", defaultButton=QtGui.QMessageBox.Ok)
                
                # change year state from 1 (active) to 2 (saved)
                self.curState = self.CUR_STATE['saved']
                self.saveConf('Current/state', self.curState) 
                self.updateUI()
                  
            print "retcode = %d"%retcode

    def showStudentsManager(self):
        dlg_student = DlgStudentManager(self, self.lastClass)
        dlg_student.setModal(True)
        ret = dlg_student.exec_()
        self.lastClass = dlg_student.lstClasses.currentText() 
        

    def showTeachersManager(self):
        dlg_teacher = DlgTeacherManager(self)
        dlg_teacher.setModal(True)
        ret = dlg_teacher.exec_()
    

    def showArchBackup(self):
        os.system('xdg-open "%s"' % self.pathBackup)

            
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    mainWindow = MainWindow(None)
    mainWindow.show()
    sys.exit(app.exec_())
