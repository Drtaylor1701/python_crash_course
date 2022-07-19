#!/usr/bin/env/python3
'''many data types in Python are sequences
strings, lists, and tuples

tuples are immutable sequences

lists are great but it's nice to have an immutable option
'''

#example of a tuple
from lib2to3.pytree import convert


fullname = ("Grace", "M", "Hopper")

'''positions of elements have meaning

when a function returns multiple values, they are returned in a tuple'''

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

result = convert_seconds(5000)
print(type(result))
print(result)

#unpacking tuples
hours, minutes, seconds = result
print(hours, minutes, seconds)

hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes, seconds)