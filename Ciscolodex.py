#!/usr/bin/python
try:
    import Tkinter as tk
    from Tkinter import *
except:
    import tkinter as tk
    from tkinter import *


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
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='blue')
        tk.Label(self, width=50, text="Access", fg="blue", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        
        var1 = StringVar()
        var1.set("I have a Cisco account with my old company that has all my Cisco certifications and \n I no longer have access to that email. How can I get the DevAsc course and exam connected to my new email?")
        tk.Label(self, width=95, textvariable=var1, fg="black", font=('Helvetica', 12)).pack(side="top", pady=10)
        
        var1b = tk.Text(self, height=10, width=100, fg="black", font=('Helvetica', 10))
        var1b.pack()

        quote="""Great question. We'll just need to merge your accounts. We'll need three things from you: \
        \n 1. The old email associated with your account \n 2. The new email your using for Cisco now \n 3. The  Profile ID \
        \n Here's how you can get your Profile ID: \
        \n Open an Incognito window in Chrome or new Private window in Firefox or Safari. Go enter your sign-on information. \
        \n Click your prof  to the DevNet site at https://developer.cisco.com \
        \n Click Login andile icon in the upper right-hand corner and choose Profile & Achievements. \
        \n Copy the profile ID, such as d47d4b96-6812-11e7-a515-02420ae9710c, which should be in the URL and on the page. \
        \n Paste your profile ID into the ticket or other communication to DevNet."""
        var1b.insert(tk.END, quote) 
        # fg="black", font=('Helvetica', 12)).pack(side="top", pady=10, fill="both")
                
        var2 = StringVar()
        var2.set("How does a Cisco employee get access?")
        tk.Label(self, width=55, textvariable=var2, fg="black", font=('Helvetica', 12)).pack(side="top", pady=10)        

        var2b = tk.Text(self, height=10, width=100, fg="black", font=('Helvetica', 10))
        var2b.pack()
        quote2 = """The DevNet Associate Fundamentals Course is not available for Cisco Employees to purchase at this time. \
        \n If you'd like to express interest in this course, you may fill out this form: \
        \n (https://app.smartsheet.com/b/form/e7fdfeb3f6074674a577ae52fffe0a34A) \
        \n If you would like to start your learning journey for the DevNet Associate Certification immediately, \
        \n we’d like to direct you to another DevNet Associate course that has been developed in partnership with Learning@Cisco. \
        \n The title of the course is 'Developing Applications and Automating Workflows using Cisco Core Platforms (DEVASC) v1.0' \
        \n and it is available today at no cost on the Cisco Digital Learning Library (CDLL). Please visit https://cxtraining.cisco.com/c/cdll_infbundle/ .\
        \n Please stay tuned for more information on the DevNet Associate Fundamentals training course employee program."""
        var2b.insert(tk.END, quote2)

        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack(pady=10)

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="Content", fg="red", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

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