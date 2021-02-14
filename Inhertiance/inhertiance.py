class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

#use parentheses in the class declaration to show an inheritance relationship

#both Apple and Grape inhertis from Fruit
#have same constructor
class Apple(Fruit):
    pass

class Grape(Fruit):
    pass

granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")

print(granny_smith.flavor)
print(carnelian.color)

class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name=self.name, sound = self.sound))

class Piglet(Animal):
    sound = "Oink!"

hamlet = Piglet("Hamlet")
hamlet.speak()

class Cow(Animal):
    sound = "Moooo"

milky = Cow("Milky White")
milky.speak()

class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {name} is made of {material}".format(self.name,self.material))
			
class Shirt(Clothing):
    pass
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()

class Employee:
    def __init__():
        