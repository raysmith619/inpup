# square_positional.py  04Nov2025  crs, Drop import *
#                       25Feb2022  crs,
# Display a set of colored squares
# Use colors from a list
# function paramaters have no defaults
# and must be present in call

import turtle as tu    # Graphic functions d tu.xxx

colors = ["red", "orange", "yellow",
          "green", "blue", "indigo",
          "violet"]


def square(x, y, size, colr):
    """ Display square
    :x: x location of lower left corner
    :y: y location of lower left corner
    :colr: color of square
    :size: size of side
    """
    tu.penup()
    tu.goto(x,y)
    tu.pendown()
    tu.color(colr)
    for i in range(4):  # Do 4 times
        tu.forward(size)
        tu.right(90)
    

#colors = 2*colors      # Double list
nsquare = len(colors)
sq_size_min = 10
begin = -int(sq_size_min*nsquare/2)   # lower left corner
for n in range(1, nsquare+1):
    sq_size = n*sq_size_min
    x = n*sq_size + begin
    y = n*sq_size + begin
    colr = colors[n%len(colors)]
    tu.width(n*2)
    square(x=x, y=y, size=sq_size,
           colr=colr)
tu.done()
