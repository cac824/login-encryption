# login-encryption
This is my third personal project. A sign-in/log-in application sends usernames and passwords into a file to be encrypted and decrypted to log in. It also uses user authentication. 

**Features**
  * Signing in with your username and password
  * Login with your username and password
  * Username and password are fed into a file that is encrypted after the sign-in process and is decrypted to find the username and password and encrypted again after the process is done
  * Encryption is done using **symmetric encryption** (fernet)

**Libraries Used**
  * I used the **cryptography** library for the encryption portion of the program and the **Tkinter** library for the GUI. This project uses a basic user authentication with security features.
  * I also used the **Tkinter** library for the GUI portion of the program and utilized the ttk module to enhance the layout

**Currently Working On**
 * I want to improve the password search when logging in because it's based on text matching. I want to improve it and make it more secure by having it be case-sensitive

**Future Improvements:**
  * I want to improve the encryption system and use a hashing system or RSA
  * Improve modularity
  * 2FA with email or number
  * Split the username and password into separate files to increase security
    

