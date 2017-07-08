from sys import argv
import time

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

t1 = time.time()
fib1(35)
print "Fib1 time: ", time.time() - t1

print "\n===============================\n"

t2 = time.time()
fib2(35)
print "Fib2 time: ", time.time() - t2
