def my_decorator(f):

    def wrapper():
        print "Something happen before f is called"

        f()

        print "Something happen after f is called"

    return wrapper

def my_function():
    print "my function is called"

my_function = my_decorator(my_function)

my_function()
