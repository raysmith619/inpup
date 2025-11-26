#from_turtle_import.py     30Dec2021  crs, Author
"""
from <module> import * 
Bring in some or all (*) functions
from module
"""
from turtle import *    # Bring in all functions

color("red")
side = 100
angle = 60
for i in range(6):
    forward(side)
    right(angle)
    
