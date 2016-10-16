from sys import argv
script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print line_count, f.readline()


file = open(input_file)

print "file there is complt file"

print_all(file)

print "now rewind this file"
 
rewind(file)

print "print three lines of file"

line = 1
print_a_line(line,file)

line += 1
print_a_line(line,file)

line += 1
print_a_line(line,file) 
