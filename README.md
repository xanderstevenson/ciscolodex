# Ciscolodex
A tool for Cisco DevNet CX and CIN

Purpose: 
--------
a quick offline tool to provide basic answers to customer inquiries regarding DevNet, specifically the DevNet Associate Fundamentals Course.

Design:
------- 
This tool is made with Python 3.8.1 and Tkinter. We've used Class based programming with a seperate module for each 'Page' of the app. The pages are 5 in number with each representing a category. The main file, Ciscolodex.py, imports the 5 modules and coordinates the display based on user input

Execution:
---------
In the /dist folder, you'll find a Ciscolodex.exe file which can be downloaded and run on a Windows computer. This standalone executable was created with PyInstaller using the following command: pyinstaller Ciscolodex.py -w -F

Future Considerations:
----------------------
- A Mac verson can be compiled if there is a demand for it
- The current version should run on a Windows computer. If not, try:
    - install Python
    - install TKinter: 
        https://tkdocs.com/tutorial/install.html
        https://www.activestate.com/products/tcl/downloads/
    - Contact Alex @ alexstev@cisco.com



by Alex Stevenson and Geev Cheria
