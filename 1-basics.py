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
## Accessing elements by index
print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: 'hello'

## Counting occurrences of an element
count_tuple = (1, 2, 3, 1, 1, 2)
print(count_tuple.count(1))  # Output: 3

## Finding the index of an element
print(count_tuple.index(2))  # Output: 1

# Loop allows a specific chunk to code to be repeated a certain number of times
# Example: We can use loop to print numbers 0 through 10
for i in range(11):
  print(i)

## We can loop through our data structures as shown below
## List loop
for elt in l:
  print(elt) # or any operation you may want to do
## We can do similar loop for tuples and sets

## Dictionary loop
for k, v in d.items():
  print(f'Key: {k}, Value: {v}') # print key and values in dictionary

## Comprehension is a shorthand way of writing a loop
## For example we can use the below to multiply every element in list l with 2
[elt*2 for elt in l]

# Functions: A block of code that can be re-used as needed. This allows for us to have logic defined in one place, making it easy to maintainand use.
## For example lets create a simple function, that takes a list as an input and returns another list whose values are greater than 3
def gt_three(input_list):
  return [elt for elt in input_list if elt > 3]
## NOTE: we use list comprehension with filtering in the above function

list_1 = [1, 2, 3, 4, 5, 6]
print(gt_three(list_1)) ## Will print [4, 5, 6]

list_2 = [1, 2, 3, 1, 1, 1]
print(gt_three(list_2)) ## Will print []

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

# Libraries are code that can be reused.

# Python comes with some standard libraries to do common operations, 
# such as datetime library to work with time (although there are better libraries)
from datetime import datetime # you can import library or your code from another file with the import statement
datetime.now() # will show a datetime object that has the current time
datetime.now().strftime('%Y %m %d') # We can use multiple such methods 

# Generators
# Checkout generators here: https://www.startdataengineering.com/post/writing-memory-efficient-dps-in-python/#1-using-generators
