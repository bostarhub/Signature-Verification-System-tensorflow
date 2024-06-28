import cv2
import numpy as np
from tkinter import font, filedialog, messagebox
from PIL import Image, ImageTk
import tkinter as tk
#from tensorflow.keras.models import load_model
from tensorflow.keras.models import load_model

import subprocess
# Load the trained model
model_path = 'final_model.h5'
loaded_model = load_model(model_path)


# Function to preprocess the input image
def preprocess_image(image_path, target_size=(128, 128)):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
    img = cv2.resize(img, target_size)
    img = img / 255.0  # Normalize pixel values to be between 0 and 1
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

# Function to classify an image
def classify_image(img, model):
    preprocessed_img = cv2.resize(img, (128, 128))
    preprocessed_img = preprocessed_img / 255.0  # Normalize pixel values to be between 0 and 1
    preprocessed_img = np.expand_dims(preprocessed_img, axis=0)  # Add batch dimension
    raw_prediction = model.predict(preprocessed_img)
    prediction_value = raw_prediction[0][0]
    class_label = 'Genuine' if prediction_value >= 0.3 else 'Forged'
    return prediction_value, raw_prediction, class_label

class SignatureVerificationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Signature Verification System")

        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

        # Background Image
        self.bg = ImageTk.PhotoImage(file="20.jpg")
        self.bg_image = tk.Label(image=self.bg)
        self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)

        # Use Old Goudy style font
        custom_font = font.Font(family="Old Goudy", size=30, weight="bold")

        # Create the first frame
        self.frame1 = tk.Frame(root, bg='#3498db', padx=10, pady=10)
        self.frame1.pack(padx=20, pady=20, anchor='n', fill='x', expand=True)

        # You can add other widgets or text here for the title area
        title_label = tk.Label(self.frame1, text="Signature Verification System", font=custom_font, bg='#3498db', fg='white')
        title_label.pack(pady=20)

        # Create the third frame below the first one
        self.frame3 = tk.Frame(root, width=300, height=250, bd=2, relief='groove', bg="white")  # Set background color
        self.frame3.place(x=960, y=300)

        # Create the second frame below the first one
        self.frame2 = tk.Frame(root, width=300, height=250, bd=2, relief='groove', bg="white")
        self.frame2.place(x=310, y=300)

        # Create "Load Signature Image" button below frame 1
        load_button = tk.Button(self.root, text="Load Signature Image", font=("Old Goudy", 20), width="18", command=self.load_signature_image, bg='#3498db', fg='white')  # Set background and text color
        load_button.place(x=310, y=580)

        # Create "Verify Signature" button below frame 2
        verify_button = tk.Button(self.root, text="Verify Signature", width="18", font=("Old Goudy", 20),bg='#3498db', fg='white', command=self.verify_signature)
        verify_button.place(x=960, y=580)

        # Placeholder for the image label in frame2
        self.image_label = None
        self.loaded_image = None  # To store the loaded image

        # Placeholder for the result label in frame3
        self.result_label = None
       
 # Create a menu bar
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        # Create an Admin menu
        admin_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Go Back", command=self.open_main_file)

    def open_main_file(self):
        self.root.withdraw()
        subprocess.run(['python', 'administration.py'])    
     

    def load_signature_image(self):
        file_path = filedialog.askopenfilename(title="Select Signature Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        if file_path:
            # Load the image
            self.loaded_image = cv2.imread(file_path)
            self.loaded_image = cv2.cvtColor(self.loaded_image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
            self.loaded_image = cv2.resize(self.loaded_image, (300, 200))  # Resize the image to fit in frame2

            # Display the image in frame2
            photo = ImageTk.PhotoImage(Image.fromarray(self.loaded_image))
            if self.image_label:
              self.image_label.destroy()
            self.image_label = tk.Label(self.frame2, image=photo)
            self.image_label.image = photo  # To prevent the image from being garbage collected
            self.image_label.grid(row=0, column=0)

    def verify_signature(self):
        if self.image_label and self.loaded_image is not None:
            # Classify the loaded image using the trained model
            prediction_value, raw_prediction, class_label = classify_image(self.loaded_image, loaded_model)

            # Destroy the previous result label in frame3
            if self.result_label:
                self.result_label.destroy()

            # Display the result in frame3
            self.result_label = tk.Label(self.frame3, text=f"Result: {class_label} ", font=("Old Goudy", 13))  # Set background and text color
            self.result_label.grid(row=0, column=0)

            # Disable automatic resizing of frame2 and frame3
            self.frame2.grid_propagate(False)
            self.frame3.grid_propagate(False)

            # Configure frame2 to have a fixed size
            self.frame2.configure(width=300, height=200)
        else:
            # Show a message box if no image is loaded
            messagebox.showinfo("Error", "Please load a signature image first.")


            
if __name__ == "__main__":
    root = tk.Tk()
    app = SignatureVerificationApp(root)
    root.mainloop()
