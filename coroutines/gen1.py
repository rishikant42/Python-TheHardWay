def simple_generator():
    yield 1
    yield 2
    yield 3


s = simple_generator()
for i in s:
    print i

for i in s:
    print i
