#file_search.py 27May2024  crs
"""
Module to search file for string pattern
"""
import re
import os
import pathlib  # Python 3.4+

def file_search(file, pattern, lplev=1):
    """ Search for pattern within file.  Assumes
    absolute path or default directory.
    :lplev: list file path level 0 - no file - just line
                                 1 - file base name
                                 > 1 more directory levels
            default: 1 - file base name
    """
    file_name = ""
    pparts = pathlib.PurePath(file).parts
    topi = min(lplev,len(pparts))-1
    if topi > 0:
        file_name = pparts[topi]
    for i in range(topi-1, 0, -1):
        file_name = os.fspath(PurePath(file_name, pparts(i)))
    print(f"file_name: {file_name}")
    try:
        with open(file) as finp:
            line_no = 0
            for line in finp:
                line_no += 1
                if re.search(pattern, line, re.I):
                    print(f"{file_name}:{line_no:3} {line}",
                          end="")
    except:
        print(f"{file_name} - can't open/read - skipped")

#Selftest - if file run by itself
if __name__ == "__main__":
    def test_it(file, pattern, lplev=1):
        """ Test function
        :file: test file name
        :pattern: test pattern
        :lplev: test name components
                default: 1
        """
    file_search(__file__, "if")

    file_search(__file__, "if", lplev=lplev)
    
    
