a = int(raw_input('?'))
b = int(raw_input('?'))

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

sum = add(a,b)
minus = sub(a,b)

print "sum = %d \nminus = %d\n" %(sum,minus)

print "%d" %(sum + minus)
