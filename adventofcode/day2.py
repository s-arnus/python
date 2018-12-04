#!/usr/bin/python3
#For example, if you see the following box IDs:
#
#abcdef contains no letters that appear exactly two or three times.
#bababc contains two a and three b, so it counts for both.
#abbcde contains two b, but no letter appears exactly three times.
#abcccd contains three c, but no letter appears exactly two times.
#aabcdd contains two a and two d, but it only counts once.
#abcdee contains two e.
#ababab contains three a and three b, but it only counts once.
#Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which appears exactly three times. 
#Multiplying these together produces a checksum of 4 * 3 = 12.
#
#What is the checksum for your list of box IDs?

#Count the number of time there are two same characters on a line
count_two = 0

#Count the number of time there are three same characters on a line
count_three = 0

#For each input line
with open("input2.txt", "r") as file:  
   line = file.readline()
   while line:
        #print(line)
        #For each letter in the line
        i = 0
        #Reset line based character counter
        checked = []
        #Counters for not counting similar occasions
        counted_two = False
        counted_three = False
        while i < len(line):
            #Check if the character is alphabetic
            if line[i].isalpha():
                letter = line[i]
                #print(letter)
                #if the letter exists two or three times in the line then increase corresponding counter and add the letter to checked list
                if line.count(letter) == 2 and not letter in checked and not counted_two:
                    #print("Two times: " + letter)
                    count_two = count_two + 1
                    checked.append(letter)
                    counted_two = True
                elif line.count(letter) == 3 and not letter in checked and not counted_three:
                    #print("Three times: " + letter)
                    count_three = count_three + 1
                    checked.append(letter)
                    counted_three = True  
                else:
                    #print("Did not exist two or three times: " + letter)
                    checked.append(letter)
                #check if next letter has already been counted for this line
                
                #Take next letter in the line
            i = i + 1
        #Take the next line
        line = file.readline()
#Calculating checksum
print("Number of times two letters seen in a line: " + str(count_two))
print("Number of times three letters seen in a line: " + str(count_three))
print("Checksum: " + str(count_two * count_three))
