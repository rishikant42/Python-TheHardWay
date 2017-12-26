import time

def timing_fn(f):

    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        return "Time Taken: " + str(t2 - t1) + "\n"

    return wrapper

@timing_fn
def my_fn():
    num_list = []
    for num in range(0, 10000):
        num_list.append(num)
    print "\nSum: " + str(sum(num_list))

print my_fn()
