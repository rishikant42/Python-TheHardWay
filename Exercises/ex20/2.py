fo = open("file.txt", "rw+")
print fo.read()
print "name of the file: ", fo.name
line = fo.readline()
print "Readline %s" %line

fo.seek(0,0)
line = fo.readline()
print "Read line : %s" %line
fo.seek(0,1)
line = fo.readline()
print "Read line : %s" %(line)
fo.seek(0,2)
line = fo.readline()

print "Read line : %s" %(line)


fo.close()
