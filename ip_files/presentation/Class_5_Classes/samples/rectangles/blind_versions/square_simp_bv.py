#square_simp_bv.py  16Aug2024  crs, from square_simp.py
#                   10Apr2022  crs, from square.py
"""
Blind version - simplified for viewing
Simple visual example of object
Show inheritance
"""
from rectangle_simp import Rectangle

class Square(Rectangle):
    def __init__(self, side=100, **kwargs):
        self.side = side
        kwargs['width'] = kwargs['height'] = side
        super().__init__(**kwargs)


if __name__ == '__main__':
    from random import randint
    import wx_turtle_braille as tu
    
    tu.speed('fastest')     # speedup
    colors = ["red", "orange", "yellow",
              "green", "blue", "indigo",
              "violet"]
    nrec = 3
    size = 500
    x_beg = y_beg = -int(size/2)
    x_end = y_end = int(size/2)
    inc = int(size/nrec)
    x = x_beg
    y = y_beg
    for i in range(nrec):
        side = randint(inc,x_end-x)
        edge = i+1
        color = colors[i%len(colors)]
        fill = i % 2
        rec = Square(x=x, y=y, side=side,
                        color=color,fill=fill)
        x += inc
        y += inc
    tu.mainloop()