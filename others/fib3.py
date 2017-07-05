from sys import argv

def fib1(n):
    if n < 2:
        return n
    else: 
        return fib1(n-1) + fib1(n-2)

def fib2(n):
    if n < 2:
        return n
    else: 
        return fib2(n-1) + fib2(n-2)

fib1(35)
fib2(35)

print "Done"
