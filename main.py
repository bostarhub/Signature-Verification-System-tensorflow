import tkinter as tk
from PIL import Image, ImageTk
import os
import subprocess

class SplashScreen:
    def __init__(self, root):
        self.root = root
        self.welcome_shown = False
        self.create_splash_screen()

    def create_splash_screen(self):
        
        # Set the background color of the main window
        self.root.configure(bg='white')

        # Create a transparent overlay window
        self.splash_screen = tk.Toplevel(self.root)
        self.splash_screen.overrideredirect(True)
        self.splash_screen.attributes("-alpha", 1.0)
        self.splash_screen.attributes("-topmost", True)

        # Set the size of the splash screen to match the window size
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.splash_screen.geometry(f"{screen_width}x{screen_height}+0+0")

        # Load and display the image on the canvas
        # image_path = "11.png"  # Replace with the actual path to your image
        # self.image = ImageTk.PhotoImage(Image.open(image_path))
        image_path = "a.png"
        self.image = ImageTk.PhotoImage(Image.open(image_path))

        self.canvas = tk.Canvas(self.splash_screen, width=screen_width, height=screen_height, bg='white')
        self.canvas.pack()
        # Move the image a bit higher
        self.canvas.create_image(screen_width // 2, screen_height // 3 - 50, image=self.image)

        # Close button (cross)
        close_image_path = "close_icon.png"  # Replace with the actual path to your close icon image
        close_image = ImageTk.PhotoImage(Image.open(close_image_path).resize((20, 20)))
        close_button = tk.Button(self.splash_screen, image=close_image, command=self.close_splash_screen, bg='white', bd=0)
        close_button.image = close_image
        close_button.place(x=screen_width - 30, y=10)  # Adjust the position as needed

        # After 2 seconds, show the "Welcome" text
        self.splash_screen.after(2000, self.show_welcome)

    def show_welcome(self):
        # Display the "Welcome" text
        welcome_text = self.canvas.create_text(
            self.root.winfo_screenwidth() // 2,
            self.root.winfo_screenheight() // 2,
            text="Welcome",
            font=("impact", 30),
            fill="#90caf9"
        )
        self.welcome_shown = True  # Set the flag to True

        # After 2 seconds, hide the "Welcome" text and show the "Signature Verification System"
        self.splash_screen.after(2000, lambda: self.hide_text(welcome_text, self.show_verification_system))

    def hide_text(self, text_id, callback):
        self.canvas.itemconfig(text_id, state='hidden')
        callback()

    def show_verification_system(self):
        if not self.welcome_shown:
            # Only proceed if the welcome text has been shown
            return

        # Display the "Signature Verification System" text
        self.canvas.create_text(
            self.root.winfo_screenwidth() // 2,
            self.root.winfo_screenheight() // 2 + 70,  # Adjusted Y-coordinate
            text="Signature Verification System",
            font=("impact", 30),
            fill="#90caf9"
        )

        # After 2 seconds, close the splash screen and open admin_login.py
        self.splash_screen.after(2000, self.close_splash_screen)

    def close_splash_screen(self):
        self.splash_screen.withdraw()  # Withdraw the window (hide it)
        self.root.deiconify()  # Show the main window

        # Open the admin_login.py file or perform any other desired action
        os.system("python admin_login.py")
        # os.system("admin_login.py")


class AdminLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Login.py")

        # Your admin login window content goes here

        # Add a back button to return to the splash screen
        back_button = tk.Button(root, text="Back to Splash Screen", command=self.back_to_splash)
        back_button.pack()

    def back_to_splash(self):
        self.root.withdraw()  # Withdraw the window (hide it)
        splash_screen = SplashScreen(self.root)  # Re-create the splash screen
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Splash Screen Example")

    # Set the window size and position
    root.attributes("-fullscreen", True)

    # Create the splash screen
    Splash = SplashScreen(root)
    root.mainloop()
