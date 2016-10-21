class Point(object):
    """represent a point"""

def print_point(t):
    print "(%f, %f)" %(t.x, t.y)

class rectangle(object):
    """represent rectangle"""

box = rectangle()
box.width = 100.0
box.height = 200.0


box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def find_centre(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p

centre = find_centre(box)
print_point(centre)
