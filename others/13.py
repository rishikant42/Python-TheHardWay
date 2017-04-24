# recursive approach
def fact1(n):
    if n == 1:
        return 1
    else:
        return n * fact1(n-1)

# iterative approach
def fact2(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

print fact1(6)
print fact2(6)

import math
print math.factorial(6)
