def my_decorator(f):

    def wrapper():

        num = 10

        if num == 10:
            print "Yes!!"
        else:
            print "No!!"

        f()

        print "Something happen after f is called"

    return wrapper

def my_function():
    print "my function is called"

my_function = my_decorator(my_function)

my_function()
