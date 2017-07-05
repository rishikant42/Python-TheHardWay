from multiprocessing import Process

def fib1(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a

def fib2(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a

p1 = Process(target = fib1, args = (500000, ))
p1.start()

p2 = Process(target = fib2, args = (500000, ))
p2.start()

p1.join()
p2.join()

print "done"
