from tkinter import Tk
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to Code at Codemy.com")
root.iconbitmap("tk.ico")

my_img = ImageTk.PhotoImage(Image.open("D:/DOCS/PICS/2015-04-11/Сканировать1.JPG"))
my_label = ttk.Label(root, image=my_img)
my_label.grid()

button_quit = ttk.Button(root, text="Exit", command=root.quit)
button_quit.grid()

root.mainloop()