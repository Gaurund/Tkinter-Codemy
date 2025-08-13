from tkinter import Tk
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to Code at Codemy.com")
root.iconbitmap("tk.ico")

files_list = [
    "images/9.jpg",
    # "images/304762-003.jpg",
    "images/13.jpg",
    "images/15.jpg",
    "images/25.jpg",
    "images/34.jpg",
    "images/44.jpg",
    "images/46.jpg",
    "images/61.jpg",
    "images/68.jpg",
]

image_list = [ImageTk.PhotoImage(Image.open(f)) for f in files_list]

image_number = 0

status = ttk.Label(
    root, text=f"Image 1 of {len(image_list)} ", relief="sunken", anchor="e"
)

my_label = ttk.Label(root, image=image_list[0])
my_label.grid(column=0, row=0, columnspan=3)


def step(step) -> None:
    global image_number
    image_number = eval(f"{image_number}{step}")
    if image_number == 0:
        button_back["state"] = "disabled"
    elif image_number == len(image_list) - 1:
        button_forward["state"] = "disabled"
    else:
        button_forward["state"] = "!disabled"
        button_back["state"] = "!disabled"
    my_label["image"] = image_list[image_number]
    status["text"] = f"Image {image_number + 1} of {len(image_list)} "


button_back = ttk.Button(root, text="<<", state="disabled", command=lambda: step("-1"))
button_exit = ttk.Button(root, text="Quit", command=root.quit)
button_forward = ttk.Button(root, text=">>", command=lambda: step("+1"))

button_back.grid(column=0, row=1)
button_exit.grid(column=1, row=1, pady=10)
button_forward.grid(column=2, row=1)

status.grid(column=0, row=2, columnspan=3, sticky="ew", ipadx=3, ipady=3)

root.mainloop()
