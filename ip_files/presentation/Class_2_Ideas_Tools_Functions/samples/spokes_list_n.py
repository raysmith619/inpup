# spokes_list_n.py    13Jul2022, crs, increasing dot size
#                   25Feb2022  crs, from spokes.py
# Display a star with spokes using list


import turtle as tu    # Bring in turtle graphic functions

colors = ["red", "orange", "yellow",
          "green", "blue", "indigo",
          "violet"]

nspoke = len(colors)
ntime = 3
nspoke *= ntime   # Go through list ntime
spoke_len = 300
for color in colors*ntime:
    tu.color(color)
    tu.forward(spoke_len)
    tu.dot(spoke_len)
    tu.backward(spoke_len)
    tu.right(360/nspoke)
tu.done()
