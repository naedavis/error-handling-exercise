import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()
root.config(bg="green")
root.geometry("400x400")
root.title("Exception Handling")

lbl_enter = Label(root, text="Please enter amount in your account", font="Arial 17")
lbl_enter.place(x=15, y=60)
e_amount = Entry(root, font="Arial 14")
e_amount.focus_set()
e_amount.place(x=70, y=120, width=240, height=50)


# function which determines whether the amount entered is enough for the user to qualify for the malaysian trip
def check_amount():
    try:
        amount = int(e_amount.get())
        # if the amount is more than or equal to 3000
        if amount >= 3000:
            # user qualifies
            messagebox.showinfo("STATUS FEEDBACK", "You Qualify for the trip to MALAYSIA")
        else:
            # user does not qualify
            messagebox.showinfo("STATUS FEEDBACK", "You DO NOT Qualify for the trip")
            e_amount.delete(0, END)
    except ValueError:
        messagebox.showinfo("STATUS FEEDBACK", "You DO NOT Qualify for the trip")
        e_amount.delete(0, END)


btn_Check = Button(root, text="Check Qualification", font="Arial 17", fg="Green", bg="white", command=check_amount)
btn_Check.place(x=80, y=200)

root.mainloop()
