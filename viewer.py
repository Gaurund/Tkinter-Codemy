from tkinter import Tk
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to Code at Codemy.com")
root.iconbitmap("tk.ico")

my_img1 = ImageTk.PhotoImage(Image.open("images/9.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/13.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/15.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/25.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/44.jpg"))


image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = ttk.Label(image=my_img1)
my_label.grid(column=0, row=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = ttk.Label(image=image_list[image_number])
    button_forward = ttk.Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = ttk.Button(root, text="<<", command=lambda: back(image_number-1))
    if image_number == 4:
        button_forward = ttk.Button(root, text=">>", state="disabled")
    my_label.grid(column=0, row=0, columnspan=3)
    button_back.grid(column=0, row=1)
    button_forward.grid(column=2, row=1)

def back(image_number=0):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = ttk.Label(image=image_list[image_number])
    button_forward = ttk.Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = ttk.Button(root, text="<<", command=lambda: back(image_number-1))
    if image_number == 0:
        button_back = ttk.Button(root, text="<<", state="disabled")
    my_label.grid(column=0, row=0, columnspan=3)
    button_back.grid(column=0, row=1)
    button_forward.grid(column=2, row=1)

button_back = ttk.Button(root, text="<<", command=lambda: back())
button_exit = ttk.Button(root, text="Quit", command=root.quit)
button_forward = ttk.Button(root, text=">>", command=lambda: forward(1))

button_back.grid(column=0, row=1)
button_exit.grid(column=1, row=1)
button_forward.grid(column=2, row=1)


root.mainloop()
