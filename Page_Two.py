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


class PageTwo(tk.Frame):
    def __init__(self, master):

        def show_text(self, item):
            item.pack(side="top", pady=10)
            self.Text.set("")
            self.Text.pack_forget(width=0)
        # def hide_text(self, item):
        #     item.pack_forget()       

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='red')
        tk.Label(self, width=50, text="Content", fg="black", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)

        tk.Button(self, text="Refresh this page",
                  command=lambda: master.switch_frame(PageTwo)).pack(pady=5, side = TOP)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(restart_program())).pack(pady=5,side = TOP)      
      
        var1 = StringVar()
        var1_text="I found an error in the course. How can I report it?"
        var1.set(var1_text)
        
        var1b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var1b.pack()
        var1b_text="""Please open a ticket here --> https://devnetsupport.cisco.com/hc/en-us/requests/new?ticket_form_id=360002862214"""
        var1b.insert(tk.END, var1b_text) 
        # fg="black", font=('Helvetica', 12)).pack(side="top", pady=10, fill="both")
        label = Button(self, width=55, textvariable=var1, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var1b)).pack(side="top", pady=10)        


        var2 = StringVar()
        var2_text="I'm having trouble with a particular lab in the DevNet Associate Fundamentals course. Can someone help me?"
        var2.set(var2_text)
         

        var2b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var2b.pack()
        var2b_text = """For any questions on content, please go to the DevNet Associate community forum here ----> https://learningnetwork.cisco.com/s/topic/0TO3i0000008jY5GAI/devnet-certifications-community"""
        var2b.insert(tk.END, var2b_text)
        label = Button(self, width=85, textvariable=var2, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var2b)).pack(side="top", pady=10) 



        var3 = StringVar()
        var3_text="How long can you complete the course, without any programming experience?"
        var3.set(var3_text)
        label = Button(self, width=70, textvariable=var3, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var3b)).pack(side="top", pady=10)        

        var3b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var3b.pack()
        var3b_text = """It varies from person to person. If you’d like to improve your coding skills before taking the course, /n we offer these free modules, plus many more: https://developer.cisco.com/startnow/#coding-apis-v0"""
        var3b.insert(tk.END, var3b_text)


        var4 = StringVar()
        var4_text="Unable to access repo-https://github.com/CiscoDevNet/devasc-code-examples.git -1"
        var4.set(var4_text)
        label = Button(self, width=75, textvariable=var4, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var4b)).pack(side="top", pady=10)        

        var4b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var3b.pack()
        var4b_text = """???"""
        var4b.insert(tk.END, var4b_text)

