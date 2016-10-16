from sys import argv
from os.path import exists

script, from_file, to_file = argv
print 'coping from %s to %s' %(from_file,to_file)

in_file = open(from_file)
indata = in_file.read()

print 'the input of file is %d byte yeild' %len(indata)
print 'does output is already exists? %r' %exists(to_file)

print 'press ctrl-c if exist otherwise hit return'
raw_input()

out_file = open(to_file,'w')
out_file.write(indata)

print 'alright done'

out_file.close()
in_file.close()
