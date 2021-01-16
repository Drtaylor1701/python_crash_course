'''
Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements function to return every other [1] from the list, this time using the enumerate function to check if an [1] is on an even position or an odd position.
'''

def skip_elements(elements):
	# code goes here
    output_list = []
    for element in enumerate(elements):
        #print(element)
        if element[0] % 2 == 0:
            output_list.append(element[1])
            #print(output_list)
    return output_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']