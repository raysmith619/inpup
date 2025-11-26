#files_search_simp.py 27May2024  crs
"""
Module to search list of files for string pattern
"""
import re
import os

from file_search_simp import file_search

def files_search(dir_name=".", file_pat=r"\.py", pattern="."):
    """ Search for pattern within file within a directory.
    :dir: directory default: current directory
    :file_pat: regular expression pattern for file name
                default: \.py (python file)
    :pattern: regular expression pattern to search fo
                default: . any character
    """
    files = os.listdir(dir_name)
    for file in files:
        if re.search(file_pat, file, re.I):
            fpath = os.path.join(dir_name,file)
            file_search(fpath, pattern)
        
#Selftest - if file run by itself
if __name__ == "__main__":

    def test_it(dir_name=".", file_pat=r"\.py", pattern=r"\d\d\w+\d\d"):
        print(f"\ndir: {os.path.abspath(dir_name)}"
              f" file_pat: {file_pat}"
              f" pattern: {pattern}")
        files_search(dir_name=dir_name, file_pat=file_pat,
                     pattern=pattern)
    test_it()
    
    test_it(dir_name="..")
    test_it(dir_name="../..")
    
    
