import unicodecsv

with open('example.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)

    for row in reader:
        print row

f.close()
