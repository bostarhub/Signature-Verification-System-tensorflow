import sqlite3
import tkinter as tk
import os
from datetime import datetime
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
import subprocess

# Create or connect to the SQLite database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create a logout_records table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Userlogout_record (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id TEXT,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        password TEXT,
        mobile_number TEXT,
        address TEXT,
        signature_image TEXT,
        registration_time TEXT,
        registration_date TEXT,
        logout_time TEXT,
        logout_date TEXT
    )
''')

# Function to move image data to the "logoutdataset" folder and delete from source
def move_image_data(User_id):
    source_folder = 'dataset'  # Folder where all image data is currently stored
    target_folder = 'User_logoutdataset'  # Folder where image data will be moved

    # Ensure the target folder exists or create it
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # List all files in the source folder
    files = os.listdir(source_folder)

    for filename in files:
        if filename.startswith(User_id):
            source_path = os.path.join(source_folder, filename)
            target_path = os.path.join(target_folder, filename)
            
            # Move the image data to the "logoutdataset" folder
            os.rename(source_path, target_path)

# Function to move the employee record to the logout_records table and delete from source/admin_record
def move_employee_to_logout_records():
    # Get values from entry fields
    User_id = id_entry.get()
    first_name = first_name_entry.get()

    if not User_id or not first_name:
        messagebox.showerror("Error", "Both fields must be filled")
        return

    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get the current date and time

    # Check if the employee exists in employee_record by matching the id
    cursor.execute("SELECT * FROM UserRegistration_record WHERE User_id = ? AND first_name = ?", (User_id, first_name))
    employee_record = cursor.fetchone()

    if employee_record:
        # Move the image data to the "logoutdataset" folder and delete from source
        move_image_data(User_id)

        # Move the record from employee_record to logout_records and set the current date and time
        cursor.execute("INSERT INTO Userlogout_record (employee_id, first_name, last_name, email, password, mobile_number, address,  signature_image, registration_time, registration_date, logout_time, logout_date) VALUES (?, ?, ?, ?, ?, ?,  ?, ?, ?, ?, ?, ?)",
                       (employee_record[1], employee_record[2], employee_record[3], employee_record[4], employee_record[5], employee_record[6], employee_record[7], employee_record[8], employee_record[9], employee_record[10],  current_datetime, current_datetime))
        conn.commit()

        # Delete the record from employee_record
        cursor.execute("DELETE FROM UserRegistration_record WHERE User_id = ?", (User_id,))
        conn.commit()

        messagebox.showinfo("Success", "Record Moved to Logout Records and Images Deleted from Source Records")
        id_entry.delete(0, 'end')  # Clear the entry fields
        first_name_entry.delete(0, 'end')
    else:
        messagebox.showerror("Error", "Record not found in Source Records")

# Create a Tkinter window
window = tk.Tk()
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.title("User Log-Out")

# Load the background image
bg_image = Image.open("6.jpg")  # Replace with the path to your background image
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label for the background image
bg_label = tk.Label(window, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

Frame_registration1 = tk.Frame(window, bg="#2a6bac", borderwidth=2, relief="ridge", highlightbackground="sky blue", highlightcolor="sky blue")
Frame_registration1.place(x=0, y=0, width=1600, height=90)
subtitle = tk.Label(Frame_registration1, text="User Eliminate panel!", font=("impact", 35), fg="white", bg="#2a6bac", width=35)
subtitle.place(x=480, y=10)

# Create a frame in the center with a white background
frame = tk.Frame(window, bg="white", borderwidth=2, relief="ridge", highlightbackground="blue", highlightcolor="sky blue", height=470, width=470)
frame.place(x=880, y=200,)

admin_label2 = tk.Label(window, text="User Eliminate Here!", font=("impact", 30, "bold",), bg="white", fg="#2a6bac")
admin_label2.place(x=980, y=230)

# Create entry fields
id_label = tk.Label(window, text="User ID:", font=("goudy old style",18, "bold",), fg="#2a6bac", bg="white")
id_label.place(x=990, y=320)

id_entry = tk.Entry(window, width=23, font=("goudy old style", 20, "bold"), borderwidth=2, relief="ridge", highlightbackground="#2a6bac", highlightcolor="#2a6bac")
id_entry.place(x=990, y=355)

first_name_label = tk.Label(window, text="First Name:", font=("goudy old style", 18, "bold",), fg="#2a6bac", bg="white")
first_name_label.place(x=990, y=405)

first_name_entry = tk.Entry(window, font=("goudy old style", 20,"bold"), width=23, borderwidth=2, relief="ridge", highlightbackground="#2a6bac", highlightcolor="#2a6bac")
first_name_entry.place(x=990, y=435)

# Create a circular button
move_button = tk.Button(window, text="Logout", font=("goudy old style", 16, "bold"), fg="white", bg="#2a6bac", width=12, height=1, command=move_employee_to_logout_records, borderwidth=0, relief="solid")
move_button.place(x=990, y=510)

def open_main_file():
    window.withdraw() 
    subprocess.run(['python', 'admin.py'])

# Create a menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Create an Admin menu
admin_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Go Back", command=open_main_file)

window.mainloop()

# Close the database connection when done
conn.close()
