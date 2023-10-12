#!/usr/bin/env python3
'''
A prototypical main file with parameters from command line arguments
Martin-D. Lacasse, JHU 2022
'''

import sys
import params 

# Print Usage
def printHelp(name):
    print("Usage: ", name, "filename.par")
    sys.exit(1)


def run():
    try:
        filename = sys.argv[1]
    except:
        printHelp(sys.argv[0])

    myDico = params.readParameters(filename)
    params.printParameters(myDico)

#####################################################################
# This is the main program
if __name__ == '__main__':

    run()

else:
    print("Error: Can't import main script as a module.", repr(__name__))

