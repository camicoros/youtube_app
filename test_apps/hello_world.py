"""
Hello world application for Tkinter
This program just says hello
author: D.D. Saushkin
"""
import tkinter as tk


# creating root window
root = tk.Tk()
# creating label
label = tk.Label(root, text="Hello world")
# place it on the GUI
label.pack()

# start application event loop
root.mainloop()
