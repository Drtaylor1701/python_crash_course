class Piglet:
    name = "piglet"
    #self represents the instance that the method is being executed on
    def speak(self):
        print("Oink! I'm {}! Oink!".format(self.name))
        #self.name above means it's accessing the attribute "name" from the current instance of "Piglet"

    years = 0
    def pig_years(self):
        return self.years * 18

hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()

petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()

piggy = Piglet()
piggy.years = 2
print(piggy.pig_years())