import re
import tkinter as tk
from cryptography.fernet import Fernet

def encode_file(mode , file_name): # encrypts/decrypts files
    global encrypted_content
    key = Fernet.generate_key()  # generates key
    fernet = Fernet(key)
    if mode == "E": # checks if its encrypting
        with open("filekey.key", "wb") as key_file:
            key_file.write(key)
        with open("filekey.key","rb") as key_file:
            key_file.read()
        with open(file_name, "rb") as file:
            content = file.read()
        with open(file_name, "wb") as file:
            encrypted_content = fernet.encrypt(content)  # encrypted file
            file.write(encrypted_content)
    elif mode == "D": # checks if its decrypting
        with open("filekey.key", "rb") as file:
            key = file.read()
        fernet = Fernet(key)
        with open(file_name, "rb") as file:
            encrypted_content = file.read()
            decrypted_content = fernet.decrypt(encrypted_content)
        with open(file_name, "wb") as file:
            file.write(decrypted_content)
def sign_in():
    user = entry1.get()
    password = entry2.get()
    if user and password:  # checks if both entries are filled out
        with open("sign-in_info", "a") as file:
            file.write(user + "\n")  # enters the user and password into the file
            file.write(password + "\n")
        entry1.delete(0, tk.END)  # clears the entries after all are filled out and submitted
        entry2.delete(0, tk.END)
        window.destroy()  # closes the sign in window after succesfully signing in and opens the log in window
        encode_file("E", "sign-in_info")

def log_in():
    log_user = entry3.get()
    log_password = entry4.get()
    if log_user and log_password:  # checks if both entries are filled out
        encode_file("D", "sign-in_info")
        with open("sign-in_info", "r") as file:  # checks if the given user and password is in the file
            contents = file.read()
            if re.search(log_user, contents) and re.search(log_password, contents): # looks through the files and finds the user and password
                new_window = tk.Tk()
                new_window.geometry("200x100")
                new_window.title("Success!")
                success_label = tk.Label(new_window, text="Login Successful!", font="Arial")
                success_label.pack()
    encode_file("E", "sign-in_info") # encrypts the file again after opening and decrypting it


window = tk.Tk()  #   Sign in screen
window.geometry("500x500")
window.title("Sign In")

label1 = tk.Label(window, text="Username", font="Arial")
label1.pack()

entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text="Password", font="Arial")
label2.pack()

entry2 = tk.Entry(window)
entry2.pack()

button = tk.Button(window, text="Sign In", font="Arial", command=sign_in)
button.pack()

window.mainloop()

log_window = tk.Tk()  # Log in screen
log_window.geometry("500x500")
log_window.title("Log In")

label3 = tk.Label(log_window, text="Username", font="Arial")
label3.pack()

entry3 = tk.Entry(log_window)
entry3.pack()

label4 = tk.Label(log_window, text="Password", font="Arial")
label4.pack()

entry4 = tk.Entry(log_window)
entry4.pack()

button = tk.Button(log_window, text="Log In", font="Arial", command=log_in)
button.pack()

log_window.mainloop()
