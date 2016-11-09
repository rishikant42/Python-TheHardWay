def is_intstring(s):
    try:
        int(s)
        return int(s)

    except ValueError:
        try:
            float(s)
            return float(s)
        except ValueError:
            return s

var = raw_input()

t = is_intstring(var)

def output():
    if type(t) == int:
        print "This input of type Integer."
    elif type(t) == str:
        print "This input of type String."
    elif type(t) == float:
        print "This input of type Float."
    else:
        print "This is something else."

output()
