import tkinter as tk
from PIL import Image, ImageTk
import sys
import sqlite3
from tkinter import messagebox
import re
import os
import datetime
from tkinter import filedialog
import time
import shutil
import subprocess

# Create or connect to the SQLite database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create an employees table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS AdminRegistration_record (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id TEXT UNIQUE,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        password TEXT,
        mobile_number TEXT,
        address TEXT,
        designation TEXT,
        registration_time TEXT,
        registration_date TEXT
    )
''')
conn.commit()

# Function to generate a unique employee ID
def generate_employee_id():
    timestamp = int(time.time())
    employee_id = f"EMP{timestamp}"
    entry_employee_id.delete(0, tk.END)
    entry_employee_id.insert(0, employee_id)
    entry_employee_id.config(state='readonly')  # Disable the entry widget

# Function to validate input fields
def validate_input():
    employee_id = entry_employee_id.get()
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    password = entry_password.get()
    mobile_number = entry_mobile_number.get()
    address = entry_address.get()
    designation = entry_designation.get()
    
    if not re.match("^[0-9a-zA-Z]+$", employee_id):
        messagebox.showerror("Error", "Invalid Employee ID (Only alphanumeric characters allowed)")
        return False

    if not (re.match("^[a-zA-Z]+$", first_name) and re.match("^[a-zA-Z]+$", last_name)):
        messagebox.showerror("Error", "Invalid First Name or Last Name (Only letters allowed)")
        return False

    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        messagebox.showerror("Error", "Invalid Email Format")
        return False

    if len(password) < 6:
        messagebox.showerror("Error", "Password must be at least 6 characters long")
        return False

    if not re.match("^[0-9]{11}$", mobile_number):
        messagebox.showerror("Error", "Invalid Mobile Number (11 digits allowed)")
        return False
    
    if not re.match("^[0-9a-zA-Z]+$", address):
        messagebox.showerror("Error", "Invalid Address (Only alphanumeric characters allowed)")
        return False

    if not re.match("^[0-9a-zA-Z]+$", designation):
        messagebox.showerror("Error", "Invalid Designation (Only alphanumeric characters allowed)")
        return False
    

    return True

# Function to save the data to the database
def save_employee_data():
    if validate_input():
            employee_id = entry_employee_id.get()
            first_name = entry_first_name.get()
            last_name = entry_last_name.get()
            email = entry_email.get()
            password = entry_password.get()
            mobile_number = entry_mobile_number.get()
            address = entry_address.get()
            designation = entry_designation.get()

            current_time = datetime.datetime.now().strftime("%H:%M:%S")  # Get current time as a string
            current_date = datetime.date.today()  # Get the current date

            cursor.execute('''
                INSERT OR REPLACE INTO AdminRegistration_record (
                    employee_id, first_name, last_name, email, password, mobile_number, address, designation,
                registration_time, registration_date
                ) VALUES (?, ?, ?, ?, ?, ?, ?,  ?, ?, ?)
            ''', (employee_id, first_name, last_name, email, password, mobile_number, address, designation, current_time, current_date))

            conn.commit()
            messagebox.showinfo("Success", "Employee data registered successfully.")
    
# Function to open the administration.py script and close the current window
def open_administration_script():
    root.destroy()  # Close the current window
    registration_window = tk.Toplevel(root)
    registration_window.title("administration Window")
    os.system(sys.executable + " administration.py")

# Create the main Tkinter window
root = tk.Tk()
root.title("Employee Registration")

# Make the window fullscreen
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# Background Image
bg = ImageTk.PhotoImage(file="7.jpg")
bg_image = tk.Label(image=bg)
bg_image.place(x=0, y=0, relwidth=1, relheight=1)

Frame_registration1 = tk.Frame(root, bg="sky blue", borderwidth=2, relief="ridge", highlightbackground="dark blue", highlightcolor="dark blue")
Frame_registration1.place(x=0, y=0, width=1600, height=80)
subtitle = tk.Label(Frame_registration1, text="Employee Registration panel!", font=("impact", 35 ), fg="white", bg="sky blue")
subtitle.place(x=520, y=10)

# Registration Frame
Frame_registration = tk.Frame(root, bg="white", borderwidth=2, relief="ridge", highlightbackground="purple", highlightcolor="purple")
Frame_registration.place(x=200, y=100, width=500, height=700)
subtitle = tk.Label(Frame_registration, text="Members Registration Area", font=("Goudy old style", 15, "bold"), fg="dark blue", bg="white")
subtitle.place(x=80, y=20)


# Create and place the input fields with labels
label_employee_id = tk.Label(Frame_registration, text="Employee ID:", fg="#6162FF", bg="white", font=("Goudy old style", 16, "bold"))
label_employee_id.place(x=80, y=60)
entry_employee_id = tk.Entry(Frame_registration, highlightthickness=0, font=("Goudy old style", 16, "bold"), bg="white")
entry_employee_id.place(x=85, y=90, width=300)

# Create a "Generate ID" button
btn_generate_id = tk.Button(Frame_registration, text="Generate ID", bg="#6162FF", fg="white", command=generate_employee_id, padx=20, pady=2)
btn_generate_id.place(x=280, y=120)

label_first_name = tk.Label(Frame_registration, text="First Name:", fg="#6162FF", bg="white", font=("Goudy old style", 16, "bold"))
label_first_name.place(x=80, y=130)
entry_first_name = tk.Entry(Frame_registration, highlightthickness=0, font=("Goudy old style", 16, "bold"), bg="white")
entry_first_name.place(x=85, y=160, width=300)

label_last_name = tk.Label(Frame_registration, text="Last Name:", fg="#6162FF", bg="white", font=("Goudy old style", 16, "bold"))
label_last_name.place(x=80, y=190)
entry_last_name = tk.Entry(Frame_registration, highlightthickness=0, font=("Goudy old style", 16, "bold"), bg="white")
entry_last_name.place(x=85, y=220, width=300)

label_email = tk.Label(Frame_registration, text="Email:", fg="#6162FF", bg="white", font=("Goudy old style", 16, "bold"))
label_email.place(x=80, y=250)
entry_email = tk.Entry(Frame_registration, highlightthickness=0, font=("Goudy old style", 16, "bold"), bg="white")
entry_email.place(x=85, y=280, width=300)

label_password = tk.Label(Frame_registration, text="Password:", fg="#6162FF", bg="white", font=("Goudy old style", 16, "bold"))
label_password.place(x=80, y=310)
entry_password = tk.Entry(Frame_registration, width=20, show='*', highlightthickness=0, font=("Goudy old style", 16, "bold"), bg="white")
entry_password.place(x=85, y=340, width=300)

label_mobile_number = tk.Label(Frame_registration, text="Mobile Number:", fg="#6162FF", bg="white", font=("Goudy old style", 16, "bold"))
label_mobile_number.place(x=80, y=370)
entry_mobile_number = tk.Entry(Frame_registration, highlightthickness=0, font=("Goudy old style", 16, "bold"), bg="white")
entry_mobile_number.place(x=85, y=400, width=300)

label_address = tk.Label(Frame_registration, text="Address:", fg="#6162FF", bg="white", font=("Goudy old style", 16, "bold"))
label_address.place(x=80, y=430)
entry_address = tk.Entry(Frame_registration, highlightthickness=0, font=("Goudy old style", 16, "bold"), bg="white")
entry_address.place(x=85, y=460, width=300)

label_designation = tk.Label(Frame_registration, text="Designation:", fg="#6162FF", bg="white", font=("Goudy old style", 16, "bold"))
label_designation.place(x=80, y=490)
entry_designation = tk.Entry(Frame_registration, highlightthickness=0, font=("Goudy old style", 16, "bold"), bg="white")
entry_designation.place(x=85, y=520,width=300)

# Create a "Register" button
btn_register = tk.Button(Frame_registration, text="Register", command=save_employee_data, bg="#6162FF", fg="white", padx=15, pady=4, font=("Goudy old style", 15, "bold"))
btn_register.place(x=85, y=550)

# Function to open the administration.py script in a new window
def open_admin_login_window():
    root.withdraw()  # Hide the current window
    os.system(sys.executable + "admin_login.py")  # Adjust the file path according to your folder structure

btn_open_admin_login = tk.Button(Frame_registration, text="Login", command=open_admin_login_window, bg="#6162FF", fg="white", padx=15, pady=4, font=("Goudy old style", 15, "bold"))
btn_open_admin_login.place(x=266, y=550, width=120)

def open_main_file():
    root.withdraw() 
    subprocess.run(['python', 'admin.py'])

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create an Admin menu
admin_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Go Back", command=open_main_file)

root.mainloop()
