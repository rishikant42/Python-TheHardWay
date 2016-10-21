from sys import argv
from os.path import exists

script, file1, file2 = argv

a = open(file1)
x = a.read()
print x

print "copy %r > %r" %(file1, file2)
print "check whether %r exist? %r" %(file2, exists(file2))

print "hit enter if %r is not exist" %file2
raw_input()
b = open(file2,'w')
b.write(x)

a.close()
b.close()
