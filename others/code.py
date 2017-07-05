from sys import argv
from multiprocessing import Process
from multiprocessing.pool import ThreadPool

def add(a, b):
    return a+b

p1 = Process(target = add, args = (1, 2))
p1.start()

p1.join()

pool = ThreadPool(processes=2)

async_result = pool.apply_async(add, (1, 2))
async_resul = pool.apply_async(add, (3, 2))

return_val = async_result.get()
return_va = async_resul.get()
print return_val
print return_va
