import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from validator import *

product_list = []

def sell_click():
    if(validator(model.get())):
        product = {
            "brand": brand.get(),
            "model": model.get(),
            "color": color.get(),
            "option": {
                "glass": option_glass.get(),
                "memory": option_memory.get()
            }
        }
        # save to database
        product_list.append(product)
        msg.showinfo("Save", f"Product {product} Saved")
        reset_form()
    else:
        msg.showerror("Error", "Please enter a valid data")


def reset_form():
    color.set("")
    model.set("")
    brand.set("")
    option_glass.set(False)
    option_memory.set(False)

win = tkinter.Tk()
win.title("Product Sale")
win.geometry("270x300")
win.resizable(False, False)


tkinter.Label(win, text="Brand").place(x=20, y=20)
brand = tkinter.StringVar()
ttk.Combobox(win,
             textvariable=brand,
             values=["Apple", "Samsung", "Nokia"],
             state="readonly"
             ).place(x=80, y=20)

tkinter.Label(win, text="Model").place(x=20, y=60)
model = tkinter.StringVar()
tkinter.Entry(win, textvariable=model,width=23).place(x=80, y=60)

tkinter.Label(win, text="Color").place(x=20, y=100)
color = tkinter.StringVar()
ttk.Combobox(win,
             textvariable=color,
             values=["White", "Black", "Red", "Blue"],
             state="readonly"
             ).place(x=80, y=100)

tkinter.Label(win, text="Option").place(x=20, y=140)
option_glass = tkinter.BooleanVar()
tkinter.Checkbutton(win, text="Glass", variable=option_glass).place(x=80, y=140)

option_memory = tkinter.BooleanVar()
tkinter.Checkbutton(win, text="Memory", variable=option_memory).place(x=80, y=180)



tkinter.Button(win, text="Sell", width=10, command=sell_click).place(x=90, y=250)

win.mainloop()