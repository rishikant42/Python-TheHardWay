def next_sqr():
    i = 1

    while True:
        yield i*i
        i += 1

sqr = next_sqr()

for n in sqr:
    if n > 100:
        break
    print n
