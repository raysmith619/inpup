# notes_3e.py   13Oct2022  crs, from notes_3d
#               26-Jul-2018
"""
Re-ask if can't open data file

Write a "Notes" program. The program will display lines
from a text file, containing a given text string.
Test:
file name = "people.notes"
text = "Watertown"
Loop asking for new file
Loop over patterns
Use regular expression search
"""
import os
os.chdir(os.path.dirname(__file__))
file_name = "test.notes"

import re

# Default values
def_file_name = "test.notes"
def_pattern = "student"

while True:
    # Set to default values
    pattern = def_pattern

    while True:
        file_name = def_file_name
        inp = input("Enter file name[" + file_name + "] ")
        inp = inp.rstrip()
        if inp == "":
            inp = file_name
        file_name = inp
        while True:         # Loop over patterns
            while True:
                try:
                    finp = open(file_name)
                    break               # Got opened file
                
                except IOError :
                    print("Can't open file ", file_name)
                    finp = None
                    break
                
            if finp is None:
                break   # Try file again
                
            inp = input("Enter pattern(rex)[" + pattern + "] ")
            if inp == "":
                inp = pattern
            pattern = inp
            for line in finp:
                match = re.search(pattern, line, re.I)
                if (match):
                    print(line, end="")
