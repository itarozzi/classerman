#!/usr/bin/env python
 
from optparse import OptionParser
import os
 
def main():
 
 argParser = OptionParser()
 
 (options, args) = argParser.parse_args()
 
 for k in args:
     outfilename = '_'
     outfilename = outfilename.join(k.split('.'))
     outfilename = outfilename + '.py'
 
 
     command = 'pyuic4 -o %s %s' % (outfilename, k)
     os.system(command)
 
if __name__ == '__main__':
 main()
