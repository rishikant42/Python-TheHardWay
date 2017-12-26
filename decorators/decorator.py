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
