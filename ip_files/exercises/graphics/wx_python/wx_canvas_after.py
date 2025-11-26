#wx_canvas_after.py 14Jun2025  crs, follow canvas_after.py
#                   24Oct2022  crs
"""
wxPython version of an event based display:
Two dimensional version of a traffic light
FOLLOW canvas_after.py style
"""
import wx
import math
import time
import random
import time

@staticmethod
def pt(x,y):
    """ Force int for Point
    """
    return (wx.Point(int(x),int(y)))
    
class CanvasFrame(wx.Frame):    

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.SetBackgroundColour("floral white")
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.SetTitle("wxPython Traffic Lights")
        self.color_red = "red"
        self.color_yellow = "yellow"
        self.color_green = wx.Colour(0,128,0)
        time_green = 2000           # time for green milliseconds
        time_red = 1000             # time for red
        time_yellow = int(time_red/3)
        self.states = [
            (self.color_green, time_green, self.green_light),
            (self.color_yellow, time_yellow, self.yellow_light),
            (self.color_red, time_red, self.red_light)]
        
        self.istate = len(self.states)-1    # flip to first            
        self.time_begin = time.time()
        self.prev_rect = None
        self.call_later = None
        self.Centre()
        self.Refresh()
        self.Show()
        self.next_state()   # Force next light state (in self.states)

    def time_rel(self):
        return time.time()-self.time_begin
                                
    def OnPaint(self, e):
        #print()
        self.set_sizes()
        
        state = self.states[self.istate]
        color_proc = state[2]
        print(f"{self.time_rel():.2f}: {self.istate = }: {state = }")
        color_proc()

    def next_state(self):
        """ Set duration / next update
        """
        # Advance state
        self.istate = (self.istate +1)%len(self.states)
        state = self.states[self.istate]
        duration = state[1]
        self.CallLater = wx.CallLater(duration,
                            self.next_state)
        self.Refresh()
            
    def set_sizes(self):
        # Establish sizes
        rect = self.GetClientRect()
        if self.prev_rect is not None:
            if rect != self.prev_rect:
                print(f"resize {rect =}")
        self.prev_rect = rect
                
        cv_width = rect.GetWidth()
        x_min = cv_width*.05
        x_max = cv_width*.95
        x_mid = (x_min+x_max)/2
        width = x_max-x_min
        x_max = x_min + width
        
        cv_height = rect.GetHeight() 
        y_min = cv_height*.05       # tk .1 ???
        y_max = cv_height*.95
        y_mid = (y_min+y_max)/2
        y_range = abs(y_max-y_min)

        # Add drawing area
        # Add title text
        title_text = "wxPython timing- using CallLater()"
        title_font = wx.Font(wx.FontInfo(18))
        dc = wx.PaintDC(self)
        pen = wx.Pen(wx.Colour("blue"), 2, wx.SOLID)
        dc.SetPen(pen)
        dc.SetFont(title_font)
        title_w, title_h = dc.GetTextExtent(title_text)
        th = title_h
        title_pt = pt(x_mid-title_w/2, y_min-th)
        dc.DrawText(text=title_text,  pt=title_pt)

        # Lights layout
        light_range = width
        self.light_size = min(y_range/3, width*.95)
        light_spacer = self.light_size*.05
        yt = y_min+th
        ytb = yt + self.light_size
        yt_c = (yt+ytb)/2
        self.top_light = pt(x_mid,yt_c)
        
        ym = ytb + light_spacer
        ymb = ym + self.light_size
        ym_c = int((ym+ymb)/2)
        self.middle_light = pt(x_mid,ym_c)
        
        yb = ymb + light_spacer
        ybb = yb + self.light_size
        yb_c = int((yb+ybb)/2)
        self.bottom_light = pt(x_mid,yb_c)

    def color_light(self, light_pos, color):
        """ Set lights to color
        :light_pos: light center
        :color: light color string
        """
        #print(f"color_light({light_pos}, {color})")
        dc = wx.PaintDC(self)
        dc.SetPen(wx.Pen(color, style=wx.SOLID))
        dc.SetBrush(wx.Brush(color, wx.SOLID))
        dc.DrawCircle(light_pos, int(self.light_size/2))
        
    def red_light(self):
        """ Configure lights for red light """
        self.color_light(self.top_light, self.color_red)
        self.color_light(self.middle_light, "gray")
        self.color_light(self.bottom_light, "gray")
                    
    def yellow_light(self):
        """ Configure lights for yellow light """
        self.color_light(self.top_light, "gray")
        self.color_light(self.middle_light, self.color_yellow)
        self.color_light(self.bottom_light, "gray")

    def green_light(self):
        """ Configure lights for green light """
        self.color_light(self.top_light, "gray")
        self.color_light(self.middle_light, "gray")
        self.color_light(self.bottom_light, self.color_green)


app = wx.App()
# Establish starting sizes
cv_width = 300          # canvas size
cv_height = cv_width*3
tlt = CanvasFrame(None, size=wx.Size(cv_width, cv_height))


app.MainLoop()
