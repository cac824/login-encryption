import re
import tkinter as tk
from tkinter import ttk
from zxcvbn import zxcvbn
import hashlib
import os


def check_file(text):  # checks file existence
    if not os.path.exists(text):
        with open(text, "w") as file:
            file.write("")  # if the file doesnt exist it will create an empty file


def encode_file(text):  # encrypts/decrypts files
    check_file("password")
    check_file("user")

    encoded_string = text.encode("utf-8")  # Encode string to bytes
    hash_object = hashlib.sha256()  # Create hash object
    hash_object.update(encoded_string)  # Update hash object with encoded string
    return hash_object.hexdigest()  # Return the hex digest of the hash


def message(title, text):  # makes error and success messages
    # message_window
    message_window = tk.Tk()
    message_window.geometry("400x400")
    message_window.title(title)
    message_label = tk.Label(message_window, text=text, font="Arial")
    message_label.pack()


def sign_in():
    user = entry1.get()
    password = entry2.get()
    encode_file(user)
    encode_file(password)
    if user and password:  # checks if both entries are filled out
        with open("user", "r") as file:
            if encode_file(user) in file:  # checks if the given username already exists
                message("Error", "Username in use, make another")
                return

        result = zxcvbn(password)
        if result['score'] >= 3:
            with open("user", "a") as file:
                file.write(encode_file(user) + "\n")  # enters the user into the file
            with open("password", "a") as file:
                file.write(encode_file(password) + "\n")
            entry1.delete(0, tk.END)  # clears the entries after all are filled out and submitted
            entry2.delete(0, tk.END)
            window.destroy()  # closes the sign-in window
        else:
            message("Error", "Weak Password\nAdd numbers and special characters")
    else:
        message("Error", "Both entries need to be filled out")


def log_in():
    log_user = entry3.get()
    log_password = entry4.get()
    if log_user and log_password:  # checks if both entries are filled out
        with open("user", "r") as file:  # checks if the given user and password are in the file
            stored_users = [line.strip() for line in file.readlines()]
        with open("password", "r") as file:
            stored_passwords = [line.strip() for line in file.readlines()]

        if encode_file(log_user) in stored_users and encode_file(log_password) in stored_passwords:  # looks for user and password
            message("Success", "Login Successful!")
            entry3.delete(0, tk.END)
            entry4.delete(0, tk.END)
        else:
            message("Error", "Wrong username or password")
    else:
        message("Error", "Both entries need to be filled out")


def handle_signin_click():
    if is_signin_checked.get():
        entry2.config(show="")
    else:
        entry2.config(show="*")


def handle_login_click():
    if is_login_checked.get():
        entry4.config(show="")
    else:
        entry4.config(show="*")


#  checks files existence
check_file("user")
check_file("password")

window = tk.Tk()  # Sign in screen
window.geometry("500x500")
window.title("Sign In")
window.configure(padx=20, pady=20)

is_signin_checked = tk.IntVar()

label1 = ttk.Label(window, text="Username", font="Arial")
label1.pack()

entry1 = ttk.Entry(window)
entry1.pack()

label2 = ttk.Label(window, text="Password", font="Arial")
label2.pack()

check_button = ttk.Checkbutton(window, text="Show Password", variable=is_signin_checked, command=handle_signin_click)
check_button.pack()

entry2 = ttk.Entry(window, show="*")
entry2.pack()

button = ttk.Button(window, text="Sign In", command=sign_in)
button.pack()

button2 = ttk.Button(window, text="Already Signed In?", command=window.destroy)
button2.pack()

window.mainloop()

log_window = tk.Tk()  # Log in screen
log_window.geometry("500x500")
log_window.title("Log In")
log_window.configure(padx=20, pady=20)

is_login_checked = tk.IntVar()

label3 = ttk.Label(log_window, text="Username", font="Arial")
label3.pack()

entry3 = ttk.Entry(log_window)
entry3.pack()

label4 = ttk.Label(log_window, text="Password", font="Arial")
label4.pack()

check_button2 = ttk.Checkbutton(log_window, text="Show Password", variable=is_login_checked, command=handle_login_click)
check_button2.pack()

entry4 = ttk.Entry(log_window, show="*")
entry4.pack()

button = ttk.Button(log_window, text="Log In", command=log_in)
button.pack()

log_window.mainloop()
