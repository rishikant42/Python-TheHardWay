from math import *

class test():
    """represnt distance b/w two point"""

blank = test()

blank.x1 = float(raw_input('x1 = '))
blank.y1 = float(raw_input('y1 = '))
blank.x2 = float(raw_input('x2 = '))
blank.y2 = float(raw_input('y2 = '))

def distance(t):
    D = sqrt((t.x2 - t.x1)**2 + (t.y2 - t.y1)**2)
    print "%f" %D

distance(blank)
