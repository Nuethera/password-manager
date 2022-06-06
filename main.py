from tkinter import *
from tkinter import messagebox
from passgen import Passgen
import pyperclip

FONT = ("Arial", 10, "normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
gen = Passgen()


def generatepass():
    p = gen.makepass()
    entry_password.delete(0, 'end')
    entry_password.insert(0, p)
    pyperclip.copy(p)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = entry_website.get()
    user = entry_email.get()
    passw = entry_password.get()
    if website == '' or user == '' or passw == '':
        messagebox.showinfo(title="Empty Entry Field", message="Please enter all the details")
    else:
        pass_str = f"{website},{user},{passw}\n"
        is_ok = messagebox.askokcancel(title=website, message=f"These are the deatils you entered:\nEmail/Username: "
                                                              f"{user}\nPassword: {passw}\nIs it ok to save?")
        if is_ok:
            try:
                f = open("new_pass.csv", 'a')
            except FileNotFoundError:
                f = open("new_pass.csv", "w")
                f.write("email,user,password\n")
            finally:
                f.write(pass_str)
                f.close()
            entry_password.delete(0, 'end')
            entry_email.delete(0, 'end')
            entry_website.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:", font=FONT)
label_website.grid(row=1, column=0)

label_email = Label(text="Email/Username:", font=FONT)
label_email.grid(row=2, column=0)

label_password = Label(text="Password:", font=FONT)
label_password.grid(row=3, column=0)

entry_website = Entry(width=35, font=FONT)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()
entry_email = Entry(width=35, font=FONT)
entry_email.grid(column=1, row=2, columnspan=2)

entry_password = Entry(width=20, font=FONT)
entry_password.grid(column=1, row=3, columnspan=1)

button_pass = Button(text="Generate Password", font=FONT, command=generatepass)
button_pass.grid(column=2, row=3, sticky='w')

button_add = Button(text="Add", width=36, font=FONT, command=save_password)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
