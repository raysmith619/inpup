#list_lines.py  23Jul2024  crs
"""
List lines in file that have a pattern
Hopefully to develpe a replacement for perl -ane '{.....} *.py
"""
import os
import re

wk_dir = os.path.dirname(__file__)  # Our directory
py_files =[f for f in os.listdir(wk_dir) if re.match(r'^.*\.py$', f)]
for f in py_files:
    print(f)