#!/usr/bin/python
try:
    import Tkinter as tk
    from Tkinter import *
except:
    import tkinter as tk
    from tkinter import *
from PIL import ImageTk,Image

class PageFive(tk.Frame):
    def __init__(self, master):

        def show_text(self, item):
            item.pack(side="top", pady=10)
            self.Text.set("")
            self.Text.pack_forget(width=0)
        # def hide_text(self, item):
        #     item.pack_forget()       

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='purple')
        tk.Label(self, width=50, text="Certifications", fg="black", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
      
        tk.Button(self, text="Refresh this page",
                  command=lambda: master.switch_frame(PageFive)).pack(pady=5, side = TOP)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack(pady=5,side = TOP)
      
        var1 = StringVar()
        var1_text="How do I claim my continuing education credits? Are there any extra requirements?"
        var1.set(var1_text)
        
        var1b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var1b.pack()
        var1b_text="""After you have completed the entire course, you will see an option to "Claim you Course Certificate" on the course website. Download the PDF version of the certificate and then pleaseease follow the process here: https://developer.cisco.com/docs/fundamentals/help/#!continuing-education-credit/continuing-education-credit

        Here are a few extra resources to help:

        https://www.cisco.com/c/dam/en_us/training-events/training-certification-faqs.pdf

        https://www.cisco.com/c/en/us/training-events/training-certifications/recertification-policy.html"""
        var1b.insert(tk.END, var1b_text) 
        # fg="black", font=('Helvetica', 12)).pack(side="top", pady=10, fill="both")
        label = Button(self, width=75, textvariable=var1, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var1b)).pack(side="top", pady=10)        


        var2 = StringVar()
        var2_text="Are there any additional resources to prepare for the DevNet Associate Exam?"
        var2.set(var2_text)
         

        var2b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var2b.pack()
        var2b_text = """On the DevNet site, there is the DevNet Associate Fundamentals Course (the best way), and the subscription applies only to that course. There are additional DevNet courses in the Cisco Platinum Learning Library: https://www.cisco.com/c/en/us/training-events/training-certifications/training/learning-library/platinum-learning-library.html You can also check out https://developer.cisco.com/certification/exam-topic-associate/ for the Topics and relevant Learning Labs."""
        var2b.insert(tk.END, var2b_text)
        label = Button(self, width=75, textvariable=var2, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var2b)).pack(side="top", pady=10) 



        var3 = StringVar()
        var3_text="How many CEs will I get for completing the course?"
        var3.set(var3_text)
        label = Button(self, width=75, textvariable=var3, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var3b)).pack(side="top", pady=10)        

        var3b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var3b.pack()
        var3b_text = """The Continuing Education Program is governed by the Cisco Continuing Education Advisory Board. The Cisco Continuing Education Advisory Board has approved DevNet Associate Fundamentals course for earning 48 Continuing Education credits."""
        var3b.insert(tk.END, var3b_text)


        var4 = StringVar()
        var4_text="Will passing the DevNet Associate exam renew my CCNP / CCNA / etc.?"
        var4.set(var4_text)
        label = Button(self, width=75, textvariable=var4, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var4b)).pack(side="top", pady=10)        

        var4b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var3b.pack()
        var4b_text = """It unfortunately won’t due to 200-901 being at the associate level and not the professional level. (It will renew all associate level exams you hold) Take a look at the recertification requirements here: https://www.cisco.com/c/en/us/training-events/training-certifications/recertification-policy.html#~requirements"""
        var4b.insert(tk.END, var4b_text)
