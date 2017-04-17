d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

for k,v in d.iteritems():
    print k, " ==> ", v

print "=============================="

for k in d:
    print k, " ==> ", d[k]
