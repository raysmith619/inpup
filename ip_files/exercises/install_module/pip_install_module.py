# pip_install_module.py
# Install python module for currently executing python, using: -m pip install
# usually IDLE
#
import sys
from pathlib import Path
import subprocess

def install_modules(install_list):
    """ Install list of modules
    :install_list: list of module names
    """
    pgm_list = ["py", "-m", "pip", "install"]
    pgm_list.extend(install_list)
    print(f"Running: {pgm_list}")
    pgm_run = subprocess.Popen(pgm_list,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                )
    pgm_out, pgm_error = pgm_run.communicate()
    pgm_run.wait()
    print(f"pgm_error: {pgm_error}")
    print(f"output:\n{pgm_out.decode()}")
    
    
install_list = ["pyttsx3",
                "pyttsx4", "wxpython", "numpy",
                "pysinewave", "sounddevice",
               ]

install_modules(install_list)

