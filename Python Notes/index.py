# Python Complete Guide (A-Z)
# Save as Python_Guide.py or use Jupyter Notebook in VS Code

#======================================================================
# 1. Python Basics
#======================================================================

# 1.1 Installation & VS Code Setup
# Install Python from python.org
# VS Code Extensions: Python, Pylance, Jupyter
# Ctrl+Shift+P -> Python: Select Interpreter

print("Hello, VS Code!")  # Simple test

# 1.2 Basic Syntax
name = "Alice"  # Variable declaration
print(f"Hello {name}")  # f-string (Python 3.6+)

# 1.3 Data Types
# Fundamental Types
num_int = 10       # Integer
num_float = 10.5   # Float
text = "Python"    # String
is_true = True     # Boolean
nothing = None     # NoneType

# Type Checking
print(type(num_int))   # <class 'int'>

# 1.4 Collections
# List (Mutable)
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

# Tuple (Immutable)
coordinates = (10.0, 20.5)

# Set (Unique elements)
unique_nums = {1, 2, 3, 2}  # {1, 2, 3}

# Dictionary (Key-Value pairs)
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# 1.5 Control Flow
# If-Elif-Else
age = 18
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")

# For Loop
for fruit in fruits:
    print(fruit.upper())

# While Loop
count = 0
while count < 5:
    print(count)
    count += 1

#======================================================================
# 2. Intermediate Python
#======================================================================

# 2.1 Functions
def greet(name="Guest"):
    """Documentation String"""
    return f"Hello, {name}!"

print(greet("Alice"))  # Positional argument
print(greet())         # Default argument

# 2.2 File Handling
# Writing
with open("demo.txt", "w") as file:
    file.write("Hello File!")

# Reading
with open("demo.txt", "r") as file:
    content = file.read()
print(content)

# 2.3 Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Cleanup code")

# 2.4 OOP Concepts
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return "Woof!"

buddy = Dog("Buddy")
print(buddy.speak())

#======================================================================
# 3. Advanced Python
#======================================================================

# 3.1 Decorators
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(2, 3))  # Logs: Calling add

# 3.3 Generators
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

for num in fibonacci(100):
    print(num)

# 3.4 Async Programming
import asyncio

async def fetch_data():
    await asyncio.sleep(1)
    return "Data fetched"

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())

#======================================================================
# 4. Best Practices & Tools
#======================================================================

# 4.1 PEP8 Compliance
# Use pycodestyle or flake8 in VS Code
# Enable formatting with black or autopep8

# 4.2 Virtual Environments
# Terminal: python -m venv .venv
# Activate: .venv\Scripts\activate (Windows)

# 4.3 Testing (pytest)
# test_sample.py
def test_add():
    assert add(2, 3) == 5

# Run: pytest test_sample.py

# 4.4 Debugging in VS Code
# Set breakpoints (F9)
# Start debugging (F5)
# Watch variables & call stack

#======================================================================
# 5. Additional Topics
#======================================================================







# Python A to Z: From Basics to Advanced with Detailed Subtopics and Examples

# ----------------------------
# Day 1: Git & GitHub (Brief Intro)
# ----------------------------

# Git is a version control system.
# GitHub is a platform to host Git repositories.

# Commands:
# git init
# git status
# git add .
# git commit -m "message"
# git push origin main

# ----------------------------
# Day 2: Variables
# ----------------------------
x = 10
name = "Alice"
pi = 3.14
is_active = True
print(x, name, pi, is_active)

# ----------------------------
# Day 3: Datatypes
# ----------------------------
print(type(10))          # int
print(type(3.14))        # float
print(type("Hello"))     # str
print(type(True))        # bool
print(type([1, 2, 3]))    # list
print(type((1, 2, 3)))    # tuple
print(type({"a": 1}))     # dict
print(type({1, 2, 3}))    # set

# ----------------------------
# Day 4: Operators - Part 1
# ----------------------------
# Arithmetic: + - * / % // **
print(10 + 5)
print(10 % 3)
print(10 ** 2)

# ----------------------------
# Day 5: Operators - Part 2
# ----------------------------
# Comparison
print(5 > 3, 5 == 5)
# Logical
print(True and False)
# Assignment
x = 5
x += 2
print(x)

# ----------------------------
# Day 6: Conditionals & Loops
# ----------------------------
# if-else
num = 7
if num > 0:
    print("Positive")
else:
    print("Non-positive")

# for loop
for i in range(3):
    print(i)

# while loop
n = 0
while n < 3:
    print(n)
    n += 1

# match-case (Python 3.10+)
def color_meaning(color):
    match color:
        case "red":
            return "Stop"
        case "green":
            return "Go"
        case _:
            return "Unknown"
print(color_meaning("red"))

# ----------------------------
# Day 7: Functions
# ----------------------------
def greet(name):
    return f"Hello, {name}"
print(greet("Bob"))

# Lambda
square = lambda x: x * x
print(square(4))

# ----------------------------
# Day 8: Modules
# ----------------------------
import math
print(math.sqrt(16))

# ----------------------------
# Day 9: Packages (concept only)
# ----------------------------
# A package is a directory with __init__.py file and modules inside.

# ----------------------------
# Day 10: List Methods
# ----------------------------
lst = [1, 2, 3]
lst.append(4)
lst.insert(1, 10)
lst.remove(3)
print(lst)

# ----------------------------
# Day 11: Set & Tuple Methods
# ----------------------------
s = {1, 2, 3}
s.add(4)
s.discard(2)
print(s)

tup = (1, 2, 3)
print(tup.count(2))

# ----------------------------
# Day 12: Dictionary Methods
# ----------------------------
d = {"a": 1, "b": 2}
print(d.keys())
print(d.get("a"))
d.update({"c": 3})
print(d)

# ----------------------------
# Additional Topics
# ----------------------------

# Strings
s = "Hello"
print(s.upper(), s[0], s[-1])

# Casting
a = int("10")
b = float("5.5")
print(a + b)

# Arrays (using array module)
import array
arr = array.array('i', [1, 2, 3])
print(arr)

# Classes and Objects
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes sound")
a = Animal("Dog")
a.speak()

# Inheritance
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")
d = Dog("Tommy")
d.speak()

# Iterators
mylist = [1, 2, 3]
myiter = iter(mylist)
print(next(myiter), next(myiter))

# Polymorphism
class Cat:
    def speak(self):
        print("Meow")
def animal_sound(animal):
    animal.speak()
animal_sound(Cat())

# Scope
x = 10
def scope_test():
    global x
    x = 20
scope_test()
print(x)

# Dates
import datetime
print(datetime.datetime.now())

# Math
print(math.factorial(5))

# JSON
import json
js = '{"name": "John", "age": 30}'
data = json.loads(js)
print(data["name"])

# RegEx
import re
text = "Python 101"
match = re.search(r"\d+", text)
print(match.group())

# PIP (Python Package Installer)
# pip install package-name

# Try-Except
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Can't divide by zero")

# User Input
user = input("Enter name: ")
print("Welcome", user)

# String Formatting
name = "John"
age = 25
print(f"Name: {name}, Age: {age}")

# File Handling
with open("demo.txt", "w") as f:
    f.write("This is a file")
with open("demo.txt") as f:
    print(f.read())




# Python Complete Guide with Examples
# Save as python_guide.py and run in VS Code

#======================================================================
# Python Introduction Topics
#======================================================================

# 1. Python Syntax
print("Hello, World!")  # Simple print statement
if 5 > 2: print("Five is greater than two!")  # Indentation matters

# 2. Python Comments
# This is a single-line comment
""" This is a 
multi-line comment """

# 3. Python Variables
x = 5                   # int
name = "John"           # str
is_active = True        # bool
PI = 3.1415926535       # float

# 4. Python Data Types
print(type(x))          # <class 'int'>
print(type(name))       # <class 'str'>
print(type(is_active))  # <class 'bool'>

# 5. Python Numbers
a = 10          # int
b = 20.5        # float
c = 1 + 3j      # complex
print(c.real)   # 1.0

# 6. Python Casting
str_num = "123"
int_num = int(str_num)
float_num = float("123.45")

# 7. Python Strings
msg = "Python Programming"
print(msg[0])       # 'P'
print(len(msg))     # 18
print(msg.upper())  # PYTHON PROGRAMMING

# 8. Python Booleans
print(10 > 9)       # True
print(bool([]))     # False (empty list)
print(bool("abc"))  # True

# 9. Python Operators
# Arithmetic: + - * / // % **
# Comparison: == != > < >= <=
# Logical: and or not
# Assignment: = += -= *= /=
# Membership: in, not in

# 10. Python Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits[1] = "mango"
print(fruits[:2])  # ['apple', 'mango']

# 11. Python Tuples
colors = ("red", "green", "blue")
# colors[0] = "yellow"  # Error (immutable)
print(colors[1])  # green

# 12. Python Sets
unique_nums = {1, 2, 3, 2, 1}
print(unique_nums)  # {1, 2, 3}

# 13. Python Dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "Paris"
}
print(person.get("age"))  # 30

# 14. Python if-else
age = 18
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")

# 15. Python Match (3.10+)
status = 404
match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case _:
        print("Unknown")

# 16. Python While Loops
count = 0
while count < 3:
    print(count)
    count += 1  # 0 1 2

# 17. Python For Loops
for fruit in fruits:
    print(fruit.upper())

# 18. Python Functions
def greet(name="Guest"):
    return f"Hello, {name}!"
print(greet("Bob"))  # Hello, Bob!

# 19. Python Lambda
square = lambda x: x ** 2
print(square(5))  # 25

# 20. Python Arrays
import array
nums = array.array('i', [1, 2, 3])
nums.append(4)

# 21. Python Classes/Objects
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return "Woof!"

buddy = Dog("Buddy")
print(buddy.bark())  # Woof!

# 22. Python Inheritance
class Poodle(Dog):
    def show_breed(self):
        return "Poodle"

fluffy = Poodle("Fluffy")
print(fluffy.bark())  # Woof!

# 23. Python Iterators
class Count:
    def __init__(self, limit):
        self.limit = limit
    
    def __iter__(self):
        self.n = 1
        return self
    
    def __next__(self):
        if self.n <= self.limit:
            res = self.n
            self.n += 1
            return res
        else:
            raise StopIteration

for num in Count(3):
    print(num)  # 1 2 3

# 24. Python Polymorphism
class Cat:
    def speak(self):
        return "Meow"

class Duck:
    def speak(self):
        return "Quack"

def animal_sound(animal):
    print(animal.speak())

animal_sound(Cat())  # Meow
animal_sound(Duck())  # Quack

# 25. Python Scope
x = 10  # Global
def test():
    y = 5  # Local
    print(x + y)
test()

# 26. Python Modules
import math
print(math.sqrt(25))  # 5.0

# 27. Python Dates
from datetime import datetime
now = datetime.now()
print(now.strftime("%Y-%m-%d"))  # Current date

# 28. Python Math
print(math.pi)           # 3.141592653589793
print(math.pow(2, 3))    # 8.0
print(math.floor(3.7))   # 3

# 29. Python JSON
import json
person_json = json.dumps(person)
print(person_json)  # {"name": "Alice", ...}

# 30. Python RegEx
import re
text = "Contact: info@example.com"
match = re.search(r'[\w.]+@[\w.]+', text)
print(match.group())  # info@example.com

# 31. Python PIP
# Terminal: pip install pandas
# (Run in VS Code terminal)

# 32. Python Try-Except
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Cleanup")

# 33. Python User Input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# 34. Python String Formatting
price = 49.99
print(f"Price: ${price:.2f}")       # f-string
print("Price: ${:.2f}".format(price))  # format()

# 35. Python File Handling
with open("sample.txt", "w") as f:
    f.write("Hello File!")

with open("sample.txt") as f:
    print(f.read())  # Hello File!

#======================================================================
# 12-Day Learning Plan with Examples
#======================================================================

# Day1 - Git/GitHub
"""
VS Code Steps:
1. Initialize repo: git init
2. Stage files: git add .
3. Commit: git commit -m "Initial commit"
4. Connect to GitHub: git remote add origin <url>
5. Push: git push -u origin master
"""

# Day2 - Variables
x = 10          # Integer
y = "Python"    # String
z = 3.14        # Float

# Day3 - Data Types
print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
print(type(z))  # <class 'float'>

# Day4 - Operators-1
a = 10 + 5      # 15
b = 20 / 3      # 6.666...
c = 2 ** 3      # 8

# Day5 - Operators-2
print(10 > 5 and 5 < 8)  # True
print("py" in "python")   # True

# Day6 - Conditionals & Loops
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

for i in range(3):
    print(i)  # 0 1 2

# Day7 - Functions
def multiply(a, b):
    return a * b
print(multiply(3, 4))  # 12

# Day8 - Modules
# Create mymodule.py with:
# def greet(name):
#     return f"Hello {name}"
# Then:
# import mymodule
# print(mymodule.greet("Alice"))

# Day9 - Packages
"""
Create directory structure:
mypackage/
    __init__.py
    math_tools.py
Then import:
from mypackage.math_tools import add
"""

# Day10 - List Methods
nums = [1, 2, 3]
nums.append(4)      # [1,2,3,4]
nums.insert(1, 5)   # [1,5,2,3,4]
nums.remove(2)      # [1,5,3,4]

# Day11 - Set/Tuple Methods
colors = {"red", "green", "blue"}
colors.add("yellow")  # {'red', 'green', 'blue', 'yellow'}

coordinates = (10.5, 20.3)
print(coordinates.index(10.5))  # 0

# Day12 - Dict Methods
student = {"name": "John", "age": 20}
print(student.keys())    # dict_keys(['name', 'age'])
student.update({"grade": "A"})  # Adds new key




