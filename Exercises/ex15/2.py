print 'Enter file name which u want to open'
a = raw_input('>')

x = open(a)
print x.read()

b = raw_input('enter other\n >')

y = open(b)
print y.read()
