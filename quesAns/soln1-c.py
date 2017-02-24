#!/usr/bin/python

import csv
from sys import argv

def countDistinctPrediction(fileName):
    inputFile = open(fileName)
    readFile = csv.reader(inputFile)

    #Skip headers from readFile
    readFile.next()

    d = {}

    for row in readFile:
        if row[4] in dict.keys(d):
            d[row[4]] += 1
        else:
            d[row[4]] = 1

    for k, v in d.iteritems():
        print "Predication: %s is counted %s times" %(k, v)

try:
    countDistinctPrediction(argv[1])
except IndexError:
    print "ERROR: Pass CSV file"

# Running instruction

# $ python soln1-c.py data.csv
