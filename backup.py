#!/usr/bin/python3
# Script to do backups
# NB! Not functional
import sys
import os

# Ask for source and destination
def ask_for_input(argument):
    answer = input(argument)
    # Check if it is valid file or directory
    if os.path.isfile(answer) or os.path.isdir(answer):
        return answer
    # If not, then ask again
    else:
        print("Provided input was not valid. Exiting.")
        sys.exit(1)

# Copy source recursively to destination
#TODO

# A module’s __name__ is set equal to '__main__' when read from standard input, a script, or from an interactive prompt.
if __name__ == "__main__":
    # Not expecting any arguments
    if len(sys.argv) == 1:
        # Ask what to copy and where, check if they exist
        provided_source = ask_for_input("Provide source to copy: ")
        provided_destination = ask_for_input("Provide destination to copy to: ")
        print("Source: ",provided_source)
        print("Destination: ",provided_destination)
    else:
        print("Arguments are not allowed")
        sys.exit(1)
    # Do the copying
    #TODO