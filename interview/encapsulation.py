class Base:
    def __init__(self):
        self.public = 1
        self._protected = 2
        self.__private = 3

    def bprint(self):
        print('public', self.public)
        print('protected', self._protected)
        print('private', self.__private)

    def _protectmethod(self):
        print('protected method')


class Child(Base):
    def __init__(self):
        super().__init__()
        self._protected = 3

    def cprint(self):
        print('public', self.public)
        print('protected', self._protected)
        # print('private', self.__private)


# b = Base()
# print(b.public)
# print(b._protected)
# b.bprint()

c = Child()
print(c.public)
print(c._protected)
c.cprint()
c._protectmethod()
