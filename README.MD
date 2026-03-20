#  Password Manager (Core Python)

# Overview
A secure and simple Password Manager built using Core Python.  
It helps you store, manage, and retrieve passwords safely using encryption.

---

# Features

- Master Password Authentication  
- Encrypted Password Storage (Fernet)  
- Password Generator  
- Password Strength Checker  
- Store Multiple Credentials  
- Search Saved Sites  
- Update Passwords  
- Delete Passwords  
- Copy Password to Clipboard  
- Backup Data  

---

# Tech Stack

- Python  
- JSON  
- Cryptography (Fernet)  
- Pyperclip  
- OS, Random, String  

---

# Preview

```
--- Password Manager ---
1. Save Password
2. Get Password
3. Generate Password
4. View All Sites
5. Update Password
6. Delete Password
7. Search Site
8. Copy Password
9. Backup Data
10. Exit
```

---

# Project Structure

```
password-manager/
│
├── main.py
├── passwords.json
├── key.key
├── master.key
├── backup_passwords.json
└── README.md
```

---

# Installation

# 1. Clone Repository
```bash
git clone https://github.com/your-username/password-manager-python.git
cd password-manager-python
```

# 2. Install Dependencies
```bash
pip install cryptography pyperclip
```

---

# Run the Project

```bash
python main.py
```

---

# Security

- Uses Fernet encryption for passwords  
- Data stored locally  
- Master password required  

 Note: Master password is currently stored in plain text (can be improved using hashing)

---

# Author

Saurabh Pathare  

- GitHub: https://github.com/saurabhpathare7
- LinkedIn: https://linkedin.com/in/saurabh-pathare7  

---

# Support

If you like this project:

- Star the repo  
- Fork it  
- Share it  

---

# Note

This project is for educational purposes and demonstrates core Python + security concepts.