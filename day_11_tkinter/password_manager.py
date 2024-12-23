import tkinter as tk
from tkinter import messagebox
import json
import secrets
import string

# Function to generate a random password
def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(12))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to save password
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            data = {}

        if website in data:
            messagebox.showinfo(title="Website Exists", message=f"A password for {website} already exists.")
        else:
            is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                               f"\nPassword: {password} \nIs it ok to save?")
            if is_ok:
                data.update({website: {"email": email, "password": password}})
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)

# Function to search for a website
def search_website():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="No Data", message="No data file found.")
        return

    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title="Website Exists", message=f"Email: {email}\nPassword: {password}")
    else:
        messagebox.showinfo(title="Website Not Found", message=f"No entry found for {website}.")

# Create the main window
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
canvas = tk.Canvas(height=200, width=200)
canvas.create_image(100, 100)
canvas.grid(row=0, column=1, pady=20)

# Website Entry
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0, padx=10, pady=10)
website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
website_entry.focus()

# Search Button
search_button = tk.Button(text="Search", command=search_website)
search_button.grid(row=1, column=3, padx=10, pady=10)

# Email Entry
email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0, padx=10, pady=10)
email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
email_entry.insert(0, "your_email@example.com")

# Password Entry
password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0, padx=10, pady=10)
password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1, padx=10, pady=10)

# Buttons
generate_password_button = tk.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, padx=10, pady=10)
add_button = tk.Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

window.mainloop()
