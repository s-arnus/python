#!/usr/bin/python3
import sys, os, re
import shutil #for copying files
from PIL import Image

#This script sorts out dark pictures from brigh ones
#Very basic check is done only based on two pixels (works with timelaps pictures)
#If the pixels RGB values are very dark then they are not copied to a new directory

#File input location
filelocation = "/home/user/Pictures/camera/"
#Output location where the modified files will be written
outputlocation = "/home/user/Pictures/bright/"

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
            #Get the date part of the filename into variables
            matchObj = re.match( '(\d{4})-(\d{2})-(\d{2})_(\d{4}).*', infile, re.M|re.I)
            if matchObj:
                r1, g1, b1 = im.getpixel((33, 457))
                r2, g2, b2 = im.getpixel((540, 460))
                #Black has RGB values of 0 0 0. The closer the sum of the three colours is to zero the darker the picture.
                rgbsum1 = int(r1) + int(g1) + int(b1)
                rgbsum2 = int(r2) + int(g2) + int(b2)
                #print(infile, " RGB1: ", r1, g1, b1, " sum:", rgbsum1)
                #print(infile, " RGB2: ", r2, g2, b2, " sum:", rgbsum2)
                if ( rgbsum1 < 300 or rgbsum2 < 170 ):
                    #Ignoring dark pictures
                    #print("Dark picture with sum of", rgbsum, " ", infile)
                    pass
                else:
                    #Copy only pictures that are not dark
                    shutil.copy(infile, outputlocation + infile)
            else:
                print("No match for: " + infile)
    except IOError:
        #Nothing happens when pass executes
        #All non-image files are ignored and not mentioned
        pass
print("Modified files saved in", outputlocation)
print("Done")