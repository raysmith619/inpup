#dice_display.py    09Oct2024
""" Display dice - Two dimentional
"""
import turtle as tk
def_die_edge = 50
def_die_color = "red"
def_dot_color = "black"

dot_pos = {
    """die spots are in a 3-by-3 arrangement"""
    1: [(1,1)],    #[row,col]
    2: [(0,0), (2,2)],
    3: [(0,0), (1,1), (2,2)],
    4: [(0,0), (2,0), (2,0), (2,2)],
    5: [(0,0), (2,0), (1,1), (0,2), (2,0)],
    6: [(0,0), (1,0), (2,0), (0,2), (1,2), (2,2)],
    }

def die_display_edge(x, y, n, die_edge=def_die_edge):
    """ Display die edge
    :prameters: see die_display
    """
    tk.penup()
    tk.goto(x, y)
    tk.color(def_die_color)
    tk.pendown()
    tk.begin_fill()
    for i in range(4):
        tk.forward(die_edge)
        tk.left(90)
    tk.end_fill()

def die_display_dot(x, y, dot, die_edge=def_die_edge):
    """ Display die dots
    :prameters: see die_display
    :dot: row,col tuple of dot location within dot grid
    """
    dot_irow,dot_icol = dot     # Unpack pair
    edge_xy_off = 5 # Offset from edge
    dot_size = (die_edge-2*edge_xy_off)/4
    dot_cent_sep = (die_edge-2*edge_xy_off)/3
    dot_cent_x = x + edge_xy_off + dot_irow*dot_cent_sep
    dot_cent_y = y + edge_xy_off + dot_icol*dot_cent_sep
    tk.penup()
    tk.goto(dot_cent_x, dot_cent_y)
    tk.pendown()
    tk.dot(dot_size)

def die_display_dots(x, y, n, die_edge=def_die_edge):
    """ Display die dots
    :prameters: see die_display
    """
    dot_list = dot_pos[n]
    for dot in dot_list:
        die_display_dot(x,y,dot, die_edge=die_edge)


def die_display(x, y, n, die_edge=def_die_edge):
    """ Display die
    :x: x-coordinate of lower left corner
    :y: y-coordinate of lower left corner
    :n: die value
    :die_edge: size of die edge default=50
    """
    die_display_edge(x, y, n, die_edge=die_edge)
    die_display_dots(x, y, n, die_edge=die_edge)
    
