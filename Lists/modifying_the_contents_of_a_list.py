#!/usr/bin/env/python3

'''
lists are mutable
'''

fruits = ["Pineapple", "Banana", "Apple", "Melon"]

#add and element to the end of the list
fruits.append("Kiwi")
print(fruits)

#add an element at a given location
fruits.insert(0, "Orange")
print(fruits)

fruits.insert(25, "Peach") #adds the element to the end
print(fruits)

#remove first occurrence of an element from a list
fruits.remove("Melon")
#fruits.remove("Pear") Generates a ValueError

fruits.pop(3) #removes item at index 3
print(fruits)

fruits[2] = "Strawberry" #assigns Strawberry to index 2
print(fruits)