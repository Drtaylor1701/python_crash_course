 #!/usr/bin/env/python3

'''list data type is like a long box with spaces in them, with a different thing in each space.'''

x = ["Now", "we", "are", "cooking!"]

print(type(x))
print(len(x)) #number of elements in a list
print("are" in x)
print(x[3])
#print(x[4]) returns an IndexError
print(x[:2])