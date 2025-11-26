# notes.py  26-Jul-2018
"""
Write a "Notes" program. The program will display lines
from a text file, containing a given text string.
Testing new computer setup with GitHub
Test:
file name = "people.notes"
text = "Watertown"
 Implementation Iterations:
Setup test file(s): "test.notes",  "people.notes"
    1.	Read specific file e.g. "test.notes", printing out all lines
    2.	Print only lines containing "student"
            How to match lines ? Google "python search for substring" ?
            Support case insensitive match (Student, STUDENT)
    3.	Prompt for, then accept file name, pattern
    4.	[Extra Credit]  Support multiple text patterns

"""
# In some environments, e.g. Visual Studio Code
# the default place to look for files is NOT
# the directory of the program file
# The following two lines sets the default
# directory to that of this source file.
import os
os.chdir(os.path.dirname(__file__))
file_name = "test.notes"

