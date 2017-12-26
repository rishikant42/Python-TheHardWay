from time import sleep

def sleep_decorator(f):

    def wrapper(*args, **kwargs):
        sleep(2)
        return f(*args, **kwargs)

    return wrapper

@sleep_decorator
def print_number(num):
    return num

for num in range(6):
    print print_number(num)
