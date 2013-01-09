#coding=iso-8859-15
'''
Created on 04/lug/2011

@author: ivan
'''

from PyQt4 import QtGui
from PyQt4 import QtCore
import sys
import csv
import re
import subprocess



from  ui.dlgstudentimport_ui import Ui_DlgStudentImport
import commandexec

class my_unix_dialect(csv.Dialect):
    """Describe the usual properties of unix-generated CSV files."""
    delimiter = ';'
    quotechar = '\\'
    doublequote = True
    skipinitialspace = False
    lineterminator = '\n'
    quoting = csv.QUOTE_MINIMAL
    
csv.register_dialect("my_unix_dialect", my_unix_dialect)



class DlgStudentImport(QtGui.QDialog, Ui_DlgStudentImport):
    checkType = {'CHK_NAME':0,'CHK_USERNAME':1, 'CHK_GROUP':2, 'CHK_PASSWD':3}        
    fileMod = False
    fileErr = False
    className=''
    
    def __init__(self, parent, classname, filename):
        self.className = classname
        
        super(DlgStudentImport, self).__init__(parent)
        self.setupUi(self)

        #assign window's controls
        self.initUI(classname, filename)

        
    def initUI(self, classname, filename):
        self.lblClass.setText(classname)       
        
        self.filename = filename

        # == table properties ==
        self.tableStudents.clear()
        self.tableStudents.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.tableStudents.setRowCount(0)
        self.tableStudents.setColumnCount(4)
        self.tableStudents.setHorizontalHeaderLabels(['Cognome', 'Nome', 'username', 'Classe'])
        self.tableStudents.setColumnWidth(0,200)
        self.tableStudents.setColumnWidth(1,200)
        self.tableStudents.setColumnWidth(2,300)
        self.setMinimumWidth(880)
        
        self.tableLoad()
        


    def tableCheck (self):
        self.tableStudents.setAlternatingRowColors(True)
        max_row = self.tableStudents.rowCount()
        max_col = self.tableStudents.columnCount()
        self.fileErr = False 
        for row in range(0, max_row-1) :

            for col in range(0, max_col) :
                itm = self.tableStudents.item(row,col)
                if itm :
                    #print 'check for item > r-%d c%d - Item %s'% (row,col, itm.text()) 
                                    
                    if col == 0 : # Nome
                        (chk_ret, chk_str) = self.checkField(itm.text(), self.checkType['CHK_NAME'])
                    elif col == 1 : # Cognome
                        (chk_ret, chk_str) = self.checkField(itm.text(), self.checkType['CHK_NAME'])
                    elif col == 2 : # Username
                        (chk_ret, chk_str) = self.checkField(itm.text(), self.checkType['CHK_USERNAME'])
                    elif col == 3 : # Classe
                        if itm.text() and itm.text() != self.className :
                            (chk_ret, chk_str) = (2, "La classe del file non corrisponde alla classe selezionata")
                        else : 
                            (chk_ret, chk_str) = self.checkField(itm.text(), self.checkType['CHK_GROUP'])
                        
                           
                    if chk_ret == 1 :
                        # red
                        itm.setBackgroundColor(QtGui.QColor(255, 0, 0, 127))
                    elif chk_ret == 2 :                  
                        # orange
                        itm.setBackgroundColor(QtGui.QColor(255, 165, 0, 127))
                    elif chk_ret == 3 :
                        # yellow                  
                        itm.setBackgroundColor(QtGui.QColor(255, 255, 0, 127))
                    else :
                        if bool(row%2) :
                            clr = QtGui.QPalette.color(QtGui.QPalette(), QtGui.QPalette.Normal, QtGui.QPalette.Base)
                        else :
                            clr = QtGui.QPalette.color(QtGui.QPalette(), QtGui.QPalette.Normal, QtGui.QPalette.AlternateBase)
                        
                        itm.setBackgroundColor(clr)
                    
                    if chk_ret > 0 :
                        self.fileErr = True
                        
                    # tooltip
                    itm.setToolTip(chk_str)
                else :
                    itm=QtGui.QTableWidgetItem("")
                    itm.setBackgroundColor(QtGui.QColor(255, 0, 0, 127))
                    
                    itm.setToolTip("Campo non presente!")
                    self.tableStudents.setItem(row,col,itm)
                    
    def checkField(self, field, check_type):

        # == check unicode==
        #TODO: al momento uso l'errore di str(), vedere se esiste metodo ligliore
        try:
            s_field = str(field)
        except :
            return (1, "Il campo contiene dei caratteri UNICODE")
        #TODO: gestire meglio le stringhe unicode
        
        # == Check empty ==
        if s_field == "":
            return (1, "Campo vuoto")
        
        # == check lower ==
        if (check_type == self.checkType['CHK_USERNAME']) or (check_type == self.checkType['CHK_GROUP']) or (check_type == self.checkType['CHK_PASSWD']) :
            if s_field != s_field.lower():
                return (3, "Questo campo è preferibile in minuscolo")  

        # == check spaces ==
        if (check_type == self.checkType['CHK_USERNAME']) or (check_type == self.checkType['CHK_GROUP']) or (check_type == self.checkType['CHK_PASSWD']) :
            if s_field != re.sub(r'\s', '', s_field) :
                return (1, "Il campo contiene degli spazi")
        else :
            if s_field != s_field.strip() :  
                return (2, "Il campo contiene degli spazi all'inizio o alla fine")
        
        #TODO: inserire controllo caratteri non permessi in username e grp
        
        return(0,"")

    def tableItemChanged(self):
        self.fileMod = True
        
    def tableReload(self):
        if (self.fileMod) :
            retcode = QtGui.QMessageBox.warning(self, "Attenzione", "Questa operazione eliminerà tutte le modifiche effettuate!\n\n \
                 Sicuri di voler procedere?", QtGui.QMessageBox.Ok|QtGui.QMessageBox.Cancel)
        
            if retcode == QtGui.QMessageBox.Ok:
                self.tableLoad()
                
            
    def tableLoad(self):
        
        # == read csv file ==
        
        
        freader = csv.reader(open(self.filename, "rb"),  dialect= my_unix_dialect, delimiter=';')
        
        try :
            row=-1
            
            self.tableStudents.setRowCount(0)
            
            for data in freader:
                
                try:
                    self.tableStudents.setRowCount(self.tableStudents.rowCount()+1)
                    row += 1
                            
                    for col in range (0, 4):
                        if data[col]:
                            #print "row", row, "-", col, "->", data[col]
                            itm=QtGui.QTableWidgetItem(data[col])
                            self.tableStudents.setItem(row,col,itm)
                            
                    
                except IndexError, e:
                    print "ERR",e , "R/C=", row, ",", col    
                    itm=QtGui.QTableWidgetItem("")
                    itm.setBackgroundColor(QtGui.QColor(255, 0, 0, 127))
                    
                    itm.setToolTip("Campo non presente!")
                    self.tableStudents.setItem(row,col,itm)
                                    
            self.tableCheck()
                
        except csv.Error, e:
            print 'file %s, line %d: %s' % (self.filename, freader.line_num, e)
        
        self.fileMod = False
        
        #=======================================================================
        # except :
        #    print "GENERR"
        #    pass
        #=======================================================================

    def tableImport(self):
        if (self.fileErr) :
            QtGui.QMessageBox.critical(self, "Attenzione", "Impossibile eseguire l'importazione\n\nCorreggere prima tutti i campi!\n\n ")
        else :
            if self.fileMod :
                retcode = QtGui.QMessageBox.warning(self, "Attenzione", "Il file originale verrà sovrascritto con le modifiche apportate!\n\nSicuri di voler procedere?", QtGui.QMessageBox.Ok|QtGui.QMessageBox.Cancel)
                if retcode != QtGui.QMessageBox.Ok:
                    return
                
            
            #save csv anyway, to prevent line terminator issue
            self.saveCsv()
                        
            retcode = QtGui.QMessageBox.warning(self, "Attenzione", "Procedere con l'inserimento degli alunni elencati?", QtGui.QMessageBox.Ok|QtGui.QMessageBox.Cancel)
            if retcode == QtGui.QMessageBox.Ok:
                # == Execute import script ==
                print "eseguo SCRIPT!!!"
        
                exe = commandexec.execCommand()
                args='%s' % self.filename
                script = './scripts/add_students.sh'
                retcode = exe.execute(script, args)
                if retcode != 0 :
                    QtGui.QMessageBox.critical(self, "Errore", "Errore nell'esecuzione dello script di importazione  [%s %s]\n\nCodice di errore %d" % (script, args, retcode), QtGui.QMessageBox.Ok)
                else: 
                    QtGui.QMessageBox.information(self, "Comando OK", "Comando completato con successo!", defaultButton=QtGui.QMessageBox.Ok)
                    self.close()
        

    def saveCsv(self):
        # == Save the modified csv file ==
        max_row = self.tableStudents.rowCount()
        max_col = self.tableStudents.columnCount()
        fileWriter = csv.writer(open(self.filename, 'wb'), dialect=my_unix_dialect, delimiter=';')
        
        for row in range(0, max_row-1) :
            row_obj = []
            for col in range(0, max_col) :
                itm = self.tableStudents.item(row,col)
                row_obj.append(itm.text())
        
            fileWriter.writerow(row_obj)
        
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    mainWindow = DlgStudentImport(None, sys.argv[1],sys.argv[2])
    mainWindow.show()
    sys.exit(app.exec_())


