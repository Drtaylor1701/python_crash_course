#!/usr/bin/env/python3
'''you can use for loops for this
'''

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}

for extension in file_counts:
    #will list the keys, but not associated values
    print(extension)

#items method will return the keys
for extension, amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount, extension))

#you might just want the values
print(file_counts.keys())
print(file_counts.values())

for item in file_counts.values():
    print(item)

def count_letters(text):
    '''example of counting how many times each letter appears in a text'''
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("tenant"))
print(count_letters("a long string with a lot of letters"))
