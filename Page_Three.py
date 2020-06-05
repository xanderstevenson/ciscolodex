#!/usr/bin/python

try:
    import Tkinter as tk
    from Tkinter import *
except:
    import tkinter as tk
    from tkinter import *
from PIL import ImageTk,Image

import sys
import os

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

class PageThree(tk.Frame):
    def __init__(self, master):

        def show_text(self, item):
            item.pack(side="top", pady=10)
            # self.Text.set("")
            list = [var1b, var2b, var3b, var4b]
            index = list.index(item)

            del list[index]


            for it in list:
                it.pack_forget()      

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='#a1ad9a')
        tk.Label(self, width=50, text="Payment", fg="black", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
      

        tk.Button(self, text="Refresh this page",
                  command=lambda: master.switch_frame(PageThree)).pack(pady=5, side = TOP)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(restart_program())).pack(pady=5,side = TOP)
              
        var1 = StringVar()
        var1_text="Question 1"
        var1.set(var1_text)
        
        var1b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var1b.pack()
        var1b_text="Answer 1"
        var1b.insert(tk.END, var1b_text) 
        # fg="black", font=('Helvetica', 12)).pack(side="top", pady=10, fill="both")
        label = Button(self, width=45, textvariable=var1, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var1b)).pack(side="top", pady=10)        


        var2 = StringVar()
        var2_text="Question 2"
        var2.set(var2_text)
         

        var2b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var2b.pack()
        var2b_text = "Answer 2"
        var2b.insert(tk.END, var2b_text)
        label = Button(self, width=55, textvariable=var2, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var2b)).pack(side="top", pady=10) 



        var3 = StringVar()
        var3_text="Question 3"
        var3.set(var3_text)
        label = Button(self, width=80, textvariable=var3, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var3b)).pack(side="top", pady=10)        

        var3b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var3b.pack()
        var3b_text = "Answer 3"
        var3b.insert(tk.END, var3b_text)


        var4 = StringVar()
        var4_text="Question 4"
        var4.set(var4_text)
        label = Button(self, width=85, textvariable=var4, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var4b)).pack(side="top", pady=10)        

        var4b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var3b.pack()
        var4b_text = "Answer 4"
        var4b.insert(tk.END, var4b_text)