# shapes_simple.py  14Jun2024  crs, simplify shapes_around
#                   16Feb2022  crs, Author
"""
Make a bunch of regular polygon shapes
using functions
"""
from turtle import *


def polygon(nside=3, x=0, y=0,
            side=100, colr="blue",
            wid=2):
    """ Create regular polygon
    :nside: number of sides default: 3
    :x: initial position default: 0
    :y: initial y position default: 0
    :side: side length default: 0
    :colr: line color default: blue
    :wid: line width default: 2
    """
    penup()
    goto(x,y)
    pendown()
    
    ext_angle = 360/nside
    width(wid)
    color(colr)
    for i in range(nside):
        forward(side)
        left(ext_angle)

""" Testing
Note that we use if __name__ == "__main__" to that
this code only gets executed if we are running this
file by itself
"""
if __name__ == "__main__":
    
    colors = ["red","orange", "yellow"
                  "green", "blue", "indigo",
                  "violet"]
    for i in range(8):            
        colr = colors[i%len(colors)]
        polygon(nside=i+3, colr=colr, wid=2+i)
