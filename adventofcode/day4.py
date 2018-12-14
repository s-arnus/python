#!/usr/bin/python3
#
#For example, consider the following records, which have already been organized into chronological order:
#
#[1518-11-01 00:00] Guard #10 begins shift
#[1518-11-01 00:05] falls asleep
#[1518-11-01 00:25] wakes up
#[1518-11-01 00:30] falls asleep
#[1518-11-01 00:55] wakes up
#[1518-11-01 23:58] Guard #99 begins shift
#[1518-11-02 00:40] falls asleep
#[1518-11-02 00:50] wakes up
#[1518-11-03 00:05] Guard #10 begins shift
#[1518-11-03 00:24] falls asleep
#[1518-11-03 00:29] wakes up
#[1518-11-04 00:02] Guard #99 begins shift
#[1518-11-04 00:36] falls asleep
#[1518-11-04 00:46] wakes up
#[1518-11-05 00:03] Guard #99 begins shift
#[1518-11-05 00:45] falls asleep
#[1518-11-05 00:55] wakes up
#Timestamps are written using year-month-day hour:minute format. The guard falling asleep or waking up is always the one whose shift most recently started. Because all asleep/awake times are during the midnight hour (00:00 - 00:59), only the minute portion (00 - 59) is relevant for those events.
#Note that guards count as asleep on the minute they fall asleep, and they count as awake on the minute they wake up. For example, because Guard #10 wakes up at 00:25 on 1518-11-01, minute 25 is marked as awake.
#
#If you can figure out the guard most likely to be asleep at a specific time, you might be able to trick that guard into working tonight so you can have the best chance of sneaking in. You have two strategies for choosing the best guard/minute combination.
#
#Strategy 1: Find the guard that has the most minutes asleep. What minute does that guard spend asleep the most?
#
#In the example above, Guard #10 spent the most minutes asleep, a total of 50 minutes (20+25+5), while Guard #99 only slept for a total of 30 minutes (10+10+10). Guard #10 was asleep most during minute 24 (on two days, whereas any other minute the guard was asleep was only seen on one day).
#
#While this example listed the entries in chronological order, your entries are in the order you found them. You'll need to organize them before they can be analyzed.
#
#What is the ID of the guard you chose multiplied by the minute you chose? (In the above example, the answer would be 10 * 24 = 240.)

from datetime import datetime, date, time
import collections

#List to store values
guard_sleep_list = []
#List to store minutes when the guards were asleep, to later find the minute that was spent asleep most
sleep_counter_list = []

#Store input in a list
inputlist = []
with open("input4.txt", "r") as file:
    line = file.readline()
    while line:
        #Add all the lines to a list that is later used over and over again
        inputlist.append(line.strip())
        line = file.readline()

#Sort input
inputlist.sort()

for line1, line2 in zip(inputlist, inputlist[1:]):
    #Take first and second line from input
    #parse the date and time from it
    date1 = line1.split( )[0][1:]
    time1 = line1.split( )[1][:-1]
    action1 = line1.split( )[2]
    date2 = line2.split( )[0][1:]
    time2 = line2.split( )[1][:-1]
    action2 = line2.split( )[2]
    #parse the Guard number to a variable
    if action1 == "Guard":
        ID1 = line1.split( )[3]
    if action2 == "Guard":
        ID2 = line2.split( )[3]
    #if the guard falls asleep and wakes up then calculate the number of minutes he slept
    if action1 == "falls" and action2 == "wakes":
        #Parsing out year, month, day, hours, minutes then combining them into datetime variables that will be used to calculate minutes slept
        year1 = int(date1.split("-")[0])
        month1 = int(date1.split("-")[1])
        day1 = int(date1.split("-")[2])
        hour1 = int(time1.split(":")[0])
        minute1 = int(time1.split(":")[1])
        datetime1 = datetime.combine(date(year1, month1, day1), time(hour1, minute1))
        year2 = int(date2.split("-")[0])
        month2 = int(date2.split("-")[1])
        day2 = int(date2.split("-")[2])
        hour2 = int(time2.split(":")[0])
        minute2 = int(time2.split(":")[1])
        datetime2 = datetime.combine(date(year2, month2, day2), time(hour2, minute2))

        slept = (datetime2 - datetime1).total_seconds() / 60
        #print("Guard " + ID1 + " was asleep for: " + str(slept))
        #Create a list that contains an element containing ID and minute for every minute a guard is asleep. 
        #So that for guard #10 being asleep between 00:24-00:29, the list would be ['#10_24', '#10_25', '#10_26', '#10_27', '#10_28']
        #Similarly for all the guards and days. 
        #Once we know the guard we are interested in we can get the most common element starting with guard ID to get the minute he was asleep most of the times
        #print("Minute 1: "+ str(minute1) + " minute 2: " + str(minute2))
        for i in range(minute1, minute2):
            sleep_counter_list.append(ID1+"_"+str(i))
        #Adding the first value to the list
        if len(guard_sleep_list) == 0:
            guard_sleep_list.append(ID1+"_"+str(slept))
            #Jump to next lines
            continue
        #Checking if the same guard has already a sleep recorded
        for counter, value in enumerate(guard_sleep_list):
            #print(counter, value)
            if ID1 in value:
                #Store the new value by adding the sleep sums (sleep1 + guard_slept)
                sleep1 = value.split("_")[1]
                #print(ID1+"_"+str(float(slept)+float(sleep1)))
                #Remove the previous value that is now wrong
                #print("Removing from list: " + value)
                guard_sleep_list.remove(value)
                #Add the new value to the same position
                #print("Adding new value to the list: " + ID1+"_"+str(float(slept)+float(sleep1)))
                guard_sleep_list.insert(counter, ID1+"_"+str(float(slept)+float(sleep1)))
                #print("New list: " + str(guard_sleep_list))
                break
            elif counter == (len(guard_sleep_list) - 1):
                #print("Adding missing guard to list: " + ID1+"_"+str(slept))
                guard_sleep_list.append(ID1+"_"+str(slept))
                #print("New list: " + str(guard_sleep_list))
                break
maximum = 0.0
max_ID = "null"
for item in guard_sleep_list:
    guard_ID = item.split("_")[0]
    total_slept = item.split("_")[1]
    #print(guard_ID + total_slept)
    if float(total_slept) > float(maximum):
        maximum = total_slept
        max_ID = guard_ID
print("Guard " + max_ID + " slept the longest. " + str(maximum) + " minutes")

#Finding the minute that guard spend sleeping most of the times
#We have a list with guard ID and every minute spent asleep: #10_05, #10_06, etc.
#Now just need to find the most common value that starts with guard ID (max_ID)
c = collections.Counter(sleep_counter_list)
#NB! value in most_common might need tuning if no answers or several are returned
for letter, count in c.most_common(14):
    if max_ID in letter:
        minute = letter.split("_")[1]
        print("Guard slept most during minute:  ",minute, " counted ", count, " times")
        guard = max_ID[1:]
print("Answer = ", (int(guard) * int(minute)), "(",guard,"*",minute,")")
