import tkinter as tk

window = tk.Tk()
window.title("Requisition system")
window.geometry("500x400")

tk.Label(window, text="Staff Name").grid(row=0, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

tk.Label(window, text="Staff ID").grid(row=1, column=0)
id_entry = tk.Entry(window)
id_entry.grid(row=1, column=1)
                                                                        #Grouping this stff makes it so much easier 
tk.Label(window, text="Date").grid(row=2, column=0)
date_entry = tk.Entry(window)
date_entry.grid(row=2, column=1)

tk.Label(window, text="Item Price").grid(row=3, column=0)
price_entry = tk.Entry(window)
price_entry.grid(row=3, column=1)













items = []
listbox = tk.Listbox(window)
listbox.grid(row=4, column=0, columnspan=2)














result_label = tk.Label(window, text="")
result_label.grid(row=8, column=0, columnspan=2)














def add_item():
    price = float(price_entry.get())   
    items.append(price)
    listbox.insert(tk.END, "Item: $" + str(price))

def calculate_total():
    total = sum(items)
    result_label.config(text="Total: $" + str(total))

def check_approval():
    total = sum(items)
    name = name_entry.get()

    if total <= 1000:
        status = "Approved"
    else:
        status = "Not Approved"

    result_label.config(text=name + " | " + status + " | Total $" + str(total))












tk.Button(window, text="Add Item", command=add_item).grid(row=5, column=0)
tk.Button(window, text="Calculate Total", command=calculate_total).grid(row=5, column=1)
tk.Button(window, text="Check Approval", command=check_approval).grid(row=6, column=0, columnspan=2)




window.mainloop()








