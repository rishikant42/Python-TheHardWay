class Pet(object):

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" %(self.name, self.species)

class Dog(Pet):

    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, "Dogy")
        self.chases_cats = chases_cats
        
    def chasesCats(self):
        return self.chases_cats

class Cat(Dog):

    def __init__(self, name, hates_dogs):
        Pet.__init__(self, name, "Cat")
        self.hates_dogs = hates_dogs

    def hatesDogs(self):
        return self.hates_dogs

polly = Pet("Polly", "Parrot")

#print ("Polly is a %s" % polly.getSpecies())

doggy = Dog("Lebra", "yes")

caty = Cat("Meow", "No")

print isinstance(polly, Pet)
print isinstance(polly, Dog)

print isinstance(doggy, Pet)
print isinstance(doggy, Dog)

print isinstance(caty, Cat)
print isinstance(caty, Pet)
print isinstance(caty, Dog)

#print ("Dog name: %s have species: %s following cats %s" % (doggy.getName(), doggy.getSpecies(), doggy.chasesCats()))

#print doggy

#print ("Polly is a %s" % Pet.getSpecies(polly))

#print polly
