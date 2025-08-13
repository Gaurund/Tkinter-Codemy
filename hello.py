from tkinter import *
from tkinter import ttk

root = Tk()

entry = ttk.Entry(root, width=50)
entry.grid(column=0, row=0)
entry.insert(0, "Enter your name...")

def myClick():
    hello = "Hello " + entry.get().capitalize()
    myLabel = ttk.Label(root, text=hello)
    myLabel.grid(column=0,row=2)

myButton = ttk.Button(root, text="Enter Your Name", padding="10", command=myClick)
myButton.grid(column=0, row=1)

root.mainloop()