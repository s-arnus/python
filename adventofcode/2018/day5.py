#!/usr/bin/python3
#The polymer is formed by smaller units which, when triggered, react with each other such that two adjacent units of the same type and opposite polarity are destroyed. Units' types are represented by letters; units' polarity is represented by capitalization. For instance, r and R are units with the same type but opposite polarity, whereas r and s are entirely different types and do not react.
#
#For example:
#
#In aA, a and A react, leaving nothing behind.
#In abBA, bB destroys itself, leaving aA. As above, this then destroys itself, leaving nothing.
#In abAB, no two adjacent units are of the same type, and so nothing happens.
#In aabAAB, even though aa and AA are of the same type, their polarities match, and so nothing happens.
#Now, consider a larger example, dabAcCaCBAcCcaDA:
#
#dabAcCaCBAcCcaDA  The first 'cC' is removed.
#dabAaCBAcCcaDA    This creates 'Aa', which is removed.
#dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
#dabCBAcaDA        No further actions can be taken.
#After all possible reactions, the resulting polymer contains 10 units.
#
#How many units remain after fully reacting the polymer you scanned?


#Plan is to go over the input that has been put into a list starting from the beginning and compareing two consecutive characters.
#If the characters do not react then check next ones. If they react then remove both of them from the list and move to the start of the list.

#Store input in a list
inputlist = []
with open("input5.txt", "r") as file:
    char = file.read(1)
    while char:
        #Add all the chars to a list that is later used over and over again
        #Do not add newline
        if char != "\n":
            inputlist.append(char.strip())
        char = file.read(1)

#Lets take a list and remove the elements as needed
print(len(inputlist))

i = 0
while i < len(inputlist):
    if i < len(inputlist) - 1:
        char1 = inputlist[i]
        char2 = inputlist[i + 1]
    if char1 != char2 and (char1.lower() == char2 or char1.upper() == char2):
        print("Deleting char1 = ", char1, "index: ",i, "and char2 = ", char2, "index: ",i + 1)
        #Deletion happens for the same index both times, as after first deletion the index changes and char2 now has index of char1
        del inputlist[i]
        del inputlist[i]
        #i = i - 1
        i = 0
        continue
    i += 1

print("Answer is: ",len(inputlist))