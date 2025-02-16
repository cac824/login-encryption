# login-encryption
This is my third personal project. A sign-in/log-in application sends usernames and passwords into a file to be encrypted and decrypted to log in. It also uses user authentication. The username and password are hashed, and the program could be improved by using bcrypt to make it more secure.

**Features**
  * Signing in with your username and password
  * Login with your username and password
  * Username and password are split into different files where it is hashed, and when logging in, the given username and password are hashed and checked against the password and username in the files
  * Encryption is done using **SHA-256** (hashlib)
    

**Libraries Used**
  * I used the **hashlib** library for the encryption portion of the program. This project uses a basic user authentication with security features.
  * I also used the **Tkinter** library for the GUI portion of the program and utilized the ttk module to enhance the layout

**Currently Working On**
 * I'm currently trying to use bcrypt to make it more secure by salting the passwords

**Future Improvements:**
  * I want to improve the encryption system and use a hashing system like bcrypt
  * Improve modularity
  * 2FA with email or number
  * I want to use a database to hold the passwords and usernames because plaintext is not as secure compared to MongoDB or SQL 
    

