import tkinter as tk
from tkinter import *
from tkinter import messagebox

# dictionary used to hold username and password
user_pass = {"Naeemah": "davis09", "Ikraam": "sage21", "Atheelah": "vdschyff17"}

root = tk.Tk()
root.config(bg="green")
root.geometry("400x400")
root.title("Login Screen")
# title displayed on window
lbl_title = Label(root, text="Please enter login details", font="Arial 20")
lbl_title.place(x=50, y=30)
# label on widnow
lbl_user = Label(root, text="Username:", font="Arial 16", bg="green", fg="white")
lbl_user.place(x=135, y=90)
# entry for user to input their username
e_user = Entry(root, font="Arial 15")
# setting the focus to this entry when program is run
e_user.focus_set()
e_user.place(x=90, y=130, width=200)

lbl_pass = Label(root, text="Password:", font="Arial 16", bg="green", fg="white")
lbl_pass.place(x=135, y=170)
e_pass = Entry(root, font="Arial 15")
e_pass.place(x=90, y=210, width=200)


# function defined for capturing the username and password and letting the user know whether or not their entries are
# valid and match with the password set for the that specific username in the dictionary
def authentication():
    # checks if the value the user entered corresponds with the keys in the dictionary
    if e_user.get() in user_pass:
        # checks if the value in the password entry corresponds with the username entered
        if e_pass.get() == user_pass[e_user.get()]:
            # display a message saying login successful
            messagebox.showinfo("Authentication", "Login Successful!")
            # destroy the current window
            root.destroy()
            # import the next window
            import exception_handling
        else:
            messagebox.showinfo("Authentication", "Login Unsuccessful!")
            e_user.delete(0, END)
            e_pass.delete(0, END)
            # sets focus back on the username entry because if i dont do that and the message goes away the focus
            # remains on the password entry
            e_user.focus_set()
    else:
        messagebox.showinfo("Authentication", "Login Unsuccessful")
        e_user.delete(0, END)
        e_pass.delete(0, END)
        e_user.focus_set()


btn_login = Button(root, text="Login", font="Arial 15", bg="white", fg="green", command=authentication)
btn_login.place(x=150, y=260)

root.mainloop()
