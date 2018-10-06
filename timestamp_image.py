#!/usr/bin/python3
import sys, os, re
from PIL import Image, ImageDraw, ImageFont

#This script takes all the images in filelocation and adds timestamp text
#Specific filenames are expected: 2017-06-03_2200.jpg
#Modified images are written to new directory in outputlocation

#TODO ask user input to get the picture location
#File input location
filelocation = "/home/user/Pictures/camera/"
#Output location where the modified files will be written
outputlocation = "/home/user/Pictures/out/"
#Truetype font location:
fontlocation = "/usr/share/fonts/truetype/freefont/FreeSans.ttf"
#Changing directory to where the pictures are
os.chdir(filelocation)
#Print current working directory
print ("Starting processing pictures in: " + os.getcwd())

#Craete file output location if it does not exist
if not(os.path.isdir(outputlocation)):
    try:  
        os.makedirs(outputlocation)
    except OSError:  
        print ("Creation of the directory %s failed" % outputlocation)
    else:  
        print ("Successfully created the directory %s" % outputlocation)

#Identify image files in given directory
for infile in os.listdir(filelocation):
    try:
        #Image.open(infile) will only continue with image files
        with Image.open(infile) as im:
            #print(infile, im.format, "%dx%d" % im.size, im.mode)
            #Get the date part of the filename into variables
            matchObj = re.match( '(\d{4})-(\d{2})-(\d{2})_(\d{4}).*', infile, re.M|re.I)
            if matchObj:
                #Print the whole matched line: 2017-06-03_2200.jpg
                #print ("matchObj.group() : ", matchObj.group())
                #Print the first mathced group: 2017
                #print ("year  : ", matchObj.group(1))
                year = matchObj.group(1)
                #Print the second mathced group: 06
                #print ("month : ", matchObj.group(2))
                month = matchObj.group(2)
                #Print the third mathced group: 03
                #print ("day   : ", matchObj.group(3))
                day = matchObj.group(3)
                #Print the fourth mathced group: 2200
                #print ("time  : ", matchObj.group(4))
                time = matchObj.group(4)
                #print ("year/month/day time:", year + month + day, time)

                #Print timestampt to the pictures and store them in new directory
                fnt = ImageFont.truetype(fontlocation, 20) #Specify location font and size in points
                d = ImageDraw.Draw(im)
                # d.text((top left corner of the text), "String to print", font=fnt, fill=(Color for the text))
                d.text((500,365), year + month + day + " " + time, font=fnt, fill=(255, 255, 255))
                
                #Save the new file with new filename prefix
                #print(filelocation + "output" + infile)
                try:
                    im.save(outputlocation + "output" + infile)
                except:
                    print("Saving files failed")
            else:
                print("No match for: " + infile)
    except IOError:
        #Nothing happens when pass executes
        #All non-image files are ignored and not mentioned
        pass
print("Modified files saved in", outputlocation)
print("Done")