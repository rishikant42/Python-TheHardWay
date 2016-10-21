class point(object):
    """Represent point in 2D"""

blank = point()

blank.x = float(raw_input())
blank.y = float(raw_input())


def print_point(k):
    print "(%f, %f)" %(k.x, k.y)

print_point(blank)
