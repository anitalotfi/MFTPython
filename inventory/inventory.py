import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as msg

product_list = []

def add_click():
    product_name = product.get()
    product_price = price.get()
    product_count = int(count.get())
    transaction_type = inv.get()
    person_name = person.get()

    # Check if the product already exists in the list
    found = False
    for item in product_list:
        if item[0] == product_name:
            found = True
            if transaction_type == "Income":
                item[2] += product_count
                color = "green"
            elif transaction_type == "Outcome":
                if item[2] >= product_count:
                    item[2] -= product_count
                    color = "red"
                else:
                    msg.showerror("Error", "Not enough product in stock for this outcome.")
                    return

            # Update the row in the table
            for row in table.get_children():
                row_data = table.item(row)["values"]
                if row_data[0] == product_name:
                    table.item(row, values=(product_name, product_price, item[2], person_name), tags=('colored_row',))
                    table.tag_configure('colored_row', background=color)
                    break
            break

    if not found:
        if transaction_type == "Income":
            product_list.append([product_name, product_price, product_count, person_name])
            color = "green"
        else:
            msg.showerror("Error", "Product doesn't exist.")
            return

        # Add the new product to the table
        table.insert("", "end", values=(product_name, product_price, product_count, person_name), tags=('colored_row',))
        table.tag_configure('colored_row', background=color)

    msg.showinfo("Transaction Complete", f"Product '{product_name}' has been processed successfully.")
    reset_form()

def selected(event):
    select_option = (inv.get())
    print("You selected:", select_option)

def reset_form():
    product.set("")
    price.set("")
    count.set("")
    person.set("")
    inv.set("")

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

reset_form()

ttk.Button(win, text="Process", width=10, command=add_click).place(x=70, y=240)

win.mainloop()