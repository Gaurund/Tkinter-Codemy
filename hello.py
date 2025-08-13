from tkinter import *
from tkinter import ttk

root = Tk()

entry = ttk.Entry(root, width=50)
entry.grid(column=0, row=0)

def myClick():
    myLabel = ttk.Label(root, text="Look! I clicked a Button!!")
    myLabel.grid(column=0,row=3)

myButton = ttk.Button(root, text="My Text", padding="10", command=myClick).grid(column=0, row=1)

root.mainloop()