#!/usr/bin/python3
import sys, os, re
import shutil #for copying files
from PIL import Image

#This script deleted night pictures
#Very basic check is done only based on one pixel
#If the pixels RGB value is very dark then don't copy it to a new directory

#File input location
filelocation = "/home/sander/Pictures/camera/"
#Output location where the modified files will be written
outputlocation = "/home/sander/Pictures/bright/"

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
                #rgb_im = im.convert('RGB')
                #r, g, b = rgb_im.getpixel((1, 1))
                r, g, b = im.getpixel((33, 457))
                #Black has RGB values of 0 0 0. The closer the sum of thre three colours is to zero the darker the picture.
                rgbsum = int(r) + int(g) + int(b)
                #print(infile, " RGB: ", r, g, b, " sum:", rgbsum)
                if ( rgbsum < 150 ):
                    #Ignoring dark pictures
                    #print("Dark picture with sum of", rgbsum, " ", infile)
                    pass
                else:
                    #Copy only pictures that are not dark
                    shutil.copy(infile, outputlocation + "out" + infile)
            else:
                print("No match for: " + infile)
    except IOError:
        #Nothing happens when pass executes
        #All non-image files are ignored and not mentioned
        pass
print("Modified files saved in", outputlocation)
print("Done")