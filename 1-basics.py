# Variable: A storage location identified by its name, containing some value.

# Value of 10 is assigned to variable a and 20 to variable b
a = 10
b = 20

# We can do any operation (arithmetic for numbers, string transformation for text) on variables
# For example We can do any arithmetic calculation on numbers
c = a + b # or any calculation 
print(c) # will print 30

s = '  Some string '
# We can perform an operation on this string, for example lets remove the empty spaces in front of and behind the string
print(s.strip())

# Data Structures are ways of representing data, each has its own pros and cons and places that they are the right fit.

## List: A collection of elements that can be accessed by knowing the location (aka index) of the element
l = [1, 2, 3, 4]
l[0] # will be 1
l[3] # will print 4
## NOTE: lists retain the order of elements in it but dictionary doesn't

## Dictionary: A collection of key-value pairs, where each key is mapped to a value using a hash function. Provides fast data retrieval based on keys.
d = {'a': 1, 'b': 2}
d.get('a') # will print 1
d.get('b') # will print 2
## NOTE: The dictionary cannot have duplicate keys

## Set: A collection of unique elements that do not allow duplicates
my_set = set()
my_set.add(10)
my_set.add(10)
my_set.add(10)
print(my_set) # This will only show 10, since the set only keeps unique values

## Tuple: A collection of immutable(non changeable) elements, tuples retain their order once created.
my_tuple = (1, 'hello', 3.14)
print(my_tuple)  # Output: (1, 'hello', 3.14)
# Accessing elements by index
print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: 'hello'

# Counting occurrences of an element
count_tuple = (1, 2, 3, 1, 1, 2)
print(count_tuple.count(1))  # Output: 3

# Finding the index of an element
print(count_tuple.index(2))  # Output: 1

# Loop

# Functions

# Class and objects

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
