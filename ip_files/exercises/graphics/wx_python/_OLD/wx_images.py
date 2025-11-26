#wx_imagess.py 08Jun2023  crs, from canvas_items.py
#canvas_items.py    23Oct2022  crs, From resource_lib_proj/
"""
wxPython examples
present images as bitmaps
Thanks to Jan Bodnar (zetcode.com) for his wxPython examples on which I've drawn

"""
import os

import wx
cv_width = 300
cv_height = cv_width*2
x_min = int(cv_width*.1)
x_max = int(cv_width*.9)
pat_width = x_max-x_min
x_mid = int((x_min+x_max)/2)

y_min = int(cv_height*.1)
y_max = int(cv_height*.9)
y_mid = int((y_min+y_max)/2)
pat_height = y_max-y_min
os.chdir(os.path.dirname(__file__))
test_image_file = "white-queen.png"
test_file_path = os.path.abspath(os.path.join(".", test_image_file))
print(f"{test_file_path =}")

app = wx.App()
# Load the image
wx.Image.AddHandler(wx.PNGHandler())
img = wx.Image(test_file_path, wx.BITMAP_TYPE_ANY)
# Convert to bitmap
bitmap = wx.Bitmap(img)

class CanvasFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(CanvasFrame, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.SetTitle("wxPython images as bitmaps")
        self.Centre()

    def OnPaint(self, e):

        dc = wx.PaintDC(self)

        dc = wx.PaintDC(self)
        dc.DrawBitmap(bitmap, x_min, y_min)
        



cvf = CanvasFrame(None)         # Alternative - master frame instead of master window
cvf.SetInitialSize(wx.Size(cv_width, cv_height))
cvf.Show()

app.MainLoop()


