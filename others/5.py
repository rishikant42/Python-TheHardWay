#!/usr/bin/python

import csv
from sys import argv

def rowCounting(fileName):

    inputFile = open(fileName)
    readFile = csv.reader(inputFile)

    for row in readFile:
        print('Row #' + str(readFile.line_num) + ' ' + str(row))

try:
    rowCounting(argv[1])
except IndexError:
    print "ERROR: Pass csv file from command line"
