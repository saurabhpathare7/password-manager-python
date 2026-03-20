import json
from cryptography.fernet import Fernet
import os
import random
import string
import pyperclip

# KEY GENERATION 
def load_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as f:
            f.write(key)
    else:
        with open("key.key", "rb") as f:
            key = f.read()
    return key

key = load_key()
cipher = Fernet(key)

# MASTER PASSWORD 
def set_master_password():
    master = input("Set master password: ")
    with open("master.key", "w") as f:
        f.write(master)

def verify_master_password():
    if not os.path.exists("master.key"):
        set_master_password()
        return True

    with open("master.key", "r") as f:
        saved = f.read()

    entered = input("Enter master password: ")
    return entered == saved

# PASSWORD GENERATOR 
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

# PASSWORD STRENGTH 
def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*" for c in password):
        score += 1

    if score <= 2:
        print(" Weak Password")
    elif score <= 4:
        print(" Medium Password")
    else:
        print(" Strong Password")

#  SAVE PASSWORD 
def save_password(site, username, password):
    data = {}

    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as f:
            data = json.load(f)

    encrypted_password = cipher.encrypt(password.encode()).decode()

    data[site] = {
        "username": username,
        "password": encrypted_password
    }

    with open("passwords.json", "w") as f:
        json.dump(data, f, indent=4)

    print(" Password saved successfully!")

#  GET PASSWORD 
def get_password(site):
    if not os.path.exists("passwords.json"):
        print(" No data found!")
        return

    with open("passwords.json", "r") as f:
        data = json.load(f)

    if site in data:
        encrypted_password = data[site]["password"]
        decrypted_password = cipher.decrypt(encrypted_password.encode()).decode()

        print(f"\n Site: {site}")
        print(f" Username: {data[site]['username']}")
        print(f" Password: {decrypted_password}")
    else:
        print(" Site not found!")

#  VIEW ALL SITES 
def view_all_sites():
    if not os.path.exists("passwords.json"):
        print(" No data found!")
        return

    with open("passwords.json", "r") as f:
        data = json.load(f)

    print("\n Saved Sites:")
    for site in data:
        print(f"- {site}")

#  UPDATE PASSWORD 
def update_password(site):
    if not os.path.exists("passwords.json"):
        print(" No data found!")
        return

    with open("passwords.json", "r") as f:
        data = json.load(f)

    if site in data:
        new_password = input("Enter new password: ")
        encrypted_password = cipher.encrypt(new_password.encode()).decode()
        data[site]["password"] = encrypted_password

        with open("passwords.json", "w") as f:
            json.dump(data, f, indent=4)

        print(" Password updated!")
    else:
        print(" Site not found!")

#  DELETE PASSWORD 
def delete_password(site):
    if not os.path.exists("passwords.json"):
        print(" No data found!")
        return

    with open("passwords.json", "r") as f:
        data = json.load(f)

    if site in data:
        del data[site]

        with open("passwords.json", "w") as f:
            json.dump(data, f, indent=4)

        print(" Deleted successfully!")
    else:
        print(" Site not found!")

#  SEARCH 
def search_site(keyword):
    if not os.path.exists("passwords.json"):
        print(" No data found!")
        return

    with open("passwords.json", "r") as f:
        data = json.load(f)

    results = [site for site in data if keyword.lower() in site.lower()]

    if results:
        print("\n🔎 Matching Sites:")
        for site in results:
            print(site)
    else:
        print(" No matches found!")

#  COPY PASSWORD 
def copy_password(site):
    if not os.path.exists("passwords.json"):
        print(" No data found!")
        return

    with open("passwords.json", "r") as f:
        data = json.load(f)

    if site in data:
        encrypted_password = data[site]["password"]
        decrypted_password = cipher.decrypt(encrypted_password.encode()).decode()

        pyperclip.copy(decrypted_password)
        print(" Password copied to clipboard!")
    else:
        print(" Site not found!")

#  BACKUP 
def backup_data():
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as f:
            data = f.read()

        with open("backup_passwords.json", "w") as f:
            f.write(data)

        print(" Backup created!")
    else:
        print(" No data to backup!")

#  MAIN 
def main():
    if not verify_master_password():
        print(" Wrong master password!")
        return

    while True:
        print("\n--- Password Manager ---")
        print("1. Save Password")
        print("2. Get Password")
        print("3. Generate Password")
        print("4. View All Sites")
        print("5. Update Password")
        print("6. Delete Password")
        print("7. Search Site")
        print("8. Copy Password")
        print("9. Backup Data")
        print("10. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            site = input("Enter site: ")
            username = input("Enter username: ")
            password = input("Enter password (leave blank to generate): ")

            if not password:
                password = generate_password()
                print(f"Generated Password: {password}")

            check_strength(password)
            save_password(site, username, password)

        elif choice == "2":
            site = input("Enter site name: ")
            get_password(site)

        elif choice == "3":
            pwd = generate_password()
            print("Generated Password:", pwd)
            check_strength(pwd)

        elif choice == "4":
            view_all_sites()

        elif choice == "5":
            site = input("Enter site: ")
            update_password(site)

        elif choice == "6":
            site = input("Enter site: ")
            delete_password(site)

        elif choice == "7":
            keyword = input("Enter keyword: ")
            search_site(keyword)

        elif choice == "8":
            site = input("Enter site: ")
            copy_password(site)

        elif choice == "9":
            backup_data()

        elif choice == "10":
            break

        else:
            print(" Invalid choice")

if __name__ == "__main__":
    main()