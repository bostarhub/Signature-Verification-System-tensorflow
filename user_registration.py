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
    CREATE TABLE IF NOT EXISTS UserRegistration_record (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        User_id TEXT UNIQUE,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        password TEXT,
        mobile_number TEXT,
        address TEXT,
        signature_image BLOB,
        registration_time TEXT,
        registration_date TEXT
    )
''')
conn.commit()

# Function to generate a unique employee ID
def generate_User_id():
    timestamp = int(time.time())
    User_id = f"UserID{timestamp}"
    entry_User_id.delete(0, tk.END)
    entry_User_id.insert(0, User_id)
    entry_User_id.config(state='readonly')  # Disable the entry widget

# Function to validate input fields
def validate_input():
    User_id = entry_User_id.get()
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    password = entry_password.get()
    mobile_number = entry_mobile_number.get()
    address = entry_address.get()
    
    if not re.match("^[0-9a-zA-Z]+$", User_id):
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

    return True

# Function to save the data to the database
def save_employee_data():
    if validate_input():
        signature_image = signature_image_path
        if signature_image:  # Check if a signature image is selected
            User_id = entry_User_id.get()
            first_name = entry_first_name.get()
            last_name = entry_last_name.get()
            email = entry_email.get()
            password = entry_password.get()
            mobile_number = entry_mobile_number.get()
            address = entry_address.get()

            current_time = datetime.datetime.now().strftime("%H:%M:%S")  # Get current time as a string
            current_date = datetime.date.today()  # Get the current date

            cursor.execute('''
    INSERT OR REPLACE INTO UserRegistration_record (
        User_id, first_name, last_name, email, password, mobile_number, address,
        signature_image, registration_time, registration_date
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (User_id, first_name, last_name, email, password, mobile_number, address, signature_image, current_time, current_date))

            conn.commit()
            messagebox.showinfo("Success", "Employee data registered successfully.")
        else:
            messagebox.showerror("Error", "Please select a signature image.")
    
# Function to open the administration.py script and close the current window
def open_administration_script():
    root.destroy()  # Close the current window
    registration_window = tk.Toplevel(root)
    registration_window.title("administration Window")
    os.system(sys.executable + " administration.py")

# Create the main Tkinter window
root = tk.Tk()
root.title("User Registration")

# Make the window fullscreen
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# Background Image
bg = ImageTk.PhotoImage(file="7.jpg")
bg_image = tk.Label(image=bg)
bg_image.place(x=0, y=0, relwidth=1, relheight=1)

Frame_registration1 = tk.Frame(root, bg="sky blue", borderwidth=2, relief="ridge", highlightbackground="dark blue", highlightcolor="dark blue")
Frame_registration1.place(x=0, y=0, width=1600, height=80)
subtitle = tk.Label(Frame_registration1, text="User Registration panel!", font=("impact", 35 ), fg="white", bg="sky blue")
subtitle.place(x=600, y=10)

# Registration Frame
Frame_registration = tk.Frame(root, bg="white", borderwidth=2, relief="ridge", highlightbackground="purple", highlightcolor="purple")

Frame_registration.place(x=200, y=130, width=500, height=630)
subtitle = tk.Label(Frame_registration, text="User Registration Area", font=("Goudy old style", 15, "bold"), fg="dark blue", bg="white")
subtitle.place(x=80, y=50)
# Create and place the input fields with labels
label_User_id = tk.Label(Frame_registration, text="User ID:", fg="#6162FF", bg="white", font=("Goudy old style", 16, "bold"))
label_User_id.place(x=80, y=90)
entry_User_id = tk.Entry(Frame_registration, highlightthickness=0, font=("Goudy old style", 16, "bold"), bg="white")

# Create a "Generate ID" button
btn_generate_id = tk.Button(Frame_registration, text="Generate ID", bg="#6162FF", fg="white", command=generate_User_id, padx=20, pady=2)
btn_generate_id.place(x=280, y=150)
entry_User_id.place(x=85, y=120, width=300)

label_first_name = tk.Label(Frame_registration, text="First Name:", fg="#6162FF", bg="white", font=("Goudy old style", 16, "bold"))
label_first_name.place(x=80, y=150)
entry_first_name = tk.Entry(Frame_registration, highlightthickness=0, font=("Goudy old style", 16, "bold"), bg="white")
entry_first_name.place(x=85, y=180, width=300)

label_last_name = tk.Label(Frame_registration, text="Last Name:", fg="#6162FF", bg="white", font=("Goudy old style", 16, "bold"))
label_last_name.place(x=80, y=210)
entry_last_name = tk.Entry(Frame_registration, highlightthickness=0, font=("Goudy old style", 16, "bold"), bg="white")
entry_last_name.place(x=85, y=240, width=300)

label_email = tk.Label(Frame_registration, text="Email:", fg="#6162FF", bg="white", font=("Goudy old style", 16, "bold"))
label_email.place(x=80, y=273)
entry_email = tk.Entry(Frame_registration, highlightthickness=0, font=("Goudy old style", 16, "bold"), bg="white")
entry_email.place(x=85, y=300, width=300)

label_password = tk.Label(Frame_registration, text="Password:", fg="#6162FF", bg="white", font=("Goudy old style", 16, "bold"))
label_password.place(x=80, y=335)
entry_password = tk.Entry(Frame_registration, width=20, show='*', highlightthickness=0, font=("Goudy old style", 16, "bold"), bg="white")
entry_password.place(x=85, y=360, width=300)

label_mobile_number = tk.Label(Frame_registration, text="Mobile Number:", fg="#6162FF", bg="white", font=("Goudy old style", 16, "bold"))
label_mobile_number.place(x=80, y=390)
entry_mobile_number = tk.Entry(Frame_registration, highlightthickness=0, font=("Goudy old style", 16, "bold"), bg="white")
entry_mobile_number.place(x=85, y=420, width=300)

label_address = tk.Label(Frame_registration, text="Address:", fg="#6162FF", bg="white", font=("Goudy old style", 16, "bold"))
label_address.place(x=80, y=455)
entry_address = tk.Entry(Frame_registration, highlightthickness=0, font=("Goudy old style", 16, "bold"), bg="white")
entry_address.place(x=85, y=483, width=300)

def select_and_save_image():
    global signature_image_path
    if validate_input():
        file_path = filedialog.askopenfilename(title="Select Signature Image")

        if file_path:
            signature_image_path = file_path
            user_id = entry_User_id.get()
            first_name = entry_first_name.get()
            real_all_folder = 'dataset/REAL_ALL'  # Updated path to REAL_ALL folder

            if not os.path.exists(real_all_folder):
                os.makedirs(real_all_folder)

            # Save 10 copies of the selected image in the specified format
            for i in range(1, 11):
                copy_filename = f'{user_id}_{first_name}_{i}.jpg'
                target_path = os.path.join(real_all_folder, copy_filename)

                try:
                    shutil.copy(file_path, target_path)

                    # Open the image and set the metadata
                    image = Image.open(target_path)
                    exif_data = image.info.get("exif", b"")
                    exif = exif_data.decode("latin-1")
                    exif += f"{user_id}\nFirst Name: {first_name}\n"
                    image.info["exif"] = exif.encode("latin-1")
                    image.save(target_path)
                except Exception as e:
                    messagebox.showerror("Error", "Failed to save the Signature Image.")

            messagebox.showinfo("Success", "Signature Images saved successfully.")


btn_signature_image = tk.Button(Frame_registration, text="Select Signature Image", command=select_and_save_image, bg="#6162FF", fg="white", padx=15, pady=4, font=("Goudy old style", 15, "bold"))
btn_signature_image.place(x=85, y=510)


# Create a "Register" button
btn_register = tk.Button(Frame_registration, text="Register", command=save_employee_data, bg="#6162FF", fg="white", padx=15, pady=4, font=("Goudy old style", 15, "bold"))
btn_register.place(x=330, y=510)


def open_main_file():
    root.withdraw() 
    subprocess.run(['python', 'admin.py'])

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create an Admin menu
admin_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="back", command=open_main_file)

root.mainloop()
