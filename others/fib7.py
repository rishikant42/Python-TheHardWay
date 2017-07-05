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

fib1(500000)
fib2(500000)

print "Done"
