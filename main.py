from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']
small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def gen_pass():

    rand_cap_let = [random.choice(capital_letters) for _ in range(random.randint(4, 6))]
    rand_small_let = [random.choice(small_letters) for _ in range(random.randint(4, 6))]
    rand_num = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    rand_sym = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    random_password = rand_cap_let + rand_small_let + rand_num + rand_sym
    random.shuffle(random_password)

    random_password = "".join(random_password)

    pass_entry.delete(0, END)
    pass_entry.insert(0, random_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    web = web_entry.get()
    mail = user_entry.get()
    pas = pass_entry.get()

    if len(web) == 0 or len(pas) == 0:
        messagebox.showinfo(title="Ooops", message="Please don't leave empty fields")
    else:
        is_ok = messagebox.askyesno(title=web, message=f"This are the details you entered: \nEmail: {mail} "
                                                       f"\nPassword: {pas} \nAre you confirm?")

        if is_ok:
            with open("data.txt", 'a') as data:
                data.write(f"Website: {web}  |  Username: {mail}  |  "
                           f"Password: {pas}\n")
            web_entry.delete(0, END)
            pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")


canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website = Label()
website.config(text="Website:", bg="white")
website.grid(row=1, column=0)

username = Label()
username.config(text="Email/Username:", bg="white")
username.grid(row=2, column=0)

password = Label()
password.config(text="Password:", bg="white")
password.grid(row=3, column=0)

# Entry
web_entry = Entry(width=50)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

user_entry = Entry(width=50)
user_entry.grid(row=2, column=1, columnspan=2)

pass_entry = Entry(width=32)
pass_entry.grid(row=3, column=1)


# Buttons
gen_pass_button = Button()
gen_pass_button.config(text="Generate Password", bg="white", command=gen_pass)
gen_pass_button.grid(row=3, column=2)

add_button = Button(width=43)
add_button.config(text="Add", bg='white', command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
