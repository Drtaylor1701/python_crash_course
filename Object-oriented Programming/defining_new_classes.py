#starts a new class
#should start w/ a capital letter
class Apple:
    #pass keyword shows that the body is empty
    #can use pass as a placeholder in any empty python block
    pass

#now the class has attributes
class Apple:
    color = ""
    flavor = ""

#assign the class to a varibale to create an instance of the class
jonagold = Apple()

#assign values to the attributes
jonagold.color = "red"
jonagold.flavor = "sweet"

#to retrieve the values
print(jonagold.color)
print(jonagold.flavor)

#use a method on an attribute
print(jonagold.color.upper())

golden = Apple()
golden.color = "Yellow"
golden.flavor = "Soft"