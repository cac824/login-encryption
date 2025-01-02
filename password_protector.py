import re
import tkinter as tk
from tkinter import ttk

from zxcvbn import zxcvbn
from cryptography.fernet import Fernet
import os


def check_keyfile():
    if not os.path.exists("filekey.key"):
        key = Fernet.generate_key()
        with open("filekey.key", "wb") as key_file:
            key_file.write(key)


def encode_file(mode, file_name):  # encrypts/decrypts files
    check_keyfile() # checks the existence of the key file

    with open("filekey.key", "rb") as key_file: # reads the key file
        key = key_file.read()

    fernet = Fernet(key)

    if mode == "E":  # checks if it's encrypting
        with open(file_name, "rb") as file:  # reads everything in the file and stores it into content
            content = file.read()
        with open(file_name, "wb") as file:  # encrypts the content and writes it into the encrypted_content
            encrypted_content = fernet.encrypt(content)  # encrypted file
            file.write(encrypted_content)
    elif mode == "D":  # checks if it's decrypting
        with open(file_name, "rb") as file:  # reads the encrypted content and decrypts it
            encrypted_content = file.read()
            decrypted_content = fernet.decrypt(encrypted_content)
        with open(file_name, "wb") as file:  # writes the decrypted_content into the file
            file.write(decrypted_content)


def check_file():
    if not os.path.exists("sign-in_info"):
        with open("sign-in_info", "w") as file:
            file.write("")  # if the file doesnt exist it will create an empty file
        encode_file("E", "sign-in_info")  # encrypts the file


def error(text):
    # error_window
    error_window = tk.Tk()
    error_window.geometry("400x400")
    error_window.title("Error")
    error_label = tk.Label(error_window, text=text, font="Arial")
    error_label.pack()


def sign_in():
    user = entry1.get()
    password = entry2.get()
    if user and password:  # checks if both entries are filled out
        with open("sign-in_info", "r") as file:
            encode_file("D", "sign-in_info")
            contents = file.read()
            if re.search(user, contents):  # checks if the given username already exists
                error("Username in use, make another")
                encode_file("E", "sign-in_info")
                return

        result = zxcvbn(password)
        if result['score'] >= 3:
            with open("sign-in_info", "a") as file:
                file.write(user + "\n")  # enters the user and password into the file
                file.write(password + "\n")
            encode_file("E", "sign-in_info")  # encrypt the file after writing
            entry1.delete(0, tk.END)  # clears the entries after all are filled out and submitted
            entry2.delete(0, tk.END)
            window.destroy()  # closes the sign-in window
        else:
            error("Weak Password\nAdd numbers and special characters")
            encode_file("E", "sign-in_info")
    else:
        error("Both entries need to be filled out")


def log_in():
    log_user = entry3.get()
    log_password = entry4.get()
    if log_user and log_password:  # checks if both entries are filled out
        encode_file("D", "sign-in_info")  # decrypt the file
        with open("sign-in_info", "r") as file:  # checks if the given user and password are in the file
            contents = file.read()
            if re.search(log_user, contents) and re.search(log_password, contents):  # looks for user and password
                new_window = tk.Tk()
                new_window.geometry("200x100")
                new_window.title("Success!")
                success_label = tk.Label(new_window, text="Login Successful!", font="Arial")
                success_label.pack()
            else:
                error("Wrong username or password")
        encode_file("E", "sign-in_info")  # re-encrypt the file after checking
    else:
        error("Both entries need to be filled out")


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


# calls the check functions to ensure existense of these files
check_keyfile()
check_file()

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
