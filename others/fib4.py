from sys import argv
from threading import Thread

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


t1 = Thread(target = fib1, args = (35, ))
t1.start()

t2 = Thread(target = fib2, args = (35, ))
t2.start()

t1.join()
t2.join()

print "done"
