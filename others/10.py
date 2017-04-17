import numpy as np
import csv

data1 = np.genfromtxt('test.csv', delimiter=',')
data2 = np.array([[1,2,3,4,5], [9,10,11,12,13]])

files = open('test.csv')
readFile = csv.reader(files)

d = list(readFile)

data3A = [map(int, i) for i in d]
data3B = [[int(j) for j in i] for i in d]

def describe(data):
    print data
    print np.min(data)
    print np.max(data)
    print np.std(data)
    print "======================"

describe(data1)
describe(data2)
describe(data3A)
describe(data3B)
