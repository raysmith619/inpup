#file_components.py
import os
print(f"pathsep:{os.path.sep}")
components = __file__.split(os.path.sep)
print(f"components: {components}")
print(f"last2: {components[-2:]}")
dir_base = os.path.join(*components[-2:])
print(f"dir+base: {dir_base}")
    