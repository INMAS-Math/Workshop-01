#!/usr/bin/env python3

# A prototypical main file with parameters from command line arguments
# Martin-D. Lacasse, JHU 2022

import sys
import getopt
import params

# Print Usage
def printHelp(name):
    print("Usage: ", name, "-[h] [-a a_param] [-b b_param] [-c c_param] [-s _sourceCode] [-d DesiredOutcom] -f [file]")
    sys.exit(1)

# Parse options from command line
def processCommandLineArgs(argv):
    progName = argv[0]
    argList =  argv[1:]
    # Default values
    a, b, c, sourceCode, desiredOutcome = 0, 0, 0, 'none', 'failure'

    # Options
    options = "ha:b:c:s:d:"
 
    # Long options for parameter
    longOptions = ["help", "a=", "b=", "c==", "d=", "s="]
 
    try:
        # Parsing arguments
        opts, vals = getopt.getopt(argList, options, longOptions)
     
        # Checking each argument
        for opt, val in opts:
            if opt in ("-h", "--help"):
                printHelp(progName)
            elif opt in ("-a", "--a"):
                a = int(val)
            elif opt in ("-b", "--b"):
                b = int(val)
            elif opt in ("-c", "--c"):
                c = int(val)
            elif opt in ("-s", "--sourceCode"):
                sourceCode = val
            elif opt in ("-d", "--desiredOutcome"):
                desiredOutcome = val

    except getopt.error as err:
            print(str(err))
            printHelp(progName)
            sys.exit(2)

    # print("Opt is", opt) 
    # print("Val is", val)
    return a, b, c, sourceCode, desiredOutcome

def run():
    a, b, c, sourceCode, desiredOutcome = processCommandLineArgs(sys.argv)
    print('Arguments are:', 'a=',a, 'b=', b, 'c=', c, 'sourceCode=', sourceCode, 'desiredOutcom=', desiredOutcome)
    

#####################################################################
# This is the main program
if __name__ == "__main__":

    run()

else:
    print("Error: Can't import main script as a module.", repr(__name__))

