from sys import argv
from multiprocessing import Process
from multiprocessing.pool import ThreadPool

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


pool = ThreadPool(processes=2)
async_result = pool.apply_async(fib1, (35,))
async_resul = pool.apply_async(fib2, (35, ))

return_val = async_result.get()
return_va = async_resul.get()
print return_val
print return_va
