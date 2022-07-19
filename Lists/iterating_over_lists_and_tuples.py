#!/usr/bin/env/python3

animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animals)

print("Total characters: {}, Average Length: {}".format(chars, chars/len(animals)))

#get the index of an element in the list with enumerate
winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))

#list of tuples containing two strings each. Create a new list with one string per person

#define a function to get a list of people
def full_emails(people):
    result = []
    #iterate over the list of people
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))

'''caution:
don't use range with indexes of a list. That works great in other languages but looks ugly in Python so it's not recommended.

There are some cases where you have to, like if you want to modify the elements.
'''