import tkinter as tk
from PIL import Image, ImageTk
import os
import sys
from tkinter import messagebox
import subprocess
def open_employee_registration():
    root.withdraw() 
    os.system(sys.executable + " employee_registration.py")
    root.destroy()

def open_user_registration():
    root.withdraw() 
    os.system(sys.executable + " user_registration.py")
    root.destroy()

def open_traning():
    root.withdraw() 
    os.system(sys.executable + " train.py")
    root.destroy()

def open_eliminate():
    root.withdraw() 
    os.system(sys.executable + " eliminate.py")
    root.destroy()

def open_terminate():
    root.withdraw() 
    os.system(sys.executable + " terminate.py")
    root.destroy()

root = tk.Tk()
root.title("Administration")

# Make the window fullscreen
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# Load the background image
bg_image = Image.open("7.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

Frame_registration1 = tk.Frame(root, bg="sky blue", borderwidth=2, relief="ridge", highlightbackground="dark blue", highlightcolor="dark blue")
Frame_registration1.place(x=0, y=0, width=1590, height=90)
subtitle = tk.Label(Frame_registration1, text="Admin Panel!", font=("impact", 35 ), fg="white", bg="SKY BLUE")
subtitle.place(x=600, y=10)

Frame_admin = tk.Frame(root, bg="sky blue", borderwidth=2, relief="ridge", highlightbackground="purple", highlightcolor="purple")
Frame_admin.place(x=160, y=150, width=480, height=550)

    # Load the second image
image2 = Image.open("10.jpg")
photo2 = ImageTk.PhotoImage(image2)

    # Create and add a label to display the second image with a transparent background
image_label2 = tk.Label(root, image=photo2)
image_label2.place(x=163, y=152)

# Create a button for employee registration
registration_button = tk.Button(Frame_admin, text="Register new user", font=("goudy old style", 20, "bold"), width=15, fg="black", bg="white", command=open_user_registration)
registration_button.place(x=120, y=290)

# Create a button for employee login
login_button = tk.Button(Frame_admin, text="Traning", font=("goudy old style", 20, "bold"), width=15, fg="black", bg="white", command=open_traning)
login_button.place(x=120, y=390)

# Create a button for employee login
login_button = tk.Button(Frame_admin, text="Eliminating", font=("goudy old style", 20, "bold"), width=15, fg="black", bg="white", command=open_eliminate)
login_button.place(x=120, y=490)

Frame_admin = tk.Frame(root, bg="sky blue", borderwidth=2, relief="ridge", highlightbackground="purple", highlightcolor="purple")
Frame_admin.place(x=920, y=150, width=480, height=550)

    # Load the second image
image1 = Image.open("9.jpg")
photo1 = ImageTk.PhotoImage(image1)

    # Create and add a label to display the second image with a transparent background
image_label1 = tk.Label(root, image=photo1)
image_label1.place(x=923, y=152)

# Create a button for employee registration
registration_button = tk.Button(root, text="Recruitment", font=("goudy old style", 20, "bold"), width=15, fg="black", bg="white", command=open_employee_registration)
registration_button.place(x=1050, y=450)

# Create a button for employee login
login_button = tk.Button(root, text="Terminating", font=("goudy old style", 20, "bold"), width=15, fg="black", bg="white", command=open_terminate)
login_button.place(x=1050, y=550)


def open_main_file():
    root.withdraw() 
    subprocess.run(['python', 'administration.py'])

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create an Admin menu
admin_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="back", command=open_main_file)

root.mainloop()
