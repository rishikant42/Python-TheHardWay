from sys import argv
from multiprocessing import Process

def fib(n):
    if n < 2:
        return n
    else: 
        return fib(n-1) + fib(n-2)

p1 = Process(target = fib, args = (35, ))
p1.start()

p2 = Process(target = fib, args = (35, ))
p2.start()

p1.join()
p2.join()

print "Done"
