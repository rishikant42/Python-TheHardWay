def parent(num):

    def first_child():
        return "Beta1"

    def second_child():
        return "Beta2"

    try:
        assert num == 10
        return first_child
    except AssertionError:
        return second_child

foo = parent(10)
bar = parent(11)

print foo

print "\n\n"

print bar

print "\n\n"

print foo()

print "\n\n"

print bar()
