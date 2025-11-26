#import_turtle_n.py     16Jun2024  crs, Author
"""
import <module>
Access each turtle function via turtle.<member_name>
"""
from random import randint,uniform

import turtle

colors = ["red", "orange", "yellow",
          "green", "blue", "indigo",
          "violet"]
nt = 4   # Number of turtles
nsides = 10  # Number of sides each
side_base = 20
max_x = 320
max_y = max_x
start_range = int(max_y*.8)

turtles = []    # List of turtles
for it in range(nt):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(it)                             # Increasing drawing speed
    t.color(colors[it%len(colors)])
    x = randint(-start_range, start_range)  # Random starting location
    y = randint(-start_range, start_range)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.dot(50)                   # Mark beginning of each turtle's path
    turtles.append(t)

for isd in range(nsides): # do each side
    side = (isd+1)*side_base
    for t in turtles:    # Rotate through turtles
        t.width((nsides-isd+1)*2)           # Decreasing widths each step
        maxv = int(max_x*((isd+1)/nsides))
        if maxv < 200:
            maxv = 200
        x = randint(-maxv, maxv)        # adding a line to a random location
        y = randint(-maxv, maxv)
        t.goto(x,y)

turtle.done()    
    
            
