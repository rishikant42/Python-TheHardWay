class UserA(object):

    def __init__(self, name):
        self.name = name

    def getName(self):
        print "User-A class"
        print self.name
        print "Good luck"


class UserB(UserA):
    def __init__(self, abcd):
        UserA.__init__(self, abcd)

    def getName(self):
        print self.name


class UserC(UserB):
    def __init__(self, abcd):
        UserB.__init__(self, abcd)

    def getName(self):
        print "Hello"
        UserB.getName(self)


class UserD(UserC):
    def __init__(self, abcd):
        UserC.__init__(self, abcd)

    def getName(self):
        UserC.getName(self)


class UserE(UserC):
    def __init__(self, abcd):
        UserC.__init__(self, abcd)

    def getName(self):
        super(UserE, self).getName()
