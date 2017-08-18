class Pet(object):

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)


class Dog(Pet):

    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats

    def chasesCats(self):
        return self.chases_cats

    def getName(self, extra):
        print "This is overwritten"
        print Pet.getName(self)
        print extra
        print "Success"

    def getSpecies(self):
        print "Use of super"
        print super(Dog, self).getSpecies()
        print Pet.getSpecies(self)
        print "working"
