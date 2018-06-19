def countdown(n):
    print "Counting down from", n
    while n > 0:
        yield n
        n -= 1


g = countdown(5)

print g

print g.next()
print g.next()
print g.next()
