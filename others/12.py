def fib1(n):
    if n<2:
        return n
    else:
        return fib1(n-1) + fib1(n-2)

print fib1(36)

fibcache = {}
def fib2(n):
    if n in fibcache:
        return fibcache[n]
    else:
        if n < 2:
            fibcache[n] = n
        else:
            return fib2(n-2) + fib2(n-1)
        
        return fibcache[n]

print fib2(36)
