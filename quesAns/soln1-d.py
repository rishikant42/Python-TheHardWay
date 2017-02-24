#!/usr/bin/python

import csv
from sys import argv

def writeFile(fileName):

    inputFile = open(fileName)
    readFile = csv.reader(inputFile)

    #Skip headers from readFile
    readFile.next()

    outputFile = open('output.csv', 'w')
    outputWriter = csv.writer(outputFile)
    
    # Make Headers
    outputWriter.writerow(['Predication', "Count value"])

    d = {}

    for row in readFile:
        if row[4] in dict.keys(d):
            d[row[4]] += 1
        else:
            d[row[4]] = 1

    for k, v in d.iteritems():
        outputWriter.writerow([k, v])
        
    outputFile.close()

try:
    writeFile(argv[1])
    print "File: output.csv is successfully created."
except IndexError:
    print "ERROR: Pass CSV file"

# Running instruction

# $ python soln1-d.py data.csv
