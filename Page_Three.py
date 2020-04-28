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
            self.Text.set("")
            self.Text.pack_forget(width=0)
        # def hide_text(self, item):
        #     item.pack_forget()       

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='green')
        tk.Label(self, width=50, text="Payment", fg="black", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
      

        tk.Button(self, text="Refresh this page",
                  command=lambda: master.switch_frame(PageThree)).pack(pady=5, side = TOP)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(restart_program())).pack(pady=5,side = TOP)
              
        var1 = StringVar()
        var1_text="Can I get a refund?"
        var1.set(var1_text)
        
        var1b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var1b.pack()
        var1b_text="""Sorry, but refunds are not available."""
        var1b.insert(tk.END, var1b_text) 
        # fg="black", font=('Helvetica', 12)).pack(side="top", pady=10, fill="both")
        label = Button(self, width=45, textvariable=var1, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var1b)).pack(side="top", pady=10)        


        var2 = StringVar()
        var2_text="Can I use Cisco Learning Credits for this course?"
        var2.set(var2_text)
         

        var2b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var2b.pack()
        var2b_text = """Yes, you can! 

Please follow the steps below to buy the course using Cisco Learning Credits.

1) When you click to buy the course under the option select your payment method you will see Pay by CLC option.

2) You need to input the sales order number which should have sufficient Cisco learning credit.

3) Click Submit a request, a dialog would popup with a button "View Order"

4) Click View Order, then you will see 2 status
        • Before the order gets approved, it would show Pending for Review
        • After the order gets approved, it would show Completed

5) Along this you will also receive an email notification once the order gets approved.

Note:

Coupon is not supported with paying by Cisco Learning Credit.
If you already got a pending request then will not be able to submit a second request. (Place order failed)"""
        var2b.insert(tk.END, var2b_text)
        label = Button(self, width=55, textvariable=var2, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var2b)).pack(side="top", pady=10) 



        var3 = StringVar()
        var3_text="My company wants to pay for the 6-MONTH PLAN course, but they need to have billing \n or purchasing orders. Is it possible for Cisco to provide this?"
        var3.set(var3_text)
        label = Button(self, width=80, textvariable=var3, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var3b)).pack(side="top", pady=10)        

        var3b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var3b.pack()
        var3b_text = """Thanks for the inquiry. We provide a receipt, which will be provided at the time of purchase. No invoice is available. This has been discussed by the powers that be and it seems they're not making any exceptions. That being said, there is another DevAsc course available.

You'll have to either log-in or sign up to view ---> https://digital-learning.cisco.com/#/course/61907"""
        var3b.insert(tk.END, var3b_text)


        var4 = StringVar()
        var4_text="I wanted to know if Cisco would Automatimatically renew the subscription (which I do not want) \n or it would be a manual renewal process (if i desire). As subscription charges have been increased  \n and i do not want to renew the subscription automatically."
        var4.set(var4_text)
        label = Button(self, width=85, textvariable=var4, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var4b)).pack(side="top", pady=10)        

        var4b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var3b.pack()
        var4b_text = """A: Good question. Good news: you will NOT be charged again. Once your purchased plan period has expired, the charges and the access to the course are discontinued. In order to obtain access again, a new enrollment or a renewal plan will be required. So, as long as you don't purchase a renewal plan, which it appears you did not, when the subscription is over, after one month in your case, you will not be charged.

You can read the course FAQs"""
        var4b.insert(tk.END, var4b_text)