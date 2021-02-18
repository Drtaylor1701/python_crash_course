# organize functions, classes, and other data together in a structured way

#python standard library contains ready-to-use modules
#add a module
import random

#recieves two parameters and generates a random nubmer between them
random.randint(1, 10)

#syntax is modulenname.function

import datetime
#datetime module provides a datetime class and the datetime class gives a method called "now"

now = datetime.datetime.now()
#calls the _str_ method of the datetime class which formats the output in a specific way
print(now)
#print specific parts of the date
print(now.year)
#timedelta class calculates a date in the future or the past
print(now + datetime.timedelta(days=28))

#