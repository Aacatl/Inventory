from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("Inventory Manager")


# function add text
def submit():
    item_id = item_identification.get()
    item_p = item_price.get()
    item_q = item_quantity.get()


# title
label_title = tk.Label(root, text="Inventory Management", font=('Times New Roman', 24))
label_title.place(x=125, y=10)

# variables
item_identification = tk.StringVar()
item_quantity = tk.StringVar()
item_price = tk.StringVar()

# item id
item_identification_label = Label(root, text="Item ID:", font=('Times New Roman', 20))
item_identification_label.place(x=50, y=50)

# item quantity
item_quantity_label = Label(root, text="Item Quantity:", font=('Times New Roman', 20))
item_quantity_label.place(x=50, y=100)

# item price
item_price_label= Label(root, text="Item Price:", font=('Times New Roman', 20))
item_price_label.place(x=50, y=150)

# submit button
submit_button_label = Button(root, text="Submit", command=submit)
submit_button_label.place(x=300, y=200)

# input area's
item_identification_input_area = Entry(root, width=20)
item_identification_input_area.place(x=121, y=53)

item_quantity_input_area = Entry(root, width=20)
item_quantity_input_area.place(x=171, y=103)

item_price_input_area = Entry(root, width=20)
item_price_input_area.place(x=141, y=153)

root.mainloop()
