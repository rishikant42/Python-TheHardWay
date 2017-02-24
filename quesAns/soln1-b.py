#!/usr/bin/python

import csv
from sys import argv

def distinctPrediction(fileName):
    inputFile = open(fileName)
    readFile = csv.reader(inputFile)

    #Skip headers from readFile
    readFile.next()

    distictPredication = []

    for row in readFile:
        if row[4] not in distictPredication:
            distictPredication.append(row[4])

    for x in distictPredication:
        print x

try:
    distinctPrediction(argv[1])
except IndexError:
    print "ERROR: Pass CSV file"

# Running instruction

# $ python soln1-b.py data.csv
