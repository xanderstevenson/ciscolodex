#!/usr/bin/python
try:
    import Tkinter as tk
    from Tkinter import *
except:
    import tkinter as tk
    from tkinter import *
from PIL import ImageTk,Image

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


class PageOne(tk.Frame):
    def __init__(self, master):

        def show_text(self, item):
            item.pack(side="top", pady=10)
            self.Text.set("")
            self.Text.pack_forget(width=0)
        # def hide_text(self, item):
        #     item.pack_forget()       


        background_image=tk.PhotoImage('\img\blue-tile.png')
        background_label = tk.Label( image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image

        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='blue')
        tk.Label(self, width=50, text="Access", fg="blue", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        var1 = StringVar()
        var1_text="I have a Cisco account with my old company that has all my Cisco certifications and \n I no longer have access to that email. How can I get the DevAsc course and exam connected to my new email?"
        var1.set(var1_text)
        
        var1b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var1b.pack()
        var1b_text="""Great question. We'll just need to merge your accounts. We'll need three things from you: \
        \n 1. The old email associated with your account \n 2. The new email your using for Cisco now \n 3. The  Profile ID \
        \n Here's how you can get your Profile ID: \
        \n Open an Incognito window in Chrome or new Private window in Firefox or Safari. Go enter your sign-on information. \
        \n Click your prof  to the DevNet site at https://developer.cisco.com \
        \n Click Login andile icon in the upper right-hand corner and choose Profile & Achievements. \
        \n Copy the profile ID, such as d47d4b96-6812-11e7-a515-02420ae9710c, which should be in the URL and on the page. \
        \n Paste your profile ID into the ticket or other communication to DevNet."""
        var1b.insert(tk.END, var1b_text) 
        # fg="black", font=('Helvetica', 12)).pack(side="top", pady=10, fill="both")
        label = Button(self, width=95, textvariable=var1, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var1b)).pack(side="top", pady=10)        


        var2 = StringVar()
        var2_text="I can't take my DevAsc exam because of COVID-19 and my course is about to expire. Can I have the course extended?"
        var2.set(var2_text)
         

        var2b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var2b.pack()
        var2b_text = """We are able to extend the course for those effected by COVID-19 but for an indeterminate \n amount of time AND once we do that, you'll lose all progress in the course."""
        var2b.insert(tk.END, var2b_text)
        label = Button(self, width=95, textvariable=var2, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var2b)).pack(side="top", pady=10) 



        var3 = StringVar()
        var3_text="How does a Cisco employee get access?"
        var3.set(var3_text)
        label = Button(self, width=45, textvariable=var3, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var3b)).pack(side="top", pady=10)        

        var3b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var3b.pack()
        var3b_text = """The DevNet Associate Fundamentals Course is not available for Cisco Employees to purchase at this time. \
        \n If you'd like to express interest in this course, you may fill out this form: \
        \n (https://app.smartsheet.com/b/form/e7fdfeb3f6074674a577ae52fffe0a34A) \
        \n If you would like to start your learning journey for the DevNet Associate Certification immediately, \
        \n we’d like to direct you to another DevNet Associate course that has been developed in partnership with Learning@Cisco. \
        \n The title of the course is 'Developing Applications and Automating Workflows using Cisco Core Platforms (DEVASC) v1.0' \
        \n and it is available today at no cost on the Cisco Digital Learning Library (CDLL). Please visit https://cxtraining.cisco.com/c/cdll_infbundle/ .\
        \n Please stay tuned for more information on the DevNet Associate Fundamentals training course employee program."""
        var3b.insert(tk.END, var3b_text)



        tk.Button(self, text="Refresh this page",
                  command=lambda: master.switch_frame(PageOne)).pack(pady=5, side = BOTTOM)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack(pady=5,side = BOTTOM)



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
        tk.Label(self, width=50, text="Content", fg="red", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
      
      
        var1 = StringVar()
        var1_text="I found an error in the course. How can I report it?"
        var1.set(var1_text)
        
        var1b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var1b.pack()
        var1b_text="""Please open a ticket here --> https://devnetsupport.cisco.com/hc/en-us/requests/new?ticket_form_id=360002862214"""
        var1b.insert(tk.END, var1b_text) 
        # fg="black", font=('Helvetica', 12)).pack(side="top", pady=10, fill="both")
        label = Button(self, width=95, textvariable=var1, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var1b)).pack(side="top", pady=10)        


        var2 = StringVar()
        var2_text="I'm having trouble with a particular lab in the DevNet Associate Fundamentals course. Can someone help me?"
        var2.set(var2_text)
         

        var2b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var2b.pack()
        var2b_text = """For any questions on content, please go to the DevNet Associate community forum here ----> https://learningnetwork.cisco.com/s/topic/0TO3i0000008jY5GAI/devnet-certifications-community"""
        var2b.insert(tk.END, var2b_text)
        label = Button(self, width=95, textvariable=var2, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var2b)).pack(side="top", pady=10) 



        var3 = StringVar()
        var3_text="How long can you complete the course, without any programming experience?"
        var3.set(var3_text)
        label = Button(self, width=85, textvariable=var3, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var3b)).pack(side="top", pady=10)        

        var3b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var3b.pack()
        var3b_text = """It varies from person to person. If you’d like to improve your coding skills before taking the course, /n we offer these free modules, plus many more: https://developer.cisco.com/startnow/#coding-apis-v0"""
        var3b.insert(tk.END, var3b_text)


        var4 = StringVar()
        var4_text="Unable to access repo-https://github.com/CiscoDevNet/devasc-code-examples.git -1"
        var4.set(var4_text)
        label = Button(self, width=85, textvariable=var4, fg="black", font=('Helvetica', 12), command=lambda: show_text(self, var4b)).pack(side="top", pady=10)        

        var4b = tk.Text(self, height=10, width=120, fg="black", font=('Helvetica', 10))
        # var3b.pack()
        var4b_text = """???"""
        var4b.insert(tk.END, var4b_text)



        tk.Button(self, text="Refresh this page",
                  command=lambda: master.switch_frame(PageTwo)).pack(pady=5, side = BOTTOM)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack(pady=5,side = BOTTOM)



class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='green')
        tk.Label(self, text="Payment", fg="green", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

class PageFour(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='black')
        tk.Label(self, text="Platform", fg="black", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

class PageFive(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='purple')
        tk.Label(self, text="Certifications", fg="purple", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

# root = tk.Tk()
# frame = Frame(root)
# frame.pack()
# # Code to add widgets will go here...

# # topframe

# topframe = Frame(root, width=100, height=50)
# topframe.pack( side = TOP)

# # topframe widgets

# accessbutton = Button(frame, text="Access", fg="red")
# accessbutton.pack( side = LEFT)

# contentbutton = Button(frame, text="Content", fg="blue")
# contentbutton.pack( side = LEFT )

# paymentbutton = Button(frame, text="Payment", fg="green")
# paymentbutton.pack( side = LEFT )

# platformbutton = Button(frame, text="Platform", fg="black")
# platformbutton.pack( side = LEFT)

# certbutton = Button(frame, text="Certification", fg="purple")
# certbutton.pack( side = LEFT)



# # Code to add widgets will go here...

# # bottomframe

# bottomframe = Frame(root, width=100, height=50)
# bottomframe.pack( side = BOTTOM )

# # bottomframe widget
# var = StringVar()
# label = Label( root, textvariable=var, relief=RAISED, fg="black", anchor="n", padx=5 )
# label.config(font=("Courier", 18, "bold"))
# var.set("Ciscolodex")
# label.pack()

# def frame_1():
#     print("frame 1!")

# root.mainloop()