#!/usr/bin/env python3
'''nested for loops - one inside the other'''

for left in range(7):
    for right in range(left, 7):
        print("[ " + str(left) + "|" + str(right) + "]", end=" ")#end=" " will change newline character to a space