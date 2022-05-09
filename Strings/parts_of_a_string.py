#!/usr/bin/env python3
name = 'Jaylen'
print(name[1])

'''starts counting at 0'''
print(name[0])

print(name[5])

#generates an error
#print(name[6])

text = "random string with a lot of characters"
print(text[-1])
print(text[-2])

'''Slice

portion of a string that can contain more than one character;
also sometimes called a substring'''

color = "Orange"
print(color[1:4]) #does not include index 4

fruit = "Pineapple"
print(fruit[:4])

print(fruit[4:])