#!/usr/bin/env python3

import platform
import sys
from decimal import *

# Output Python version
#   OUTPUT: Using Python version 3.8.5
print("Using Python version "+platform.python_version())

# Using variable in print statement
#   OUTPUT: Hello World!
print("## HELLO WORLD")
text = "Hello"
print("{} World!".format(text))
print(f"{text} World!")     # f stands for format
print(text+" World!")
print("")     # Add empty line

# Conditions with numbers
print("## CONDITIONS")
x = 15
y = 10
if x > y:
    print("x is {} and larger than y {}".format(x, y))
    # OUTPUT: x is 19 and larger than y 15
elif x < y:
    print("x is {} and smaller than y {}".format(x, y))
    # OUTPUT: x is 10 and smaller than y 15
else:
    print("x and y are equal")
print("")     # Add empty line

# Print items in a list
print("## LIST")
list = ["one", "two", "three", "four"]
for item in list:
    print(item, end=" ")    # replace line end with space
    # OUTPUT: one two three four
print("")     # Add empty line

# Simple function with default value of 0
print("## FUNCTION")
def my_function(n = 0):
    print("Function input: {}".format(n))
    return n * 10   # multiply by 10
print("Function output: {}".format(my_function(42)))
    # OUTPUT: Function output: 420
print("")     # Add empty line

# ITEM TYPES
print("## ITEM TYPES")
#   11 is  <class 'int'>
#   14.56 is  <class 'float'>
#   test is  <class 'str'>
#   True is  <class 'bool'>
#   None is  <class 'NoneType'>
#   (1, 2) is  <class 'tuple'>
#   [1, 2] is  <class 'list'>
#   {'one': 1} is  <class 'dict'>
x = [11, 14.56, "test", True, None, (1,2), [1,2], {"one": 1}]
for item in x:
    print(item,"is ",type(item))
print("")     # Add empty line

# Evaluates as false
print("## FALSE")
if not 0:
    print("0 evaluates as False")
if not None:
    print("None evaluates as False")
if not False:
    print("False evaluates as False")
if not "":
    print("Empty string evaluates as False")
print("")     # Add empty line

# MATH
print("## MATH")
x = 5 * 2
y = 5 / 2   # Python 3 outputs float
z = 5 // 2  # Integer division
g = 5 % 2   # Modulo, remainder
b = .10 + .10 + .10 - .30
d = Decimal(".10") + Decimal(".10") + Decimal(".10") - Decimal(".30")
print("x={} y={} z={} g={} b={} d={}".format(x,y,z,g,b,d))
# OUTPUT: x=10 y=2.5 z=2 g=1 b=5.551115123125783e-17 d=0.00
print("")     # Add empty line

# TUPLE (immutable)
print("## TUPLE")
tuple = ("one", "two", "three", "four")
for item in tuple:
    print(item, end=" ")    # replace line end with space
    # OUTPUT: one two three four
print("\n")     # Add newline

# RANGE
print("## RANGE")
my_range = range(5)
print(my_range)
# OUTPUT: range(0, 5)
for item in my_range:
    print(item, end=" ")    # replace line end with space
    # OUTPUT: 0 1 2 3 4
print("\n")     # Add newline

# DICTIONARY
print("## DICTIONARY")
my_dictionary = { "one": 1, "two": 2, "three": 3 }
for item in my_dictionary:
    print(item, end=" ")    # replace line end with space
    # OUTPUT: one two three
print("")     # Add empty line
for key, value in my_dictionary.items():
    print(key, value, end=" ")    # replace line end with space
    # OUTPUT: one 1 two 2 three 3
print("\n")     # Add newline

# BOOLEAN
print("## BOOLEAN")
a = True
b = False
c = True
d = "red"
e = ("green", "red", "blue")

if a or b and c:
    print("True")
if not b:
    print("True")
if d in e:
    print("True")
if d is e[1]:
    print("True",id(d),id(e[1]))
print("")     # Add empty line

# WHILE LOOP
print("## WHILE LOOP")
x = 1
while x <= 5:
    print(x)
    x = x +1
print("")     # Add empty line

# LOOP CONTROLS
# continue - continue to next element
# break - break out of the loop
# else - executes only if loop executes normally
x = 1
end = "False"
while x <= 4:
    if x == 2:
        # Skip 2
        x = x +1
        continue
    print(x,end)
    x = x +1
else:
    # else executes only if loop executes normally
    end = "True"
print(end)
print("")     # Add empty line

## CLASS
print("## CLASS")
class Test:
    one = "Picked it up"
    two = "Pow!"
    
    def pick(self):
        print(self.one)
    
    def throw(self):
        print(self.two)

testing = Test()
testing.pick()
testing.throw()
print("")     # Add empty line

## EXCEPTIONS
print("## EXCEPTIONS")
# x = int("test")
# Would Output:
#   Traceback (most recent call last):
#     File "/home/sander/GIT/python/samples/samples.py", line 183, in <module>
#       x = int("test")
#   ValueError: invalid literal for int() with base 10: 'test'
try:
    x = int(None)
except ValueError:
    print("Caught a value error")
except TypeError as e:
    print(f"TypeError: {e}")
    # Outputs: 
    #   TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
except:
    print(f"Caught an error: {sys.exc_info()}")
    # Outputs something like:
    #   Caught an error: (<class 'TypeError'>, TypeError("int() argument must be a string, a bytes-like object or a number, not 'NoneType'"), <traceback object at 0x7f2ec65f20c0>)
else:
    # If try succeeds
    print(x)

