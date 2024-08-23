import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as msg

def add_click():

def selected(event):
    select_option = (inv.get())
    print("You selected :", select_option)

win = tkinter.Tk()
win.title("Inventory")
win.geometry("650x300")
win.resizable(False, False)

ttk.Label(win, text="Product: ").place(x=20, y=20)
product = tkinter.StringVar()
ttk.Entry(win, textvariable=product).place(x=90, y=20)

ttk.Label(win, text="Price: ").place(x=20, y=60)
price = tkinter.StringVar()
ttk.Entry(win, textvariable=price).place(x=90, y=60)

ttk.Label(win, text="Count: ").place(x=20, y=100)
count = tkinter.StringVar()
ttk.Entry(win, textvariable=count).place(x=90, y=100)

ttk.Label(win, text="Person: ").place(x=20, y=140)
person = tkinter.StringVar()
ttk.Entry(win, textvariable=person).place(x=90, y=140)

ttk.Label(win, text="Inventory: ",
          font=("Times New Roman", 10)).place(x=20, y=180)
inv = ttk.Combobox(win,
                   values=["Income", "Outcome"],
                   width=17,
                   state="readonly"
                   )
inv.place(x=90, y=180)
inv.bind("<<ComboboxSelected>>", selected)

table = ttk.Treeview(win, columns=(1, 2, 3, 4), height=12, show="headings")
table.heading(1, text="Product")
table.heading(2, text="Price")
table.heading(3, text="Count")
table.heading(4, text="Person")

table.column(1, width=100)
table.column(2, width=80)
table.column(3, width=50)
table.column(4, width=100)

table.place(x=230, y=20)


# ttk.Button(win, text="Sell", width=10, command=sell_click).place(x=70, y=240)

win.mainloop()