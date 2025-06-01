import os
import time

TRAP_FILE = "Passwords.txt"

def create_trap():
    if not os.path.exists(TRAP_FILE):
        with open(TRAP_FILE, "w") as f:
            f.write("This is confidential.\nusername: admin\npassword: 1234")

def trap_triggered():
    return os.path.getatime(TRAP_FILE) > os.path.getctime(TRAP_FILE)
