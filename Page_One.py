#!/usr/bin/python

try:
    import Tkinter as tk
    from Tkinter import *
except:
    import tkinter as tk
    from tkinter import *
from PIL import ImageTk,Image
# from Ciscolodex import StartPage


class PageOne(tk.Frame):
    def __init__(self, master):

        def show_text(self, item):
            item.pack(side="top", pady=10)
            # self.Text.set("")
            # self.Text.pack_forget(width=0)

        # def hide_text(self, item):
        #     item.pack_forget()       
       
        tk.Frame.__init__(self, master)    
        tk.Frame.configure(self, bg='blue')
        tk.Label(self, width=50, text="Access", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        
        tk.Button(self, text="Refresh this page",
                  command=lambda: master.switch_frame(PageOne)).pack(pady=5, side = TOP)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack(pady=5,side = TOP)        
        
        
        var1 = StringVar()
        var1_text="I have a Cisco account with my old company that has all my Cisco certifications and \n I no longer have access to that email. How can I get the DevAsc course and exam connected to my new email?"
        var1.set(var1_text)
        
        var1b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var1b.pack()
        var1b_text="""Great question. We'll just need to merge your accounts. We'll need three things from you: \
        \n 1. The old email associated with your account \n 2. The new email your using for Cisco now \n 3. The  Profile ID \
        \n Here's how you can get your Profile ID: \
        \n - Open an Incognito window in Chrome or new Private window in Firefox or Safari. Go enter your sign-on information. \
        \n - Click your prof  to the DevNet site at https://developer.cisco.com \
        \n - Click Login andile icon in the upper right-hand corner and choose Profile & Achievements. \
        \n - Copy the profile ID, such as d47d4b96-6812-11e7-a515-02420ae9710c, which should be in the URL and on the page. \
        \n - Paste your profile ID into the ticket or other communication to DevNet."""
        var1b.insert(tk.END, var1b_text) 
        # fg="black", font=('Helvetica', 12)).pack(side="top", pady=10, fill="both")
        label = Button(self, width=85, textvariable=var1, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var1b)).pack(side="top", pady=10)        


        var2 = StringVar()
        var2_text="I can't take my DevAsc exam because of COVID-19 and my course is about to expire. Can I have the course extended?"
        var2.set(var2_text)
         

        var2b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var2b.pack()
        var2b_text = """We understand and are able to extend the course for those effected by COVID-19 but for an indeterminate \n amount of time AND once we do that, you'll lose all progress in the course. \n
        Please open a ticket here ---> https://devnetsupport.cisco.com/hc/en-us/requests/new?ticket_form_id=360002862214  \n
        Inside the ticket, please provide:
        1. email used to register
        2. You CCO ID
        3. A screen shot of your receipt
        4. The Profile ID \
        \n Here's how you can get your Profile ID: \
        \n - Open an Incognito window in Chrome or new Private window in Firefox or Safari. Go enter your sign-on information. \
        \n - Click your prof  to the DevNet site at https://developer.cisco.com \
        \n - Click Login andile icon in the upper right-hand corner and choose Profile & Achievements. \
        \n - Copy the profile ID, such as d47d4b96-6812-11e7-a515-02420ae9710c, which should be in the URL and on the page. \
        \n - Paste your profile ID into the ticket or other communication to DevNet."""
        
        var2b.insert(tk.END, var2b_text)
        label = Button(self, width=95, textvariable=var2, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var2b)).pack(side="top", pady=10) 



        var3 = StringVar()
        var3_text="How does a Cisco employee get access?"
        var3.set(var3_text)
        label = Button(self, width=45, textvariable=var3, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var3b)).pack(side="top", pady=10)        

        var3b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var3b.pack()
        var3b_text = """The DevNet Associate Fundamentals Course is not available for Cisco Employees to purchase at this time. \
        \n * If you'd like to express interest in this course, please fill out this form: (https://app.smartsheet.com/b/form/e7fdfeb3f6074674a577ae52fffe0a34A) \
        \n * If you would like to start your learning journey for the DevNet Associate Certification immediately, \
        \n we’d like to direct you to another DevNet Associate course that has been developed in partnership with Learning@Cisco. \
        \n\n The title of the course is 'Developing Applications and Automating Workflows using Cisco Core Platforms (DEVASC) v1.0' \
        \n and it is available today at no cost on the Cisco Digital Learning Library (CDLL). Please visit https://cxtraining.cisco.com/c/cdll_infbundle/ .\
        \n Please stay tuned for more information on the DevNet Associate Fundamentals training course employee program."""
        var3b.insert(tk.END, var3b_text)



        var4 = StringVar()
        var4_text="I have a question about subscription period. I want to pay for the course today, \n but start to learn it in next month, for example. So, from what date will be calculated subscription period?"
        var4.set(var4_text)
        label = Button(self, width=85, textvariable=var4, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var4b)).pack(side="top", pady=10)        

        var4b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var3b.pack()
        var4b_text = """The subscription period starts on the date of your purchase , you will NOT be able to access the course if your purchased plan has expired. In order to obtain access again, a new enrollment or a renewal plan will be required. """
        var4b.insert(tk.END, var4b_text)