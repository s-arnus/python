#!/usr/bin/python3
# -*- coding: utf-8 -*-

# This script is an attempt to solve:
# https://adventofcode.com/2019/day/1

"""
Fuel required to launch a given module is based on its mass.
Specifically, to find the fuel required for a module,
take its mass, divide by three, round down, and subtract 2.

The Fuel Counter-Upper needs to know the total fuel requirement.
To find it, individually calculate the fuel needed for the mass 
of each module (your puzzle input), then add together all the fuel values.
"""

import math

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

total_fuel_required = 0
#Read lines from input file
with open("day1_input.txt", "r") as file:
    line = file.readline()
    while line:
        #removing whitespace characters
        line = line.strip()
        #checking if the input lines are all integers
        try:
            line = int(line)
            #print(str(line))
            #for each input line calculate fuel requirement and add the fuel requirement to total requirement
            module_fuel_required = round_down(line / 3) - 2
            #print("module_fuel_required:",int(module_fuel_required))
            total_fuel_required = int(total_fuel_required) + int(module_fuel_required)
        except:
            print("Input is not integer",line)
        line = file.readline()
print("Result: " + str(total_fuel_required))