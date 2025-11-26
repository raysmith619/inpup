#wx_imagess.py 08Jun2023  crs, from canvas_items.py
#canvas_items.py    23Oct2022  crs, From resource_lib_proj/
"""
wxPython examples
present images as bitmaps
Thanks to Jan Bodnar (zetcode.com) for his wxPython examples on which I've drawn

"""
import os

import wx
cv_width = cv_height = 200
x_min = y_min = int(cv_width*.1)

os.chdir(os.path.dirname(__file__))
test_image_file = "white-queen.png"

app = wx.App()
# Load from PNG image file
img = wx.Image(test_image_file, wx.BITMAP_TYPE_ANY)
bitmap = wx.Bitmap(img)         # Convert to bitmap

class CanvasFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(CanvasFrame, self).__init__(*args, **kw)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.SetTitle("wxPython images as bitmaps")
        #self.Centre()

    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(bitmap, x_min, y_min)
        

cvf = CanvasFrame(None)         # Alternative - master frame instead of master window
cvf.SetInitialSize(wx.Size(cv_width, cv_height))
cvf.Show()

app.MainLoop()


