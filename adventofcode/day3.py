##!/usr/bin/python3
#The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.
#
#Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined as follows:
#
#The number of inches between the left edge of the fabric and the left edge of the rectangle.
#The number of inches between the top edge of the fabric and the top edge of the rectangle.
#The width of the rectangle in inches.
#The height of the rectangle in inches.
#A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric represented by # (and ignores the square inches of fabric represented by .) in the diagram below:
#
#...........
#...........
#...#####...
#...#####...
#...#####...
#...#####...
#...........
#...........
#...........
#The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas. For example, consider the following claims:
#
##1 @ 1,3: 4x4
##2 @ 3,1: 4x4
##3 @ 5,5: 2x2
#Visually, these claim the following areas:
#
#........
#...2222.
#...2222.
#.11XX22.
#.11XX22.
#.111133.
#.111133.
#........
#The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others, does not overlap either of them.)
#
#If the Elves all proceed with their own plans, none of them will have enough fabric. 
#How many square inches of fabric are within two or more claims?

#Check each squere against each claim and see if it is within two or more claims. If it is then store it as 1 matching square inche
#Every square is checked only once, so the final result will be accurate

#Each squere has two coordinates x1,y1 (top left corner) and x2,y2 (bottom right corner)
#Each claim has similar coordinates x3,y3 (top left corner) and x4,y4 (bottom right corner)

#Add input from file into list
inputlist = []
with open("input3.txt", "r") as file:
    line = file.readline()
    while line:
        #Add all the lines to a list that is later used over and over again
        inputlist.append(line.strip())
        line = file.readline()

#Plan is to go over all the squares (square inches) from top right to bottom left and in every case check whether the square is inside a claim more than twice
#NB! This is very slow and not optimal
#Define how large the fabric is
maxfabric = 1000
#Count the final result of how many square inches of fabric are within two or more claims
count = 0
y1 = 0
y2 = 1
while y1 < maxfabric:
    print("Checking row " + str(y1))
    #y1 determins the row. While it is 0 the first row of square inches is checked. Then it is incremented
    #y2 determins the height of the square inch we are comparing to, as it needs to be 1 inches then that stays constant and incraeses with y1
    #x1 determins the column. 
    #x2 is contantly higher by 1 
    #Both of the x values are reset when we start with another row
    x1 = 0
    x2 = 1
    while x1 < maxfabric:
        #For every square track the number of times it is inside different claims
        conflict = 0
        #print(x1,y1,x2,y2)
        #Go over each claim in the input list
        for claim in inputlist:
            #Parse input and calculate coordinates for the top right (x3,y3) and bottom left (x4,y4) corner of each claim
            ID = claim.split( )[0]
            x3 = claim.split( )[2].split(',')[0]
            y3 = claim.split( )[2].split(',')[1][:-1]
            x4 = int(claim.split( )[3].split('x')[0]) + int(x3)
            y4 = int(claim.split( )[3].split('x')[1]) + int(y3)
            #print("ID = " + str(ID) + "; x1,y1 = " + str(x1) + "," + str(y1) + "; x2,y2 = " + str(x2) + "," + str(y2) + "; x3,y3 = " + str(x3) + "," + str(y3) + "; x4,y4 = " + str(x4) + "," + str(y4))
            #Check if the square is inside any of the claims 
            #This is the case when (x1 and x2 are within x3 until x4) and (y1 and y2 are within y3 until y4)
            if int(x3) <= int(x1) <= int(x4) and int(x3) <= int(x2) <= int(x4) and int(y3) <= int(y1) <= int(y4) and int(y3) <= int(y2) <= int(y4):
                #print("Square: " + str(x1) + "," + str(y1) + "," + str(x2) + "," + str(y2) + " inside ID " + ID)
                conflict = conflict + 1
        #print(conflict)
        if int(conflict) >= 2:
            #print("Oh no square: " + str(x1) + "," + str(y1) + "," + str(x2) + "," + str(y2) + " inside several claims!")
            count = count + 1
        x1 = x1 + 1
        x2 = x2 + 1
    y1 = y1 + 1
    y2 = y2 + 1
print(count)