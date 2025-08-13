from tkinter import *
from tkinter import ttk

root = Tk()

def myClick():
    myLabel = ttk.Label(root, text="Look! I clicked a Button!!")
    myLabel.grid(column=0,row=1)

myButton = ttk.Button(root, text="My Text", padding="10", command=myClick).grid(column=0, row=0)

root.mainloop()