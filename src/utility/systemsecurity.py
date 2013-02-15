'''
Created on 28/giu/2011

@author: ivan
'''

import pwd
import os
import crypt
import spwd
import getpass

class SystemSecurity():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''

    def checkCurrentUserPassword(self, password):
        '''
        Check if password entry is correct
        '''
        #uid = os.getuid()
        #name=pwd.getpwuid(uid)[0]

        # Get name of current sudo user 
        name = os.getenv("SUDO_USER")


        
        spwd.getspall()
        user_pwd = spwd.getspnam(name)[1]



        crypt_pwd = crypt.crypt(str(password), user_pwd) 
        

        return crypt_pwd  == user_pwd
    

        