# square_loop.py
# Display a square

from turtle_braille import *


colors = ["red","orange", "yellow", "green"]
for colr in colors:  # Do for all colors
    color(colr)
    width(40)
    forward(200)
    right(90)
done()
