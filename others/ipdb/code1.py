def main():
    import ipdb; ipdb.set_trace()

    a = 1
    b = 2
    c = 3

    print "Add = ", add(a, b, c)

    print "Subtract = ", sub(a, b, c)

    print "Multiply = ", mul(a, b, c)

    print "Divide = ", div(a, b, c)

def add(a, b, c):
    sum1 = a + b
    sum2 = sum1 + c

    return sum2

def sub(a, b, c):
    return a - b - c

def mul(a, b, c):
    import ipdb; ipdb.set_trace()
    p1 = a * b
    p2 = p1 * c

    return p2

def div(a, b, c):
    return a / b / c

main()
