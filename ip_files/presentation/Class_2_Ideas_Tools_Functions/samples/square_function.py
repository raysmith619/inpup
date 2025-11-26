# square_function.py    04Nov2025  crs, Drop import *
#                       25Feb2022  crs, from square_list.py
# Display a set of colored squares
# Use colors from a list
# define function
import turtle as tu    # Bring in turtle graphic functions
tu.speed(10)            # 10 - fastest drawing

def square(x=0, y=0, size=100, colr="red", wid=2):
    """ Display square
    :x: x position default: 0
    :y: y position default: 0
    :size: side size default: 100
    :colr: square color default: red
    :wid: line width default: 2
    """
    tu.penup()
    tu.goto(x,y)
    tu.pendown()
    tu.color(colr)
    tu.width(wid)
    for i in range(4):  # Do 4 times
        tu.forward(size)
        tu.left(90)

#
# Testing code
#

colors = ["red", "orange", "yellow",
          "green", "blue", "indigo",
          "violet"]
ncopy = 1
#ncopy = 2                   # Double list
colors = ncopy*colors      # multiply list
nsquare = len(colors)
win_size = 800  
sq_size_min = win_size/((nsquare+1)**2/2)     # Estimate size
begin = -win_size/2 - 2*sq_size_min   # lower left corner
prev_loc = begin
for i in range(nsquare):
    n = i + 1
    sq_size = n*sq_size_min
    x = prev_loc
    y = prev_loc
    wid =(i+1)*2 
    colr = colors[i%len(colors)]    # next color, wraps
    square(x,y, sq_size, colr, wid) 
    prev_loc = x + sq_size + wid  # space next sq
