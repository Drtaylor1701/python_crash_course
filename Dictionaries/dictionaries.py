#initialize a dictionary
x = {}

#example dictionary syntax
file_counts = {"jpg":10, "txt":14, "csv":2,"py":23}

#access a value
file_counts["txt"]
#returns 14

#check if something is in a dictionary
"jpg" in file_counts
"html" in file_counts

#add an entry to a dictionary
file_counts["cfg"] = 8

#overwrite an existing entry
file_counts["csv"] = 17

#delete element from a dictionary
del file_counts["cfg"]

#use a for loop to print the keys in the dictionary
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
    print(extension)

#to access values, use the items method to return at tuple for each value in the dictionary of the key and value:
for ext, amount in file_counts.items():
    print("There are {} files with the {} extension".format(amount, extension))

#keys method
file_counts.keys()

#values method
file_counts.values()

for value in file_counts.values():
    print(value)
