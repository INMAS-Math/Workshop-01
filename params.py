'''
A simple module to read parameter files.
Inspired from code by Hans Peter Langtangen

'''
__version__ = 0.1
__author__ = "Martin-D. Lacasse - JHU Oct. 2022"
__all__ = ['readPars', 'printPars']

import sys

def readPars(file):
    '''Read run-time parameters from a text file and return dictionary with string values'''
    try:
        file = open('parameters.txt', 'r')
    except:
        print("Unable to open file " + file, file=sys.stderr)
        sys.exit(1)

    myDico = {}
    for line in file:
        variable, value = [word.strip() for word in line.split('=')]
        variable.replace(' ', '_')
        pythoncode = "myDico['" + variable + "']='" + value + "'"
        exec(pythoncode)

    return myDico

def printPars(dico, file=sys.stdout):
    '''Print dictionary to file'''
    for key in dico:
        print(key + ' = ' + dico[key], file=file)


