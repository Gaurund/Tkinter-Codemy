from tkinter import Tk
from tkinter import ttk

root = Tk()
root.title("Simple Calculator")


def button_click(number):
    # entry.delete(0, "end")
    current = entry.get()
    entry.insert("end", number)

def add():
    first_number = entry.get()
    global f_num
    f_num = int(first_number)
    clear_all()

def equal():
    second_number = entry.get()
    clear_all()
    entry.insert(0, str(f_num + int(second_number)))

def clear_all():
    entry.delete(0, "end")


entry = ttk.Entry(root, width=35)
entry.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

button_1 = ttk.Button(root, text="1", command=lambda: button_click(1))
button_2 = ttk.Button(root, text="2", command=lambda: button_click(2))
button_3 = ttk.Button(root, text="3", command=lambda: button_click(3))
button_4 = ttk.Button(root, text="4", command=lambda: button_click(4))
button_5 = ttk.Button(root, text="5", command=lambda: button_click(5))
button_6 = ttk.Button(root, text="6", command=lambda: button_click(6))
button_7 = ttk.Button(root, text="7", command=lambda: button_click(7))
button_8 = ttk.Button(root, text="8", command=lambda: button_click(8))
button_9 = ttk.Button(root, text="9", command=lambda: button_click(9))
button_0 = ttk.Button(root, text="0", command=lambda: button_click(0))
button_add = ttk.Button(root, text="+", command=add)
button_equal = ttk.Button(root, text="=", command=equal)
button_clear = ttk.Button(root, text="Clear", command=clear_all)

button_1.grid(row=3, column=0, sticky="nsew")
button_2.grid(row=3, column=1, sticky="nsew")
button_3.grid(row=3, column=2, sticky="nsew")

button_4.grid(row=2, column=0, sticky="nsew")
button_5.grid(row=2, column=1, sticky="nsew")
button_6.grid(row=2, column=2, sticky="nsew")

button_7.grid(row=1, column=0, sticky="nsew")
button_8.grid(row=1, column=1, sticky="nsew")
button_9.grid(row=1, column=2, sticky="nsew")

button_0.grid(row=4, column=0, sticky="nsew")
button_clear.grid(row=4, column=1, columnspan=2, sticky="nsew")
button_add.grid(row=5, column=0, sticky="nsew")
button_equal.grid(row=5, column=1, columnspan=2, sticky="nsew")

root.mainloop()
