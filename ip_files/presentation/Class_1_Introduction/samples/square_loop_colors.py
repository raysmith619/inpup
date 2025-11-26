# square_loop_colors_width.py
# Display a square

import turtle as tu     # Coloring tools

colors = ["red", "orange", "yellow", "green"]
tu.width(40)
for color in colors:  # Do for all colors
    tu.color(color)
    tu.forward(200)
    tu.right(90)
tu.done()
