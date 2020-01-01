#!/usr/bin/python3

#https://adventofcode.com/2018/day/1
#For example, if the device displays frequency changes of +1, -2, +3, +1, then starting from a frequency of zero, the following changes would occur:
#
#Current frequency  0, change of +1; resulting frequency  1.
#Current frequency  1, change of -2; resulting frequency -1.
#Current frequency -1, change of +3; resulting frequency  2.
#Current frequency  2, change of +1; resulting frequency  3.
#In this example, the resulting frequency is 3.
#
#Here are other example situations:
#
#+1, +1, +1 results in  3
#+1, +1, -2 results in  0
#-1, -2, -3 results in -6

#Input can be positive + or negative - integer. Also including zero.
result = 0
operation = "+"
with open("input.txt", "r") as file:  
   line = file.readline()
   while line:
        if line.startswith("+"):
           #print ("positive")
           #Keep the value but remove first character
           frequency = int(line.strip()[1:])
           operation = "+"
        elif line.startswith("-"):
            #print ("negative")
            #Keep the value but remove first character
            frequency = int(line.strip()[1:])
            operation = "-"
        elif line.startswith("0"):
            #print ("zero")
            frequency = int(line.strip())
            operation = "+"
        else:
            print ("unknown character: " + line)
        if operation == "+":
            result = result + frequency
        elif operation == "-":
            result = result - frequency
        line = file.readline()
print("Result: " + str(result))