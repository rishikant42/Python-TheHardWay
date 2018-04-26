s1 = [1, 2, 3]

print map((lambda x: x*2), s1)

s2 = [[1, 1], [2, 2], [3, 3]]

print map((lambda x: x[0] + x[1]), s2)


s3 = [1, 2, 3]
s4 = [1, 2, 3]
print map((lambda x, y: x + y), s3, s4)
