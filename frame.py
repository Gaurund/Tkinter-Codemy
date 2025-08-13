from tkinter import Tk, ttk
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to Code at Codemy.com")
root.iconbitmap("tk.ico")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = ttk.Labelframe(root, text="This is my frame...", padding=50)
frame.grid(padx=50, pady=50, sticky="nsew")
frame.columnconfigure(0, weight=1)
button = ttk.Button(frame, text="Don't click here!").grid()



root.mainloop()