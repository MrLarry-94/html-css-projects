from tkinter import *
from tkinter import messagebox
import random

# --- Functions ---
def closing():
    frm_order.destroy()

def reset():
    ent_customer_name.config(state=NORMAL)
    ent_customer_name.delete(0, END)
    lbl_customer_copy.config(text="")
    lbl_coffee_price.config(text="")
    lbl_tax.config(text="")
    lbl_total.config(text="")
    lbl_payment_processed.config(text="")
    size_var.set("Small")
    lbx_payment.selection_set(0)
    for ingredient in ingredient_vars.values():
        ingredient.set(0)
    ent_customer_name.focus()

def update_price(event=None):
    size = size_var.get()
    if size == "Small":
        base_price = 2.00
    elif size == "Medium":
        base_price = 3.00
    else:
        base_price = 4.00

    ingredient_cost = sum([0.25 for var in ingredient_vars.values() if var.get() == 1])
    total_price = base_price + ingredient_cost
    tax = total_price * 0.10
    total = total_price + tax

    lbl_coffee_price.config(text=f"${total_price:.2f}", fg="blue")
    lbl_tax.config(text=f"${tax:.2f}", fg="blue")
    lbl_total.config(text=f"${total:.2f}", fg="blue")
    lbl_ingredient_price.config(text=f"Ingredients = ${ingredient_cost:.2f}", fg="blue")

def process():
    name = ent_customer_name.get()
    lbl_customer_copy.config(text=f"Thank you, {name}!", fg="red")
    update_price()

    selected_payment = lbx_payment.get(ACTIVE)
    lbl_payment_processed.config(text=f"Processed Payment: {selected_payment}", fg="red")

def help_popup():
    messagebox.showinfo("Help", "Enter your name, select coffee cup size, then click 'Process'.\nUse 'Reset' to clear the form.\nClick 'Confirm' to lock the name.")

def confirm():
    ent_customer_name.config(state=DISABLED)
    messagebox.showinfo("Confirmed", "Customer name confirmed!")

# --- Main Window Setup ---
frm_order = Tk()
frm_order.title("Best Coffee Shop Ever! - Developed By Lawrence Oladimeji")
frm_order.configure(bg="sky blue")
frm_order.geometry("800x600")
frm_order.resizable(False, False)

order_number = random.randint(1000, 9999)

# --- UI Layout ---
Label(frm_order, text="Best Coffee Shop Ever!!", font="Arial 20 bold", bg="sky blue", fg="navy").place(x=220, y=10)

# Customer Name and Order Number
Label(frm_order, text="Customer Name:", font="Arial 14", bg="sky blue", fg="navy").place(x=20, y=60)
ent_customer_name = Entry(frm_order, font="Arial 14", width=25)
ent_customer_name.place(x=180, y=60)
lbl_customer_copy = Label(frm_order, text="", font="Arial 14", bg="sky blue")
lbl_customer_copy.place(x=180, y=100)

Label(frm_order, text=f"Order #{order_number}", font="Arial 14", bg="sky blue", fg="navy").place(x=520, y=60)

# Coffee Cup Sizes
Label(frm_order, text="Coffee Cup Size:", font="Arial 16 bold", bg="sky blue", fg="navy").place(x=20, y=150)
size_var = StringVar(value="Small")
sizes = ["Small", "Medium", "Large"]
for i, size in enumerate(sizes):
    Radiobutton(frm_order, text=size, variable=size_var, value=size, font="Arial 12", bg="sky blue", fg="blue", command=update_price).place(x=30, y=190 + i * 30)

# Ingredients
Label(frm_order, text="Additional Ingredients:", font="Arial 16 bold", bg="sky blue", fg="navy").place(x=200, y=150)
ingredient_vars = {
    "Milk": IntVar(),
    "Creamer": IntVar(),
    "Chocolate": IntVar()
}
for i, (ingredient, var) in enumerate(ingredient_vars.items()):
    Checkbutton(frm_order, text=ingredient, variable=var, font="Arial 12", bg="sky blue", fg="blue", command=update_price).place(x=210, y=190 + i * 30)

# Ingredient Price Underneath
lbl_ingredient_price = Label(frm_order, text="Ingredients = $0.00", font="Arial 12", bg="sky blue", fg="blue")
lbl_ingredient_price.place(x=210, y=350)

# Payment Method
Label(frm_order, text="Payment Method:", font="Arial 14 bold", bg="sky blue", fg="navy").place(x=460, y=150)
lbx_payment = Listbox(frm_order, height=7, font="Arial 12", fg="blue", exportselection=False)  # Kept height as 7
for method in ["Cash", "Check", "Visa", "Mastercard", "American Express", "Crypto"]:
    lbx_payment.insert(END, method)
lbx_payment.place(x=460, y=190)

# Payment Result Label
lbl_payment_processed = Label(frm_order, text="", font="Arial 12", bg="sky blue", fg="red")
lbl_payment_processed.place(x=460, y=360)

# Cost Summary (moved up)
Label(frm_order, text="Cost", font="Arial 14 bold", bg="sky blue", fg="navy").place(x=20, y=360)
Label(frm_order, text="Coffee Price:", font="Arial 14", bg="sky blue", fg="navy").place(x=20, y=390)
lbl_coffee_price = Label(frm_order, text="$0.00", font="Arial 14", bg="sky blue", fg="blue")
lbl_coffee_price.place(x=160, y=390)

Label(frm_order, text="MN Tax (10%):", font="Arial 14", bg="sky blue", fg="navy").place(x=20, y=420)
lbl_tax = Label(frm_order, text="$0.00", font="Arial 14", bg="sky blue", fg="blue")
lbl_tax.place(x=160, y=420)

Label(frm_order, text="Total Price:", font="Arial 14 bold", bg="sky blue", fg="navy").place(x=20, y=450)
lbl_total = Label(frm_order, text="$0.00", font="Arial 14 bold", bg="sky blue", fg="blue")
lbl_total.place(x=160, y=450)

# Buttons (Moved to line up with Additional Ingredients)
Button(frm_order, text="Help", font="Arial 12", width=10, command=help_popup).place(x=200, y=530)
Button(frm_order, text="Confirm", font="Arial 12", width=10, command=confirm).place(x=310, y=530)
Button(frm_order, text="Process", font="Arial 12", width=10, command=process).place(x=420, y=530)
Button(frm_order, text="Reset", font="Arial 12", width=10, command=reset).place(x=530, y=530)
Button(frm_order, text="Quit", font="Arial 12", width=10, command=closing).place(x=640, y=530)

# Start App
frm_order.mainloop()
