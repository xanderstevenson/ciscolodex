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
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=200, height=100,)
        tk.Label(self, text="Ciscolodex", relief=RAISED, font=('Helvetica', 28, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Access",
                  command=lambda: master.switch_frame(PageOne)).pack(side = LEFT)
        tk.Button(self, text="Content",
                  command=lambda: master.switch_frame(PageTwo)).pack(side = LEFT)
        tk.Button(self, text="Payment",
                  command=lambda: master.switch_frame(PageThree)).pack(side = LEFT)
        tk.Button(self, text="Platform",
                  command=lambda: master.switch_frame(PageFour)).pack(side = LEFT)


class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self, text="Access", fg="blue",font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

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