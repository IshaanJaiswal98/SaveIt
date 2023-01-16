from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters+password_numbers+password_symbols


    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    password_entry.insert(0,password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():

    website= website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if len(website) == 0:
        messagebox.showerror(title="Error",message="Website Cannot be Empty")
        return

    if len(email) == 0:
        messagebox.showerror(title="Error",message="Email Cannot be Empty")
        return

    if len(password) == 0:
        messagebox.showerror(title="Error",message="Password Cannot be Empty")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details you entered:\nEmail: {email} \nPassword: {password}\nIs this Ok?")
    if is_ok:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            with open("data.json","w") as data_file:
                json.dump(data,data_file,indent=4)
        website_entry.delete(0,END)
        password_entry.delete(0,END)
        messagebox.showinfo(title=website,message="Details Saved")

#--------------------------SEARCH PASSWORD-------------------------------#
def search_password():
    website = website_entry.get().lower()
    with open("data.json","r") as data_file:
        data = json.load(data_file)
        try:
            email = data[website]['email']
            password = data[website]['password']
        except:
            messagebox.showinfo(title="Sorry", message="No data Found")
        else:
            messagebox.showinfo(title="Details", message=f"Email: {email}\nPassword: {password}")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("SaveIt")
window.config( pady=70,padx=70)
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="password.png")
canvas.create_image(100,100,image = logo_image)
canvas.grid(column=1,row=0)

#website
website_label = Label(text="Website:")
website_label.grid(column=0,row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1,row=1)
search_button = Button(text="Search",width=14, command=search_password)
search_button.grid(column=2,row=1)

#Email
email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)
email_entry = Entry(width=53)
email_entry.grid(column=1,row=2,columnspan=2)

#Password
password_label = Label(text="Password:")
password_label.grid(column=0,row=3)
password_entry = Entry(width=35)
password_entry.grid(column=1,row=3)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2,row=3)

#Add
add_button = Button(text="Add",width=45,command=save_data)
add_button.grid(column=1,row=4,columnspan=2)


window.mainloop()