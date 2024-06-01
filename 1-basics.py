a = 10 # assign value 10 to a variable named a
b = 20

c = a + b # or any calculation 
print(c) # will print 30

# create functions with def
def some_function(a, b):
  return (a + 5)*b

c = some_function(1, 3) # the value (1+5)*3 = 18 will be assigned to variable c

# We use data structures to store data in Python, the mains ones are dictionary and lists

# dictionary
# Use it when you have to access values based on its identified (aka key)
d = {'a': 1, 'b': 2}
d.get('a') # will print 1
d.get('b') # will print 2

# list 
# use it when you need to store a collection of items
l = [1, 2, 3, 4]
l[0] # will be 1
l[3] # will print 4

# NOTE: lists retain the order of elements in it but dictionary doesn't

# Loop
# We can loop through list and dictionaries and process them as necessary
for elt in l:
  print(elt)
# the above will print all the elements in list l

for k, v in d.items():
  print(k, v)
# The aboce code will print all the key and values in the dictionary d

# comprehension, aka shortcut to write loops
[print(elt) for elt in l]
[print(k, v) for k, v in d.items()]

# we can also use comprehensions to create new lists/dictionary
new_list = [elt*2 for elt in l] # new_list will have [2, 4, 6, 8] 

# Python comes with some standard libraries to do common operations, 
# such as datetime library to work with time (although there are better libraries)
from datetime import datetime # you can import library or your code from another file with the import statement
datetime.now() # will show a datetime object that has the current time
datetime.now().strftime('%Y %m %d') # We can use multiple such methods 

# Classes and Objects
# Think of a class as a blue print and objects as things created based on that blue print
# you can define classes in python as shown below
class DataExtractor:

  def __init__(self, some_value):
    self.some_value = some_value

  def get_connection(self):
    # some logic
    # some_value is accessible using self.some_value
    pass

  def close_connection(self):
    # some logic
    # some_value is accessible using self.some_value
    pass

# Lets create a DataExtractor object
de_object = DataExtractor(10)
print(de_object.some_value)
# will print 10
