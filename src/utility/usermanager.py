#coding=iso-8859-15
'''
Created on 11/lug/2011

@author: ivan
'''

from PyQt4 import QtGui
from PyQt4 import QtCore
import pwd
import subprocess
import re

class UserManager:
    
    def __init__(self, parent_obj):
        self.parentObj = parent_obj
        self.backupPath = '/backup'
    
    def getFullName(self, usr_name):
        try :
            return pwd.getpwnam(str(usr_name))[4].split(',')[0]
        except:
            return ''
    
    
    def checkUsername(self, usrname):
        err = 0
        
        # == check unicode ==
        try:
            s_field = str(usrname)
            #TODO: trovare sistema migliore
        except :
            (err, err_msg) = (1, "Il nome utente contiene dei caratteri UNICODE")

        if err == 0 :
    
            # == Check empty ==
            if s_field == "" :
                (err, err_msg) = (2, "Il nome utente è vuoto")
            else :
                # == Check for spaces ==
                if s_field != re.sub(r'\s', '', s_field) :
                    (err, err_msg) = (3, "Il nome utente contiene degli spazi")
                    
                else :
                    # == check for lower ==
                    if s_field != s_field.lower():
                        (err,err_msg) =  (4, "Questo campo è preferibile in minuscolo")
                
        
        if err != 0 :
            QtGui.QMessageBox.warning(self.parentObj, "Gestione Utenti", err_msg, QtGui.QMessageBox.Ok)
        
        return err

    def execCommand(self, cmd):
        ret = None
        try:
            
            # == build cmd and arguments list ==
            l_cmd=cmd.split(' ')
            
            sp = subprocess.Popen(cmd, shell=True)
            while ret == None :
                ret = sp.poll()
            
            
        except:
            ret = 255

        return ret

        
    def execCommand2(self, cmd, args):
        proc = QtCore.QProcess()
        
        #proc.setStandardOutputFile("./debug.log")
        #proc.setStandardErrorFile("debug_err.log")
        print '>>>>>>>>>', cmd
        print '>>>>', args.join(' ')
        
        #proc.start(cmd, args)
        
        proc.start(cmd)
        if not proc.waitForStarted(10000):
            proc.close()
            ret= 255
        
        else :
            if not proc.waitForFinished(10000) :
                ret = 254
            else: 
                ret =  proc.exitCode()
        
        proc.close()
        return ret
        
    def changePassword(self, usr_name):

        usr_name_full = self.getFullName(usr_name)

        input_end = False
        while not input_end:
            passwd1, ok = QtGui.QInputDialog.getText(self.parentObj,"Modifica della password", "Inserire la nuova password per l'utente\n%s:" % usr_name_full, mode=QtGui.QLineEdit.Password)
            if ok:
                passwd2, ok = QtGui.QInputDialog.getText(self.parentObj,"Modifica della password", "Ripetere la nuova password per l'utente\n%s:" % usr_name_full, mode=QtGui.QLineEdit.Password)
                if ok:
                    if passwd1 == passwd2:
                        input_end = True
                        
                        # == Change password ==
                        args = QtCore.QStringList("%s:%s" % (usr_name, passwd1))
                        #cmd_ret = self.execCommand('chpasswd', args)                        
                        cmd_ret = self.execCommand('echo "%s:%s" | chpasswd' % (str(usr_name), str(passwd1)))
                        if cmd_ret == 0:
                            QtGui.QMessageBox.information(self.parentObj, "Modifica della password", "Password modificata per l'utente\n%s" % usr_name_full, QtGui.QMessageBox.Ok)
                        else:
                            QtGui.QMessageBox.warning(self.parentObj, "Errore!", "Errore nell'esecuzione del comando \nCodice di errore %d" % cmd_ret, QtGui.QMessageBox.Ok)

                    else :
                        QtGui.QMessageBox.warning(self.parentObj, "Modifica della password", "Le due password non coincidono\nripetere l'inserimento:", QtGui.QMessageBox.Ok)
                else:input_end = True
            else: input_end = True
            
    def deleteUser(self, usr_name):
        usr_name_full = self.getFullName(usr_name)
        cmd_ret = -1
        retcode = QtGui.QMessageBox.warning(self.parentObj, "Eliminazione Utente", "Sicuri di voler cancellare l'utente %s?\n\nATTENZIONE:\nLa cancellazione dell'utente non sarà  reversibile!" % usr_name_full, QtGui.QMessageBox.Ok|QtGui.QMessageBox.Cancel, defaultButton=QtGui.QMessageBox.Cancel)

        if retcode == QtGui.QMessageBox.Ok:         
            #TODO: richiedere password admin di conferma?!?
            
            cmd_ret = self.execCommand('deluser %s --remove-home --backup --backup-to %s' % (usr_name, self.backupPath))
            #TODO: il path di backup dovrebbe essere assegnato in maniera flessibile!!! 
                                                
            if cmd_ret == 0:
                QtGui.QMessageBox.information(self.parentObj, "Eliminazione Utente", "L'utente %s è stato eliminato\n\nUn backup dei suoi dati è disponibile in %s" % (usr_name_full, self.backupPath), QtGui.QMessageBox.Ok)
            else:
                QtGui.QMessageBox.warning(self.parentObj, "Eliminazione Utente!", "Errore nell'esecuzione del comando \nCodice di errore %d" % cmd_ret, QtGui.QMessageBox.Ok)

        return cmd_ret