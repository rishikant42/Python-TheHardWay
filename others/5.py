#!/usr/bin/python

import csv

def rowCounting(fileName):

    inputFile = open(fileName)
    readFile = csv.reader(inputFile)

    for row in readFile:
        print('Row #' + str(readFile.line_num) + ' ' + str(row))

rowCounting('example.csv')
