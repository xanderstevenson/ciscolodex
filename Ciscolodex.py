#!/usr/bin/python
try:
    import Tkinter as tk
    from Tkinter import *
except:
    import tkinter as tk
    from tkinter import *
from PIL import ImageTk,Image
import Page_One, Page_Two, Page_Three, Page_Four, Page_Five
import sys
import os

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None

        self.switch_frame(StartPage)


    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(anchor='w')

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Ciscolodex", relief=RAISED, font=('Helvetica', 28, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Access",
                  command=lambda: master.switch_frame(PageOne)).pack(side = LEFT)
        tk.Button(self, text="Content",
                  command=lambda: master.switch_frame(PageTwo)).pack(side = LEFT)
        tk.Button(self, text="Payment",
                  command=lambda: master.switch_frame(PageThree)).pack(side = LEFT)
        tk.Button(self, text="Platform",
                  command=lambda: master.switch_frame(PageFour)).pack(side = LEFT)
        tk.Button(self, text="Certifications",
                  command=lambda: master.switch_frame(PageFive)).pack(side = LEFT)

class PageOne(Page_One.PageOne):
    pass

class PageTwo(Page_Two.PageTwo):
    pass

class PageThree(Page_Three.PageThree):
    pass

class PageFour(Page_Four.PageFour):
    pass

class PageFive(Page_Five.PageFive):
    pass

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
