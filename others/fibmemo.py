from sys import argv

fib_cache = {}

def fib(n):
    if n in fib_cache:
        return fib_cache[n]
    elif n < 2:
        fib_cache[n] = n
        return fib_cache[n]
    else:
        fib_cache[n] = fib(n-1) + fib(n-2)
        return fib_cache[n]


print fib(int(argv[1]))
