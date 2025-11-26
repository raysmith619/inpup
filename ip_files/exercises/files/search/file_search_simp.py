#file_search_simp.py 28May2024  crs
"""
Module to search file for string pattern
"""
import re
import os

def file_search(file, pattern):
    """ Search for pattern within file.  Assumes
    absolute path or default directory.
    """
    file_name = os.path.basename(file)
    try:
        finp = open(file)
        line_no = 0
        for line in finp:
            line_no += 1
            if re.search(pattern, line, re.I):
                print(f"{file_name}:{line_no:3} {line}",
                      end="")
    except:
        print(f"{file} - can't open/read - skipped")

#Selftest - if file run by itself
if __name__ == "__main__":
    def test_it(file=__file__, pat="if"):
        print(f"\nfile: {file} pat: {pat}")
        file_search(file, pat)
        
    test_it()   # Test with default test values
    test_it(pat="for")
    
    
