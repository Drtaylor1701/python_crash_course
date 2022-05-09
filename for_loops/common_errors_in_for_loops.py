#!/usr/bin/env python3

'''interpreter will not iterate over a single element'''
# for x in 25:
#     print(x)
#will return an error because it is not iterable

for x in [25]:
    print(x) #works because a list is iterable

'''strings are also iterable, FYI'''