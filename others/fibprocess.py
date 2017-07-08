from sys import argv
from multiprocessing import Process
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


p1 = Process(target = fib1, args = (35, ))

t1_start = time.time()
print "\nProcess1 start at: ", time.time()
p1.start()

p2 = Process(target = fib2, args = (35, ))

t2_start = time.time()
print "\nProcess2 start at: ", time.time()
p2.start()

p1.join()
print "\nProcess1 end at:", time.time() 

p2.join()
print "\nprocess2 end at:", time.time()

print "\nTime taken by process1:", time.time() - t1_start
print "\nTime taken by process2:", time.time() - t2_start
