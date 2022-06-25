def my_gen():
    n = 1
    print('first')
    yield n

    n += 1
    print('second')
    yield n

    n += 1
    print('three')
    yield n


g = my_gen()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
