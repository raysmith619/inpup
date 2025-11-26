# square_loop.py
# Display a square

from turtle_braille import *

color("blue")
colors = ["red","orange","yellow", "green"]
width(40)
for colr in colors:  # Do for all colors
    color(colr)
    forward(200)
    right(90)
done()
