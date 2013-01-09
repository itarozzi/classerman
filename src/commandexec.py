# -*- coding: utf-8 -*-
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
Created on 24/giu/2011

@author: ivan
'''

from PyQt4 import QtGui
from PyQt4 import QtCore

import time
import subprocess 

#TODO: redirect stdout/stderr to log file


class execCommand (QtCore.QObject) :

    #proc = QtCore.QProcess()
    def __init__(self, dlg_parent=None):
        self.dlgParent = dlg_parent
        self.proc = QtCore.QProcess()
        

    def execute(self, command, args):
        ret = None

                
        QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        
        try:
        
            cmd = command + ' ' + args
            print '>>>>EXECUTE:', cmd     
            
            sp = subprocess.Popen(cmd, shell=True)
            while ret == None :
                ret = sp.poll()
            
            
        except:
            ret = 255

        QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

        return ret
        
    def execute_OLD(self, command, args):

        # == assign command and arguments ==
        program = QtCore.QString(command)

        # == start the process ==        
        self.proc.start(command, QtCore.QString(args).split(" "))
        if not self.proc.waitForStarted(1000):
            print "Avvio ERR"
            ret= 255
            QtGui.QMessageBox.warning(None, "Errore!", "Errore nell'esecuzione del comando [%s]\nCodice di errore %d" % (command,ret), QtGui.QMessageBox.Ok)
            return ret
        
        # build the progress dialog
        self.progress = QtGui.QProgressDialog()
        self.progress.setMinimum(0)
        self.progress.setMaximum(10)
        self.progress.setWindowTitle("Esecuzione del comando")
        self.progress.setLabelText("Avvio")
        self.progress.setAutoClose(True)
        self.progress.setWindowModality(QtCore.Qt.WindowModal);
        #self.progress.setModal(True)
        QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        
        while  self.proc.waitForReadyRead(msecs=1000):
            self.progress.setValue(self.progress.value()+1)
            stdout_line=  self.proc.readLine()
            print stdout_line
        
        print self.proc.readAll()
        self.progress.hide()
        
        ret = self.proc.exitCode()
        print "RETURN IS:"
        print ret
        
        QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        return ret
