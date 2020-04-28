#!/usr/bin/python

try:
    import Tkinter as tk
    from Tkinter import *
except:
    import tkinter as tk
    from tkinter import *
from PIL import ImageTk,Image

import os
import sys

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)



class PageFour(tk.Frame):
    def __init__(self, master):

        def show_text(self, item):
            item.pack(side="top", pady=10)
            self.Text.set("")
            self.Text.pack_forget(width=0)
        # def hide_text(self, item):
        #     item.pack_forget()       

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='black')
        tk.Label(self, width=50, text="Platform", fg="black", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
    
        tk.Button(self, text="Refresh this page",
                  command=lambda: master.switch_frame(PageFour)).pack(pady=5, side = TOP)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(restart_program())).pack(pady=5,side = TOP)
    
      
      
        var1 = StringVar()
        var1_text="A page/video is not loading"
        var1.set(var1_text)
        
        var1b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var1b.pack()
        var1b_text="""Please clear your cache and try again. It that doesn't work, please \n open a ticket: Contact support ---> https://devnetsupport.cisco.com/hc/en-us/requests/new?ticket_form_id=360002862214"""
        var1b.insert(tk.END, var1b_text) 
        # fg="black", font=('Helvetica', 12)).pack(side="top", pady=10, fill="both")
        label = Button(self, width=55, textvariable=var1, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var1b)).pack(side="top", pady=10)        


        var2 = StringVar()
        var2_text="Unable to type on Terminal Window"
        var2.set(var2_text)
         

        var2b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var2b.pack()
        var2b_text = """If you are using Edge Browser then it should be of version >= 79. or else try on Firefox or Chrome"""
        var2b.insert(tk.END, var2b_text)
        label = Button(self, width=55, textvariable=var2, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var2b)).pack(side="top", pady=10) 



        var3 = StringVar()
        var3_text="How can I reset a learning progress for some module?"
        var3.set(var3_text)
        label = Button(self, width=75, textvariable=var3, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var3b)).pack(side="top", pady=10)        

        var3b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var3b.pack()
        var3b_text = """Currently, it isn’t possible to reset the learning progress. We have taken it as a feature request and will look into it as a future enhancement."""
        var3b.insert(tk.END, var3b_text)


        var4 = StringVar()
        var4_text="For any technical issues with your course, including page appearance, video or lab functionality, \n or payments, please open a ticket."
        var4.set(var4_text)
        label = Button(self, width=75, textvariable=var4, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var4b)).pack(side="top", pady=10)        

        var4b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var3b.pack()
        var4b_text = """Contact support ---> https://devnetsupport.cisco.com/hc/en-us/requests/new?ticket_form_id=360002862214"""
        var4b.insert(tk.END, var4b_text)

