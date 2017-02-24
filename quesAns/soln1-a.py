#!/usr/bin/python

import csv
from sys import argv

def rowCounting(fileName):
    inputFile = open(fileName)
    readFile = csv.reader(inputFile)

    #Skip headers from readFile
    readFile.next()

    numberOfRows = 0

    for row in readFile:
        if row[4] != 'None':
            numberOfRows += 1

    print "No. of Rows (where predication is not 'None') are", numberOfRows

try:
    rowCounting(argv[1])
except IndexError:
    print "ERROR: Pass CSV file from command line"

# TEST

# $ python soln1-a.py data.csv 
# No. of Rows (where predication is not 'None') are 164
