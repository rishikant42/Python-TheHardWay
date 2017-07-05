from sys import argv
from multiprocessing import Process
from multiprocessing.pool import ThreadPool

result = {}

def add(a, b):
    result['a'] = a+b

p1 = Process(target = add, args = (1, 2))
p1.start()

p1.join()


print result
