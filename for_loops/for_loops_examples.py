#!/usr/bin/env python3

product = 1
for n in range(1, 10):
    product = product * n

print(product)

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

#change the third parameter to change the size of each step
def to_celsius(x)