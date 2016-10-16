def print_two(*argv):
    argv1, argv2 = argv
    print 'argv1 = %r  argv2 = %r' %(argv1, argv2)
def print_otr(argv1, argv2):
    print 'argv1 = %r  argv2 = %r' %(argv1, argv2)
def print_one(argv1):
    print 'argv1 = %r' %argv1
def print_none():
    print'nothing here'


print_two('rishi','lokesh')
print_otr('rishi','lokesh')
print_one('rishi')
print_none()
