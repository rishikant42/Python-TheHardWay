def _pvt_method(order):
    return order


def public_method(pm):
    print pm
    print _pvt_method(21)
    print "Hello"

public_method("what")
