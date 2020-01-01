#!/usr/bin/python3

#https://adventofcode.com/2018/day/1
#Detecting first frequency result that is seen the second time.
#For example, using the same list of changes above (+1, -2, +3, +1), the device would loop as follows:
#
#Current frequency  0, change of +1; resulting frequency  1.
#Current frequency  1, change of -2; resulting frequency -1.
#Current frequency -1, change of +3; resulting frequency  2.
#Current frequency  2, change of +1; resulting frequency  3.
#(At this point, the device continues from the start of the list.)
#Current frequency  3, change of +1; resulting frequency  4.
#Current frequency  4, change of -2; resulting frequency  2, which has already been seen.
#In this example, the first frequency reached twice is 2. Note that your device might need to repeat its list of frequency changes many times before a duplicate frequency is found, and that duplicates might be found while in the middle of processing the list.

result = 0
operation = "+"
list = [0]
inputlist = []
with open("input.txt", "r") as file:
    line = file.readline()
    while line:
        #Add all the lines to a list that is later used over and over again
        inputlist.append(line.strip())
        line = file.readline()
    #Go over the list of inputs several times until a match is found
    i = 0
    while (i < len(inputlist)):
        if inputlist[i].startswith("+"):
            #Keep the value but remove first character
            frequency = int(inputlist[i].strip()[1:])
            operation = "+"
        elif inputlist[i].startswith("-"):
            #Keep the value but remove first character
            frequency = int(inputlist[i].strip()[1:])
            operation = "-"
        elif inputlist[i].startswith("0"):
            frequency = int(inputlist[i].strip())
            operation = "+"
        else:
            print ("unknown character: " + inputlist[i])
        if operation == "+":
            result = result + frequency
        elif operation == "-":
            result = result - frequency
        #Check if the new resulting frequency is in the list already
        if result in list:
            print("First frequency reached twice: " + str(result))
            break
        #Adding result to a list
        list.append(result)
        i = i + 1
        #Once we reach the end of input stop and start again from beginning 
        if i == len(inputlist):
            i = 0