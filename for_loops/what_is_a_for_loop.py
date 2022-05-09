#!/usr/bin/env python3

for x in range(5):
    print(x)

'''a range of numbers will start with 0 by default'''

def square(n):
    return n*n
def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

print(sum_squares(10))

friends = ['Taylor', 'Alex', 'Pat', 'Eli'] #this is a list
for friend in friends: #for loop can iterate through anything that is iterable
    print('Hi ' + friend)
