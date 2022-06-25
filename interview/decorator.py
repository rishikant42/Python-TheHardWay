def print_decorator(fn):
    def wrapper(*args, **kwargs):
        print('start')
        fn(*args, **kwargs)
        print('end')
    return wrapper


@print_decorator
def say_hello(x, y):
    print('hello', x+y)


say_hello(2, 3)
