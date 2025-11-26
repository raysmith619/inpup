# bouncing_balls_6_bv.py    15Aug2024  crs, from bouncing_balls_6.py
#                           03Apr2024  crs, from bouncing_balls_5.py
"""
Blind version - first attempt - audio clues
Simple program to demonstrate functions development

Change ball size every so often
Using:
    -- check if time to change ball size

Upgrades:
    + Display ball
    + Update ball (simple)
    + Edge detection
    + Liven up collisions
    + Change ball size every so often
"""
import time
from random import randint
import math as ma
import turtle
from pyttsx_queued import PyttsxQueued
tt = PyttsxQueued()

def tt_talk(text, qwait=0):
    """ talk/print text
    :qwait: wait after till queue size default=0
    """
    print(text)
    tt.talk(text)
    while tt.pending() > qwait:
        screen.update()
    
# screen dimensions
window_width = 800
window_height = 800
x_edge_min = -window_width/2
x_edge_max = window_width/2
y_edge_min = -window_height/2
y_edge_max = window_height/2


screen = turtle.Screen()
screen.setup(window_width, window_height)   # Window size.
screen.tracer(0)        # Turn-off animation.

update_loop_time = .01   # Our update loop time
#update_loop_time = .1    # Slow down for development

b_t = turtle.Turtle()
b_t.hideturtle()
running = True
b_x = b_y = b_vx = b_vy = 0 # Set via start_ball
b_vx = 500
b_vy = 200

# Slow down ball speed
b_vx = 100
v_vy = 40

ball_radius = 100
ball_radius_min = 50
ball_radius_max = 200
n_collision = 0             # Number of edge collisions

ball_color_index = 4        # Index into colors
colors = ["red", "orange", "yellow",
          "green", "blue", "indigo", "violet"]

trace_level = 9     # Trace level higher == more
trace_level = 0     # Stop tracing

def start_ball():
    """ Setup ball, size, position, velocity
    """
    if trace_level > 0:
        tt_talk("start_ball()")

def ball_display():
    """ Display ball
    """
    if trace_level > 0:
        tt_talk("ball_display()")
    if trace_level > 0:
        tt_talk("ball_display()")
    ball_color = colors[ball_color_index]
    b_t.clear()
    b_t.up()
    b_t.goto(b_x,b_y)
    b_t.down()
    b_t.dot(ball_radius*2, ball_color)
    b_t.up()

def ball_edge_check():
    """ Adjust motion if/when edge touched
        Simple physics of edge collision says
            The velocity perpendicular to the
            collision edge is reversed.

    """
    if trace_level > 0:
        tt_talk("ball_edge_check()")
    global b_vx, b_vy
    global ball_color_index
    global n_collision
    global ball_radius   # we may change the radius here
    collision = False
    edge = None
    if b_vx > 0:        # Going right
        if b_x > x_edge_max-ball_radius:
            b_vx = - b_vx
            collision = True
            edge = "right"
    elif b_vx < 0:        # Going right
        if b_x < x_edge_min+ball_radius:
            b_vx = - b_vx
            collision = True
            edge = "left"
    if b_vy > 0:        # Going up
        if b_y > y_edge_max-ball_radius:
            b_vy = - b_vy
            collision = True
            edge = "top"
    elif b_vy < 0:        # Going down
        if b_y < y_edge_min+ball_radius:
            b_vy = - b_vy
            collision = True
            edge = "bottom"
    if collision:
        show_position(x=b_x, y=b_y, edge=edge)
        tt_talk(f"off {edge}")
        n_collision += 1
        ball_color_index = (ball_color_index+1)%len(colors)
        ball_color = colors[ball_color_index]
        tt_talk(ball_color)
        if n_collision % 6 == 0:    # -- Change size every sixth collision
            ball_radius = randint(ball_radius_min,
                                  ball_radius_max)
        show_direction(v_x=b_vx, v_y=b_vy)

def show_direction(v_x, v_y):
    """ Show ball direction
        Use clock face 12 = Up, 3 = Right
        :v_x: x velocity
        :v_y: y velocity
    """
    ang_rad = ma.atan2(v_y, v_x)        # angle from 3 o'clock
    clock12_rad = ang_rad-ma.pi/2       # angle from 12
    clock12 = -clock12_rad/(2*ma.pi)*12 # modulo circle == 12    
    clock = round(clock12)
    if clock == 0:
        clock = 12
    elif clock < 0:
        clock = 12 + clock
    tt_talk(f"{clock} oclock")

def show_position(x, y, edge):
    """ Show ball posiion from upper left corner
        Use fraction of contact edge: 
        :x: x-coordinate
        :y: y-coordinate 
    """
    if edge in ["left", "right"]:
        y_len = y_edge_max-y_edge_min
        y_pos = (y-y_edge_min)/y_len
 
        tt_talk(f"{nolz(y_pos)}y")
    elif edge in ["top", "bottom"]:
        x_len = x_edge_max-x_edge_min
        x_pos = (x-x_edge_min)/x_len
        tt_talk(f"{nolz(x_pos)}x")
     
def nolz(nv):
    """ Suppress leading zero in fraction
    :nv: numeric value
    """
    nvstr = f"{nv:.1f}"
    ret = nvstr.lstrip("0")   
    return ret
                
def ball_update():
    """ Update ball
        Includes handeling edge collisions
    """
    if trace_level > 0:
        tt_talk("ball_update()")
    global b_x, b_y

    ball_edge_check()
    b_x += b_vx*update_loop_time
    b_y += b_vy*update_loop_time
    ball_display()

def screen_update():
    """ Update screen display
    """
    if trace_level > 0:
        tt_talk("screen_update()")
    ball_update()
    screen.update()     # In each while loop, refresh the screen with the new drawing.


"""
Run our own loop
"""
tt_talk("\nTest Start")
#trace_level = 9         # trace action
start_ball()            # Setup ball inital properties
while running:
    time.sleep(update_loop_time)
    screen_update()
