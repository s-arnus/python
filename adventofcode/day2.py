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

#PART 2
#The boxes will have IDs which differ by exactly one character at the same position in both strings. For example, given the following box IDs:
#abcde
#fghij
#klmno
#pqrst
#fguij
#axcye
#wvxyz
#The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). 
#However, the IDs fghij and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.
#
#What letters are common between the two correct box IDs? (In the example above, this is found by removing the differing character from either ID, producing fgij.)

print('\n' + "PART TWO FALLOWS")
#Empty list to store the input
inputlist = []
#Empty list to store the answer
answer = []
done = 0
#For each line go throught all the other lines and compare it. Find a string that is different by exactly one character.
with open("input2.txt", "r") as file:
    line = file.readline()
    while line:
        #Add all the lines to a list that is later used over and over again
        inputlist.append(line.strip())
        line = file.readline()
    #Go over the list of inputs to find a match
    i = 0
    while (i < len(inputlist)):
        line1 = inputlist[i]
        #print("Starting to compare: " + line1 + " index(i): " + str(i))
        j = 0
        #For every line check it agains other lines in the input list
        while (j < len(inputlist)):
            #Don't check the line with itself
            if i is not j:
                difference = 0
                line2 = inputlist[j]
                #print("Comparing against: " + line2 + " index(j): " + str(j))
                #Check characters in different strings but same postions and add the number of differences to a variable
                k = 0
                while (k < len(line1)):
                    #print("Comparing char: " + line1[k] + " against: " + line2[k])
                    if line1[k] is not line2[k]:
                        difference = difference + 1
                    k = k + 1
                #If there was only one difference then we have a winner
                if difference == 1 and done is not 1:
                    print("Line1 " + str(line1) + " and line2 " + str(line2) + " differ by " + str(difference))
                    #Find the answer by removing the different character
                    l = 0
                    while (l < len(line1)):
                        if line1[l] is line2[l]:
                            answer.append(line1[l])
                        l = l + 1
                    done = 1
            j = j + 1
        i = i + 1
print("Answer is: " + ''.join(answer))