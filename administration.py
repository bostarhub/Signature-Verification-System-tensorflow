import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import sys
import subprocess

class SignatureVerificationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Signature Verification")
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

        # Create a frame with sky-blue background color
        self.top_frame = tk.Frame(root, bg="sky blue", height=150)
        self.top_frame.pack(fill=tk.X)

        # Add a label to the left side of the top frame
        self.label = tk.Label(self.top_frame, text="Signature Verification System", font=("impact", 40,), bg="sky blue", fg="white", padx=10, pady=10)
        self.label.pack(side=tk.LEFT)

        # Add clickable text labels to the right side of the top frame
        self.exit_label = tk.Label(self.top_frame, text="Exit", font=("Helvetica", 12), bg="sky blue", fg="white", padx=10, pady=10, cursor="hand2")
        self.exit_label.pack(side=tk.RIGHT)
        self.exit_label.bind("<Enter>", lambda event: self.on_hover(event, "exit"))
        self.exit_label.bind("<Leave>", lambda event: self.on_leave(event, "exit"))
        self.exit_label.bind("<Button-1>", self.exit_application)

        self.logout_label = tk.Label(self.top_frame, text="Logout", font=("Helvetica", 12), bg="sky blue", fg="white", padx=10, pady=10, cursor="hand2")
        self.logout_label.pack(side=tk.RIGHT)
        self.logout_label.bind("<Enter>", lambda event: self.on_hover(event, "logout"))
        self.logout_label.bind("<Leave>", lambda event: self.on_leave(event, "logout"))
        self.logout_label.bind("<Button-1>", self.open_login_file)
        
        self.help_label = tk.Label(self.top_frame, text="Help", font=("Helvetica", 12), bg="sky blue", fg="white", padx=10, pady=10, cursor="hand2")
        self.help_label.pack(side=tk.RIGHT)
        self.help_label.bind("<Enter>", lambda event: self.on_hover(event, "help"))
        self.help_label.bind("<Leave>", lambda event: self.on_leave(event, "help"))
        self.help_label.bind("<Button-1>", self.show_help)

        self.about_label = tk.Label(self.top_frame, text="About", font=("Helvetica", 12), bg="sky blue", fg="white", padx=10, pady=10, cursor="hand2")
        self.about_label.pack(side=tk.RIGHT)
        self.about_label.bind("<Enter>", lambda event: self.on_hover(event, "about"))
        self.about_label.bind("<Leave>", lambda event: self.on_leave(event, "about"))
        self.about_label.bind("<Button-1>", self.show_about)

        # Add an image frame below the top frame
        self.image_frame = tk.Frame(root, bg="white", height=500)
        self.image_frame.pack(fill=tk.BOTH, expand=True)

        # Load and display the first image on the canvas
        image_path1 = "19.jpg"  # Replace with the actual path to your image
        self.image1 = ImageTk.PhotoImage(Image.open(image_path1))
        self.canvas1 = tk.Canvas(self.image_frame, width=self.root.winfo_screenwidth(), height=500, bg="white")
        self.canvas1.pack(fill=tk.BOTH, expand=True)
        self.canvas1.create_image(self.root.winfo_screenwidth() // 2, 200, image=self.image1)

        # Load and display the second image
        image_path2 = "22.jpg"  # Replace with the actual path to your second image
        self.image2 = ImageTk.PhotoImage(Image.open(image_path2))
        self.image_label2 = tk.Label(self.image_frame, image=self.image2, bg="white")
        self.image_label2.place(x=350, y=320)

        # Load and display the third image
        image_path3 = "21.jpg"  # Replace with the actual path to your third image
        self.image3 = ImageTk.PhotoImage(Image.open(image_path3))
        self.image_label3 = tk.Label(self.image_frame, image=self.image3, bg="white")
        self.image_label3.place(x=930, y=320)

        # Add buttons for signature verification and admin page
        button_font = ("old godey", 20, "bold")
        signature_verification_button = tk.Button(self.image_frame, text="Signature Verification", command=self.show_signature_verification, font=button_font, width="18", height="1", bg="sky blue", fg="white")
        signature_verification_button.place(x=350, y=550)

        admin_page_button = tk.Button(self.image_frame, text="Admin Page   ", command=self.show_admin_page , font=button_font, width="17", height="1", bg="sky blue", fg="white")
        admin_page_button.place(x=930, y=550)

    def on_hover(self, event, label_type):
        # Change color on hover
        if label_type == "help":
            self.help_label.config(fg="red")
        elif label_type == "about":
            self.about_label.config(fg="red")
        elif label_type == "logout":
            self.logout_label.config(fg="red")
        elif label_type == "exit":
            self.exit_label.config(fg="red")
        

    def on_leave(self, event, label_type):
        # Restore original color on leave
        if label_type == "help":
            self.help_label.config(fg="dark blue")
        elif label_type == "about":
            self.about_label.config(fg="dark blue")
        elif label_type == "logout":
            self.logout_label.config(fg="dark blue")
        elif label_type == "exit":
            self.exit_label.config(fg="dark blue")

    def exit_application(self, event):
        root.withdraw() 
        # Close the entire application
        self.root.destroy()

    def show_help(self, event):
        root.withdraw() 
        # Open the help.py file or perform any other desired action
        os.system(sys.executable + " help.py")

    def show_about(self, event):
        root.withdraw() 
        # Open the about.py file or perform any other desired action
        os.system(sys.executable + " about.py")

    def show_signature_verification(self):
        root.withdraw() 
        # Open the signature_verification.py file or perform any other desired action
        os.system(sys.executable + " signatureverification.py")

    def show_admin_page(self):
        root.withdraw() 
        # Open the admin.py file or perform any other desired action
        os.system(sys.executable + " admin.py")

    def open_login_file(self, event=None):
        root.withdraw() 
    # Open the admin_login.py file or perform any other desired action
        os.system(sys.executable + "  admin_login.py")

if __name__ == "__main__":
    root = tk.Tk()
    app = SignatureVerificationApp(root)
    root.mainloop()
