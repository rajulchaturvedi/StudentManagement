# auth.py

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"

def login():
    print("===== Admin Login =====")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Login successful!\n")
        return True
    else:
        print("Invalid credentials!\n")
        return False