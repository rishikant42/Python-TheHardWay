import csv

filename = 'example.csv'

with open(filename, 'rb') as f:
    reader = csv.reader(f)
    data = list(reader)

size = len(data)

for i in range(size):
    print data[i] 
