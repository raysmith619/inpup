#wx_item_scale.py 09Apr2025  crs, Using DrawBitmap
"""
wxPython examples
present images as bitmaps, using 
Thanks to Jan Bodnar (zetcode.com) for his wxPython examples on which I've drawn

"""
import os

import wx
cv_width = cv_height = 200
x_min = y_min = int(cv_width*.1)



app = wx.App()


class CanvasFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(CanvasFrame, self).__init__(*args, **kw)
        self.Bind(wx.EVT_SIZE, self.OnResize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.SetTitle("wxPython images as bitmaps")
        #self.Centre()
        self.chg_min = 10       # Only change if dimentions change by this
        self.width = cv_width
        self.height = cv_height
        
    @staticmethod
    def scale_bitmap(bitmap, width, height):    # From Stackoverflow
        image = bitmap.ConvertToImage()
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.Bitmap(image)
        return result

    def OnResize(self, e):
        width,height = self.GetClientSize()
        chg = max(abs(self.width-width),abs(self.height-height))
        self.chg_min = 0
        if (chg > self.chg_min):
            self.width = width
            self.height = height
            self.Refresh()
        

    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        dc.DrawRectangle(x_min, y_min, self.width-x_min*2, self.height-y_min*2)

cvf = CanvasFrame(None)         # Alternative - master frame instead of master window
cvf.SetInitialSize(wx.Size(cv_width, cv_height))
cvf.Show()

app.MainLoop()


