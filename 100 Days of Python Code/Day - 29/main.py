import tkinter
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for sym in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for num in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SEARCH WEBSITE ------------------------------- #

def search():
    try:
        with open("data.json", 'r') as data_file:
            website_name = website_entry.get()
            data = json.load(data_file)
            found = False
            for website in data:
                if website_name == website:
                    found = True
                    messagebox.showinfo(title=f"{website_name}", message=f"Email: {data[website_name]['email']}\nPassword: {data[website_name]['password']}")
            if not found:
                messagebox.showinfo(title=website_name, message="No details for the website exists")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_name = website_entry.get()
    email_name = email_entry.get()
    password = password_entry.get()
    new_data = {
        website_name: {
            "email":email_name,
            "password":password
        }
    }

    if len(website_name) == 0 or len(email_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opps", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"These are details you filled\nUsername/Email: {email_name}\nPassword: {password}")

        if is_ok:
            try:
                with open("data.json", 'r') as data_file:
                    #reading the json file
                    data = json.load(data_file)
                    #adding new_data to data
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", 'w') as data_file:
                    #writing the json file
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", 'w') as data_file:
                    #writing the json file
                    json.dump(data, data_file, indent=4)
            finally:
                #clears the entry
                website_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.minsize(width=400, height= 300)
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
pass_logo = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100,100, image=pass_logo)
canvas.grid(column=1, row=1)

#Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(row=2, column=0, padx=20)
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=3, column=0)
password_label = tkinter.Label(text="Password:")
password_label.grid(row=4, column=0, padx=20)

#Entry
website_entry = tkinter.Entry(width=32)
website_entry.focus()
website_entry.grid(row=2,column=1)
email_entry = tkinter.Entry(width=50)
email_entry.grid(row=3,column=1,columnspan=2)
email_entry.insert(0, "jmkl0987@gmail.com")
password_entry = tkinter.Entry(width=32)
password_entry.grid(row=4,column=1)

#Buttons
generate_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=2)
add_button = tkinter.Button(text="Add", width=43, command=save)
add_button.grid(row=5, column=1, columnspan=2)
search_button = tkinter.Button(text="Search", width=15, command=search)
search_button.grid(row=2,column=2)

window.mainloop()