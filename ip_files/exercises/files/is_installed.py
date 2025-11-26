#is_installed.py    25Jul2024  crs, Author
""" 
Check if python module is installed
Check is done in a separate file so the check is done in
a new process in order to look a new context
"""
import os
import sys
import importlib
import subprocess

def is_installed_local(module):
    """ Check if installed
    :module: module name
    """
    if module == "wxpython":
        module = "wx"       # Different import name
        
    importlib.invalidate_caches()   # Incase newly installed
    try:
        mod = importlib.import_module(module)
        if mod is None:
            print(f"module: {module} is None")
            return False
    except Exception as e:
        print(f"module: {module} Error: {e}")
        return False
    
    return True


def is_installed(module):
    """ Check if installed
    Does the import is a called process to test the basic environment
    :module: module name
    """
    src_dir = os.path.dirname(__file__)
    res = subprocess.run(['python', 'is_installed.py', module],
                    cwd=src_dir,
                    capture_output=True, text=True)
    if res.stdout.startswith("YES"):
        return True
    
    return False


if __name__ == '__main__':
    
    module = sys.argv[1] if len(sys.argv) > 1 else "is_installed"
    print(f"is_installed_local: {module}")
    if is_installed_local(module):
        print('YES')
    else:
        print('NO')
    
    