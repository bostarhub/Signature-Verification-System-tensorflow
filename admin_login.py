import tkinter as tk
from PIL import Image, ImageTk, ImageFilter, ImageEnhance
from tkinter import messagebox
import re
import sqlite3
import os
from datetime import datetime
import sys
import os
import subprocess

# Connect to the SQLite database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create the login_record table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Adminlogin_record (
        id INTEGER PRIMARY KEY,
        employee_id TEXT,
        admin_name TEXT,
        login_datetime DATETIME
    )
''')

# Function to check if a string is a valid password
def is_valid_password(password):
    return re.match(r'^[0-9]{6}$', password)

# Function to check if the entered username and password are valid and return employee_id
def validate_login(entered_username, entered_password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    first_name = entered_username.split()[0]
    cursor.execute("SELECT employee_id FROM AdminRegistration_record WHERE first_name = ? AND password = ?", (first_name, entered_password))
    result = cursor.fetchone()

    conn.close()
    return result[0] if result else None

# Function to insert login records into the login_record table
def insert_login_record(user_id, username, login_datetime):
    # Connect to the SQLite database
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Insert the login record into the login_record table
    cursor.execute("INSERT INTO Adminlogin_record (employee_id, admin_name, login_datetime) VALUES (?, ?, ?)",
                   (user_id, username, login_datetime))
    conn.commit()
    conn.close()
# Function to handle the login button click
def login():
    entered_username = entry_username.get()
    entered_password = entry_password.get()

    if not re.match("^[a-zA-Z ]+$", entered_username):
        messagebox.showerror("Login Failed", "Invalid username. Use only letters (a-z, A-Z) and space.")
    else:
        user_id = validate_login(entered_username, entered_password)
        if user_id is not None:
            try:
                current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Now that you have user_id, you can insert it into the login_record table
                insert_login_record(user_id, entered_username, current_datetime)

                # Display a successful login message
                messagebox.showinfo("Login Successful", "You have successfully logged in.")
                
                # Open the administration window
                open_administration_window()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            if not re.match(r'^[0-9]{6}$', entered_password):
                messagebox.showerror("Login Failed", "Invalid Password. Password must be 6 digits (0-9).")
            else:
                messagebox.showerror("Login Failed", "Invalid Username or Password.")

# Function to handle the "Forget Password" button click
def forget_password():
    username = entry_username.get()
    
    if not re.match("^[a-zA-Z ]+$", username):  # Allow space in the username
        messagebox.showerror("Forget Password Failed", "Invalid username. Use only letters (a-z, A-Z) and space.")
    else:
        # Create a new Toplevel window for password reset
        reset_password_window = tk.Toplevel(root)
        reset_password_window.title("Reset Password")
        reset_password_window.configure()  # Set background color
        
        # Set the initial size of the window
        reset_password_window.geometry("500x300")  # You can adjust the size as needed
        # Disable window resizing
        reset_password_window.resizable(0, 0)

        # Entry field for new password
        new_password_label = tk.Label(reset_password_window, text=f"Enter a new password:", font=("goudy old style", 18), fg="#5a46a7")
        new_password_label.pack(pady=20)
        
        new_password_entry = tk.Entry(reset_password_window, show='*', font=("goudy old style", 15))
        new_password_entry.pack(pady=20)
        
        # Button to update password
        update_password_button = tk.Button(reset_password_window, text="Update Password", command=lambda: update_password(username, new_password_entry.get()), padx=10, pady=10, font=("godey", 15, "bold"), bg="#5a46a7", fg="dark blue")
        update_password_button.pack(pady=20)
        
        def update_password(username, new_password):
            if new_password:
                # Update the password in the database
                conn = sqlite3.connect("database.db")
                cursor = conn.cursor()
                first_name = username.split()[0]
                cursor.execute("UPDATE Adminlogin_record SET password = ? WHERE admin_name = ?", (new_password, first_name))
                conn.commit()
                conn.close()
                messagebox.showinfo("Password Updated", "Password updated successfully!")
                reset_password_window.destroy()
            else:
                messagebox.showerror("Update Password Failed", "New password cannot be empty.")


                root.destroy()

# Function to open the administration.py script in a new window
def open_administration_window():
    root.withdraw()  # Hide the login window
    # Define the path to the administration.py script
    administration_script = "administration.py"

    # Check if the administration.py script exists
    if os.path.exists(administration_script):
        # Open the administration.py script in the new window
        os.system(sys.executable + " " + administration_script)
    else:
        messagebox.showerror("Error", "administration.py not found!")
def exit_application():
    result = messagebox.askquestion("Exit", "Are you sure you want to exit?", icon='warning')
    if result == 'yes':
        root.destroy()

root = tk.Tk()

# Background Image
# Set the background image
# root.bg = ImageTk.PhotoImage(file="1.png")
root.bg = ImageTk.PhotoImage(file="1.png")
root.bg_image = tk.Label(root, image=root.bg).place(x=0, y=0, relwidth=1, relheight=1)

# Set the heading label
root.txt = 'Welcome Login Here!'
root.heading = tk.Label(text=root.txt, font=("goudy old style", 50, "bold", "italic"), width=100,
                        fg="dark blue", bg="white", bd=4, relief=tk.GROOVE, highlightbackground="sky blue", highlightthickness=2)
root.heading.place(x=0, y=1, width=1590, height=100)

# Create and configure the login frame with a darker and thicker border
root.Frame_login = tk.Frame(root, bg="white", bd=4, relief=tk.GROOVE, highlightbackground="sky blue", highlightthickness=2)
root.Frame_login.place(x=880, y=200, width=450, height=480)

# Sign in
# root.sign_in_image = ImageTk.PhotoImage(file="2.png")
root.sign_in_image = ImageTk.PhotoImage(file="2.png")
root.sign_in_image_label = tk.Label(image=root.sign_in_image, bg="white")
root.sign_in_image_label.place(x=1050, y=210, width=90, height=90)

root.sign_in_label = tk.Label(text="Login In", fg="dark blue", bg="white", 
                              font=("goudy old style", 20, "bold"))
root.sign_in_label.place(x=1050, y=300)
# Username
label_username = tk.Label(root.Frame_login, text="Username", 
                          font=("Goudy old style", 16, "bold"), fg="dark blue", bg="white").place(x=90, y=140)  
entry_username = tk.Entry(root.Frame_login, highlightthickness=0, font=("Goudy old style", 16), bg="white")
entry_username.place(x=90, y=180, width=300)  
# Username icon
# root.username_icon = ImageTk.PhotoImage(file="3.png")
root.username_icon = ImageTk.PhotoImage(file="3.png")
root.username_icon_label = tk.Label(image=root.username_icon)
root.username_icon_label.place(x=920, y=385, width=30, height=30)
        
# Password
label_password = tk.Label(root.Frame_login, text="Password", font=("Goudy old style", 16, "bold"), fg="dark blue", bg="white").place(x=90,y=230)
     
entry_password = tk.Entry(root.Frame_login, highlightthickness=0, show="*", font=("Goudy old style", 16), bg="white")
entry_password.place(x=90, y=270, width=300)
        
# Password icon
# root.password_icon = ImageTk.PhotoImage(file="4.png")
root.password_icon = ImageTk.PhotoImage(file="4.png")
root.password_icon_label = tk.Label(image=root.password_icon)
root.password_icon_label.place(x=920, y=475, width=30, height=30)

# Button
submit = tk.Button(root.Frame_login, command=login, text="Login",
                   bd=0, font=("Goudy old style", 15, "bold"), bg="dark blue",
                   fg="white").place(x=90, y=370, width=160, height=40)
# Button
forget = tk.Button(root.Frame_login, text="Forget Password?", bd=0,
                   font=("Goudy old style", 13, "bold underline"),
                   fg="dark blue", bg="white", width=25, cursor="hand2", command=forget_password)
forget.place(x=20, y=300)

root.title("Admin Login page")

# Make the window fullscreen
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
 
# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create an Admin menu
admin_menu = tk.Menu(menu_bar, tearoff=0)

# Add the Admin menu to the menu bar
menu_bar.add_cascade(label="Exit", command=exit_application)

# root.mainloop()
root.mainloop()
