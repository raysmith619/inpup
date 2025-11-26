#files_search.py 27May2024  crs
"""
Module to search list of files for string pattern
"""
import re
import os

from file_search import file_search

def files_search(files, pattern, list_base=True):
    """ Search for pattern within file.  Assumes
    absolute path or default directory.
    If a member of files is a directory, all the
    included files files in included directories
    is included.  We use 
    :files: list of files to search
    :list_base: list file basename, else full given
    """
    if not isinstance(files, list):
        files = [files] # Make a list of one
    file_list = []
    for file in files:
        if os.path.isdir(file):    
            for (root, dirs, filenames) in os.walk(file):
                for dir_file in filenames:
                    file_list.append(os.path.join(root, dir_file))
        else:
            file_list.append(file)
    print("file_list:", file_list)
    for file in file_list:
        file_search(file, pattern, list_base=list_base)
        
#Selftest - if file run by itself
if __name__ == "__main__":

    def test_it(files, lb=False):
        print("\nfiles:", files)
        files_search(files, "else")
        if lb:
            files_search(files, "else", list_base=False)
        
    files = __file__
    test_it(files, lb=True)
    
    src_dir = os.path.dirname(__file__) # files in src directory
    test_it(src_dir)
    
    src_dir = os.path.dirname(src_dir) # files in src directory
    test_it(src_dir, lb=True)
    
    
