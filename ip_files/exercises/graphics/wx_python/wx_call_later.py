#wx_call_later.py   19Jul2024  crs, Author
"""
Simplest of loops
Enhanced to demonstrate window Frame which, while required
for MainLoop() to work, is not required to be shown.
Just the instance of wx.Frame() needs to be created.
Comment out the f = wx.Frame line below and the
app.MainLoop() does not work as desired.
"""
import wx
app = wx.App()
f = None
print("Frame instance REQUIRED")
f = wx.Frame(None, -1, "Required Frame")
call_no = 0

lp_time_sec = 1     # Loop time in seconds

def lp1():
    global call_no
    call_no += 1
    print(f"lp1: {call_no}")
    if f is not None:
        if call_no%2 == 0:
            f.Show()
        else:
            f.Hide()
    wx.CallLater(int(lp_time_sec*1000), lp1)    # Call ourselves later

print("Direct call of lp1")
#wx.CallAfter(lp1) 
lp1()   
print("Start wx event loop")
app.MainLoop()
print("After app.MainLoop()")    