import datetime
from os.path import exists
import getopt
import sys

if exists('Lab1/log.txt'):
    previousLogFile = open('Lab1/log.txt', 'r')
    logFile = open('Lab1/log.txt', 'w')
else:
    logFile = open('Lab1/log.txt', 'x')


def RunFromTerminal():
    lastInput = ""
    userInput = ""

    while lastInput.lower() != "exit":
        previousLogFile = open('Lab1/log.txt', 'r').readlines()
        logFile = open('Lab1/log.txt', 'w')
        userInput = input(
            "Write 'exit(e)' to close\nwrite something to the log file:\n>")
        lastInput = userInput
        if lastInput == 'exit' or lastInput == 'e':
            for value in previousLogFile:
                logFile.write(value)
            continue
        endFormat = datetime.datetime.now().strftime("%X")
        for value in previousLogFile:
            logFile.write(value)
        logFile.writelines(endFormat+": "+userInput+"\n")
        logFile.close()
        previousLogFile = open('Lab1/log.txt', 'r').readlines()
        for line in previousLogFile:
            print(line)

    logFile.close()


if len(sys.argv) <= 1:
    RunFromTerminal()

elif len(sys.argv) > 1:
    argList = sys.argv[1:]
    options = "m:"
    longOptions = ["Message"]
    arguments, values = getopt.getopt(argList, options, longOptions)
    for currentArgument, currentValue in arguments:
        if currentArgument in ('-m', '--Message'):
            endFormat = datetime.datetime.now().strftime("%X")
            logFile.write(f"{endFormat} {currentValue}\n")
    logFile.close()
