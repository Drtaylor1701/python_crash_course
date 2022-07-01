'''additional examples of string methods'''

#upper and lower
print("mountains".upper())
print("MOUNTAINS".lower())

#transform user input to case you want
answer = "YES"
if answer.lower() == 'yes':
    print("success")

#strip
print(" yes ".strip())
#also removes tabs and newlines

print(" yes ".lstrip())
print(" yes ".rstrip())

#getting information about a string
print("The number of times e occurs in this string is 4.".count('e'))

#endswith
print("Forest".endswith("t"))

#isnumeric
print("Forest".isnumeric())
print("12345".isnumeric())
print(int("12345"))

#join for concatenating
print(" ".join(['This', 'is', 'a', 'phrase', 'joined', 'by', 'spaces']))

