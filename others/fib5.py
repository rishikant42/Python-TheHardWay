from sys import argv
from multiprocessing import Process

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


p1 = Process(target = fib1, args = (35, ))
p1.start()

p2 = Process(target = fib2, args = (35, ))
p2.start()

p1.join()
p2.join()

print "done"
