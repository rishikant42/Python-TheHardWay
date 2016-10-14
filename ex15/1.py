from sys import argv
script, file = argv
txt = open(file)
print "here is discription of %s" %file
print txt.read()

print "print file name again"
again = raw_input('?')
now = open(again)
print now.read()
