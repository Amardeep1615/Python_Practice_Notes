# In Python, a variable serves as a symbolic name that references a value stored in the computer's memory. Variables facilitate the storage, manipulation, and reuse of data within a program. Unlike some other programming languages, Python does not require explicit variable declaration. A variable is created the moment a value is assigned to it using the assignment operator =. 
# Rules for Naming Variables
# Variable names must begin with a letter or an underscore.
# Variable names can only contain alphanumeric characters and underscores (A-z, 0-9, and _). 
# Variable names are case-sensitive (myVar, myvar, and MyVar are different variables). 
# Reserved keywords in Python cannot be used as variable names.
# Assigning Values to Variables
# Values are assigned to variables using the = operator. The value can be of any data type, such as integers, strings, floats, or booleans. Python is dynamically typed, so the type of a variable is inferred from the assigned value and can change during the program execution. 

x = 5         # x is an integer
y = "Hello"   # y is a string
z = 3.14      # z is a float
a = True      # a is a boolean
print(x,y,z,a)

x, y, z = "Orange", "Banana", "Cherry"
print(x)  # Output: Orange
print(y)  # Output: Banana
print(z)  # Output: Cherry

x = y = z = "Orange"
print(x)  # Output: Orange
print(y)  # Output: Orange
print(z)  # Output: Orange

# Variable 'x' stores the integer value 10
x = 5

# Variable 'name' stores the string "Samantha"
name = "Samantha"  

print(x)
print(name)


# Variable Scope
# The scope of a variable determines where in the code the variable can be accessed. In Python, variables defined outside of any function or class have "global scope" and can be accessed from anywhere in the code. Variables defined inside a function have "local scope" and can only be accessed within that function.

global_var = 10  # Global variable

def my_function():
  local_var = 5  # Local variable
  print(global_var)  # Accessing global variable inside function
  print(local_var)   # Accessing local variable inside function

my_function()
print(global_var)  # Accessing global variable outside function
# print(local_var)   # This would cause an error, as local_var is not defined outside the function

x = "Zara"
y =  10
z =  10.10

print(type(x))
print(type(y))
print(type(z)) #Casting Python Variables

age = 20
Age = 30

print( "age =", age )
print( "Age =", Age )  #Case-Sensitivity of Python Variables

# ..................................................................Day3 - Datatypes...............................................................................
# Data Types
# Python variables can hold various data types, including:
# int: Integers (whole numbers)
# float: Floating-point numbers (numbers with decimals)
# str: Strings (sequences of characters)
# bool: Booleans (True or False values)
# list: Ordered, mutable collections of values
# tuple: Ordered, immutable collections of values
# dict: Unordered collections of key-value pairs.

integer_variable = 10
float_variable = 3.14
string_variable = "Hello, World!"
boolean_variable = True
list_variable = [1, 2, 3]
tuple_variable = (4, 5, 6)
dict_variable = {"name": "John", "age": 30}


# Python has several built-in data types used to classify and categorize data. These data types can be grouped into the following categories:

# Numeric Types: Represent numerical values.
# int: Integer numbers (e.g., 10, -5, 0).
# float: Floating-point numbers (e.g., 3.14, -2.5, 0.0).
# complex: Complex numbers (e.g., 2 + 3j, 1j).

# Sequence Types: Ordered collections of items.
# str: Strings, sequences of characters (e.g., "hello", 'world').
# list: Ordered, mutable sequences of items (e.g., \[1, 2, 3], \['a', 'b', 'c']).
# tuple: Ordered, immutable sequences of items (e.g., (1, 2, 3), ('a', 'b', 'c')).
# range: Generates a sequence of numbers within a specified range.

# Mapping Type: Represents key-value pairs.
# dict: Dictionaries, collections of key-value pairs (e.g., {'name': 'Alice', 'age': 30}).

# Set Types: Unordered collections of unique items.
# set: Mutable sets, allow adding and removing elements.
# frozenset: Immutable sets, do not allow modification after creation.

# Boolean Type: Represents truth values.
# bool: Boolean values, either True or False.

# Binary Types: Represent sequences of bytes.
# bytes: Immutable sequences of bytes.
# bytearray: Mutable sequences of bytes.
# memoryview: Provides a memory view of an object without copying.

# None Type: Represents the absence of a value.
# NoneType: Has a single value, None

# Examples of data types
x = 10          # int
y = 3.14        # float
z = 2 + 3j      # complex
s = "hello"     # str
l = [1, 2, 3]   # list
t = (4, 5, 6)   # tuple
r = range(5)    # range
d = {'a': 1, 'b': 2} # dict
st = {1, 2, 3}  # set
fs = frozenset({4, 5, 6}) # frozenset
b = True        # bool
bs = b'abc'      # bytes
ba = bytearray(b'abc') # bytearray
mv = memoryview(bs) # memoryview
n = None        # NoneType

# Printing the type of each variable
print(type(x))
print(type(y))
print(type(z))
print(type(s))
print(type(l))
print(type(t))
print(type(r))
print(type(d))
print(type(st))
print(type(fs))
print(type(b))
print(type(bs))
print(type(ba))
print(type(mv))
print(type(n))

# ..................................................................Day4 - Operators-1...............................................................................
# ..................................................................Day5 - Operators-2...............................................................................
# ..................................................................Day6 - Conditional Statements,Loops...............................................................................
# ..................................................................Day7 - Functions...............................................................................
# ..................................................................Day8 - Modules...............................................................................
# ..................................................................Day9 - Packages...............................................................................
# ..................................................................Day10 - List Methods...............................................................................
# ..................................................................Day11 - Set,Tuple Methods...............................................................................
# ..................................................................Day12 - Dict Methods...............................................................................
# ..................................................................Day13 - Typecasting,Strings,Bitwise Operators...............................................................................
# ..................................................................Day14 - ...............................................................................
# ..................................................................Day15 - ...............................................................................
# ..................................................................Day16 - ...............................................................................