from sys import argv
from threading import Thread
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


t1 = Thread(target = fib1, args = (35, ))

t1_start = time.time()
print "\nThread1 start at: ", time.time()
t1.start()

t2 = Thread(target = fib2, args = (35, ))

t2_start = time.time()
print "\nThread2 start at: ", time.time()
t2.start()

t1.join()
print "\nThread1 end at:", time.time() 

t2.join()
print "\nThread2 end at:", time.time()

print "\nTime taken by thread1:", time.time() - t1_start
print "\nTime taken by thread2:", time.time() - t2_start
