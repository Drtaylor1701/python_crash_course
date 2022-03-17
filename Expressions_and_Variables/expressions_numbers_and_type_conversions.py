#python converts the int to a float to do this (implicit conversion)
print(7+8.5)

#to combine a string and number you need an explicit conversion
base = 6
height = 3
area = (base*height)/2
print("the area of the triangle is " + str(area))

'''As we saw earlier in the video, some data types can be mixed and matched due to implicit conversion. Implicit conversion is where the interpreter helps us out and automatically converts one data type into another, without having to explicitly tell it to do so.

By contrast, explicit conversion is where we manually convert from one data type to another by calling the relevant function for the data type we want to convert to. We used this in our video example when we wanted to print a number alongside some text. Before we could do that, we needed to call the str() function to convert the number into a string. Once the number was explicitly converted to a string, we could join it with the rest of our textual string and print the result.'''