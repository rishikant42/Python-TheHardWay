a = raw_input('file1?')
x = open(a)

b = raw_input('file2?')
y = open(b,'w')
y.truncate()

c = raw_input('file3?')
z = open(c,'w')
z.truncate()
line = raw_input()
z.write(line)
z.close()
