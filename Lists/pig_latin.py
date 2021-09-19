'''Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.
'''
def pig_latin(text):
    # Separate the text into words
    text_as_list = text.split()
    words = []
    for word in text_as_list:
        # Create the pig latin word and add it to the list
        words.append(word[1:] + word[0] + "ay")
        #print(words)
    # Turn the list back into a phrase
    output = ""
    for word in words:
        output = output + word + " "
    return output
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"