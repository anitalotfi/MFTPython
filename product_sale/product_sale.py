import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from validator import *

product_list = []

def sell_click():
    if(validator(model.get())):
        product = (
            brand.get(),
            model.get(),
            color.get(),
            option_glass.get(),
            option_memory.get()
        )
        print(product)
        product_list.append(product)
        msg.showinfo("Product Sold", "Product " + str(product) + " has been sold successfully")
        reset_form()
        color.set("")
        model.set("")
        brand.set("")
        option_glass.set(False)
        option_memory.set(False)
    else:
        msg.showerror("Error", "Please enter a valid data")


def reset_form():
    for item in table.get_children():
        table.delete(item)

        for product in product_list:
            table.insert("", values=product)

def selected(event):
    select_option = (brand.get())
    print("You selected :", select_option)

def color_selected(event):
    selected_option = (color.get())
    print("You selected :", selected_option)

win = tkinter.Tk()
win.title("Product Sale")
win.geometry("650x300")
win.resizable(False, False)


ttk.Label(win, text="Brand :",
          font = ("Times New Roman", 10)).place(x=20, y=20)
brand = ttk.Combobox(win,
             values=["Apple", "Samsung", "Nokia"],
             width= 20,
             state="readonly"
             )
brand.place(x=80, y=20)
brand.bind("<<ComboboxSelected>>", selected)

ttk.Label(win, text="Model").place(x=20, y=60)
model = tkinter.StringVar()
ttk.Entry(win, textvariable=model,).place(x=80, y=60)

ttk.Label(win, text="Color",
          font = ("Times New Roman", 10)).place(x=20, y=100)
color = ttk.Combobox(win,
             values=["White", "Black", "Red", "Blue"],
             width= 20,
             state="readonly"
             )
color.place(x=80, y=100)
color.bind("<<ComboboxSelected>>", color_selected)

ttk.Label(win, text="Option").place(x=20, y=140)
option_glass = tkinter.BooleanVar()
ttk.Checkbutton(win, text="Glass", variable=option_glass).place(x=80, y=140)

option_memory = tkinter.BooleanVar()
ttk.Checkbutton(win, text="Memory", variable=option_memory).place(x=80, y=180)


table = ttk.Treeview(win, columns=(1, 2, 3, 4), height=12, show="headings")
table.heading(1, text="Brand")
table.heading(2, text="Model")
table.heading(3, text="Color")
table.heading(4, text="Option")

table.column(1, width=100)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)

table.place(x=230, y=20)

reset_form()

ttk.Button(win, text="Sell", width=10, command=sell_click).place(x=70, y=240)

win.mainloop()