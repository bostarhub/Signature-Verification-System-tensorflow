import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser
import subprocess

# Create a Tkinter window
root = tk.Tk()
root.title("Help")

# Function to open a new window
def open_window(window_title):
    new_window = tk.Toplevel(root)
    new_window.title(window_title)
  
# Function to open the main Python file
def open_main_file():
    root.withdraw()
    import subprocess
    subprocess.Popen(['python', 'administration.py'])  # Replace 'main.py' with your main Python file name

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Go Back", command=open_main_file)

# Create a canvas to enable scrolling
canvas = tk.Canvas(root)
canvas.pack(side="left", fill="both", expand=True)

# Add a vertical scrollbar
vsb = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
vsb.pack(side="right", fill="y")
canvas.configure(yscrollcommand=vsb.set)

# Create a frame inside the canvas to hold the content
content_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Load the image
image1 = Image.open("19.jpg")
photo1 = ImageTk.PhotoImage(image1)

# Create and add a label to display the image with a transparent background
image_label1 = tk.Label(content_frame, image=photo1)
image_label1.image = photo1  # Keep a reference to the image
image_label1.pack()

# Add text on top of the image using label widgets
text_label1 = tk.Label(content_frame, text="                                      Signature Verification System                                                ", font=("impact", 35),  fg="dark blue")
text_label1.pack()

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="Introduction", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "Leveraging Convolutional Neural Networks (CNNs) in Python, modern signature verification systems present an advanced solution for biometric authentication, particularly crucial in secure banking environments. By harnessing CNNs' capability to discern intricate patterns and variations within handwritten signatures, these systems enhance accuracy, ensuring robust user verification. The integration of diverse datasets and hierarchical feature learning enables effective differentiation between authentic and forged signatures. This technology not only boosts accuracy but also adapts to various writing styles, providing a secure and versatile solution for user identification in banking applications, contributing significantly to fraud prevention and ensuring the integrity of financial transactions."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="Login", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "In the initial phase, an individual, whether an admin or an employee recently hired by the company, is required to perform a self-authorization process by logging into the system. During the registration phase, the user provides a personalized username and password. Subsequently, to gain access to the system, the user must log in using the specified credentials. This login procedure acts as the primary gatekeeper, ensuring that only authorized personnel can proceed further within the system. Once successfully authenticated, the individual gains the necessary clearance to perform their designated tasks and responsibilities within the system. This two-step authentication process adds an extra layer of security, ensuring that only approved users can engage with the system's functionalities."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Load the image you want to add below the paragraph
image_below_paragraph = Image.open("6.png")
image_below_paragraph_photo = ImageTk.PhotoImage(image_below_paragraph)

# Create and add a label to display the image with a transparent background
image_below_paragraph_label = tk.Label(content_frame, image=image_below_paragraph_photo)
image_below_paragraph_label.image = image_below_paragraph_photo  # Keep a reference to the image
image_below_paragraph_label.pack(pady=20)

overview_heading = tk.Label(content_frame, text="Administration Page", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left


# Add paragraphs manually using label widgets
paragraph2 = "Upon successful login by an employee, the system proceeds to authenticate the employee's status as an administrator. Following this, a new window is triggered, presenting the user with options based on their designated role. If the employee intends to perform signature verification tasks, they can seamlessly navigate to the signature verification screen by clicking on the designated button. Additionally, if the user wishes to configure system settings, such as adding new users, training the system, or making adjustments, they can effortlessly navigate to the admin window. This two-tiered approach streamlines the user experience, allowing for straightforward access to both signature verification and system configuration functionalities, enhancing overall usability and efficiency."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Load the image you want to add below the paragraph
image_below_paragraph = Image.open("7.png")
image_below_paragraph_photo = ImageTk.PhotoImage(image_below_paragraph)

# Create and add a label to display the image with a transparent background
image_below_paragraph_label = tk.Label(content_frame, image=image_below_paragraph_photo)
image_below_paragraph_label.image = image_below_paragraph_photo  # Keep a reference to the image
image_below_paragraph_label.pack(pady=20)


overview_heading = tk.Label(content_frame, text="Profile Hub", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "In the context of the signature verification software, the Profile Hub facilitates a multitude of functionalities tailored to the needs of the banking sector. This versatile software allows users to seamlessly execute signature verification tasks, including the addition and deletion of user profiles. Within the banking environment, it extends its utility to encompass critical processes such as employee onboarding, recruitment, and termination. Users can efficiently manage employee profiles by selecting a specific individual and then proceeding to perform distinct functions through dedicated forms. This integrated approach ensures the software aligns with the stringent security requirements and operational demands of the banking industry, offering a robust solution for comprehensive user and profile management."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")


# Load the image you want to add below the paragraph
#image_below_paragraph = Image.open("8.png")
#image_below_paragraph_photo = ImageTk.PhotoImage(image_below_paragraph)

# Create and add a label to display the image with a transparent background
#image_below_paragraph_label = tk.Label(content_frame, image=image_below_paragraph_photo)
#image_below_paragraph_label.image = image_below_paragraph_photo  # Keep a reference to the image
#image_below_paragraph_label.pack(pady=20)

overview_heading = tk.Label(content_frame, text="Register New User", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "In a banking environment, the administrator takes charge of the user registration process. New users provide their personal details, including name, address, phone number, and email. The administrator guides them in submitting a secure signature image, stored in a dedicated folder linked to their profile. Simultaneously, comprehensive user data is recorded and stored in the system's database. This streamlined process ensures efficient onboarding and facilitates subsequent signature verification and system interactions."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")


# Load the image you want to add below the paragraph
image_below_paragraph = Image.open("9.png")
image_below_paragraph_photo = ImageTk.PhotoImage(image_below_paragraph)

# Create and add a label to display the image with a transparent background
image_below_paragraph_label = tk.Label(content_frame, image=image_below_paragraph_photo)
image_below_paragraph_label.image = image_below_paragraph_photo  # Keep a reference to the image
image_below_paragraph_label.pack(pady=20)


overview_heading = tk.Label(content_frame, text="Traning", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "Within the Profile Hub, a specialized training function exists. By clicking the Training button, the system engages in training the signature images of newly registered bank account users. This training employs Python and a CNN model in deep learning. The purpose is to refine the system's ability to accurately verify signatures, enhancing security and precision in banking transactions."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

overview_heading = tk.Label(content_frame, text="Eliminate", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "In the Profile Hub, the administrator possesses the ability to eliminate or terminate any user account, whether initiated through the bank or the system. This streamlined process enables efficient management of user accounts, allowing for swift responses to account closure requests."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")


# Load the image you want to add below the paragraph
#image_below_paragraph = Image.open("10.png")
#image_below_paragraph_photo = ImageTk.PhotoImage(image_below_paragraph)

# Create and add a label to display the image with a transparent background
#image_below_paragraph_label = tk.Label(content_frame, image=image_below_paragraph_photo)
#image_below_paragraph_label.image = image_below_paragraph_photo  # Keep a reference to the image
#image_below_paragraph_label.pack(pady=20)


overview_heading = tk.Label(content_frame, text="Recruitment", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "In the employee profiling section, the administrator can effortlessly add new employees, accommodating both those entering the system for the first time and individuals newly recruited by the bank. This streamlined process ensures quick onboarding and access to the system's full functionality, allowing for efficient management of employee profiles in response to the bank's evolving needs."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")


# Load the image you want to add below the paragraph
#image_below_paragraph = Image.open("8.png")
#image_below_paragraph_photo = ImageTk.PhotoImage(image_below_paragraph)

# Create and add a label to display the image with a transparent background
#image_below_paragraph_label = tk.Label(content_frame, image=image_below_paragraph_photo)
#image_below_paragraph_label.image = image_below_paragraph_photo  # Keep a reference to the image
#image_below_paragraph_label.pack(pady=20)


overview_heading = tk.Label(content_frame, text="Terminate", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "To initiate the termination process for an employee, the administrator provides the employee's identification details, including their unique employee ID and name. This input triggers the termination procedure, ensuring a systematic and controlled cessation of the individual's association with the bank. The inclusion of such information streamlines the termination workflow, adding a layer of precision to the administrative functions."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")


# Load the image you want to add below the paragraph
#image_below_paragraph = Image.open("12.png")
#image_below_paragraph_photo = ImageTk.PhotoImage(image_below_paragraph)

# Create and add a label to display the image with a transparent background
#image_below_paragraph_label = tk.Label(content_frame, image=image_below_paragraph_photo)
##image_below_paragraph_label.pack(pady=20)

# Create a frame with a colored background for the content below the main text
extra_content_frame = tk.Frame(content_frame, bg="sky blue", width=1400, height=300)
extra_content_frame.pack(pady=0, anchor="w")


# Load the second image
image1 = Image.open("youtube.png")
image1_photo = ImageTk.PhotoImage(image1)

# Create a label for the second image and adjust its position
image_label2 = tk.Label(extra_content_frame, image=image1_photo, bg="#0b2838")
image_label2.image = image1_photo
image_label2.place(x=170, y=105)  # Adjust the coordinates as needed


# Load the second image
image2 = Image.open("instagram.png")
image2_photo = ImageTk.PhotoImage(image2)

# Create a label for the second image and adjust its position
image_label2 = tk.Label(extra_content_frame, image=image2_photo, bg="#0b2838")
image_label2.image = image2_photo
image_label2.place(x=420, y=105)  # Adjust the coordinates as needed

# Load the third image
image3 = Image.open("facebook.png")
image3_photo = ImageTk.PhotoImage(image3)

# Create a label for the third image and adjust its position
image_label3 = tk.Label(extra_content_frame, image=image3_photo, bg="#0b2838")
image_label3.image = image3_photo
image_label3.place(x=660, y=105)  # Adjust the coordinates as needed

# Load the third image
image3 = Image.open("call.png")
image3_photo = ImageTk.PhotoImage(image3)

# Create a label for the third image and adjust its position
image_label3 = tk.Label(extra_content_frame, image=image3_photo, bg="#0b2838")
image_label3.image = image3_photo
image_label3.place(x=950, y=105)  # Adjust the coordinates as needed



def open_youtube():
    webbrowser.open("https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiO0dvq4v2CAxUP2wIHHR9ADjEQtwJ6BAgWEAI&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DSfCab_QAwgY&usg=AOvVaw0mIXbu4RhyzpRbQMxkHx9a&opi=89978449")  # Replace with the desired Facebook URL

# Create a label with a colored background that represents the Facebook link
facebook_link_label = tk.Label(content_frame, text="https://www.youtube.com", fg="white", bg="sky blue", cursor="hand2")
facebook_link_label.place(x=200, y=4140)

# Bind the click event to open the Facebook link
facebook_link_label.bind("<Button-1>", lambda event: open_youtube())

def open_instagram():
    webbrowser.open("https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwii6q2X5P2CAxWq2QIHHXwUDCcQwqsBegQIDRAG&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DCChuwRS06Zs&usg=AOvVaw0nZdWSCeqgCZEQlgqGqXPs&opi=89978449")  # Replace with the desired Facebook URL

# Create a label with a colored background that represents the Facebook link
facebook_link_label = tk.Label(content_frame, text="https://www.instagram.com", fg="white", bg="sky blue", cursor="hand2")
facebook_link_label.place(x=450, y=4140)

# Bind the click event to open the Facebook link
facebook_link_label.bind("<Button-1>", lambda event: open_instagram())

def open_facebook():
    webbrowser.open("https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiIz76u5P2CAxXj0wIHHY7AApQQFnoECCoQAQ&url=https%3A%2F%2Fwww.entrust.com%2Fblog%2F2020%2F05%2Fvideo-verification-for-document-signing%2F&usg=AOvVaw2J_mixvVgdAZI6D2jBzk_K&opi=89978449")  # Replace with the desired Facebook URL

# Create a label with a colored background that represents the Facebook link
facebook_link_label = tk.Label(content_frame, text="https://www.facebook.com", fg="white", bg="sky blue", cursor="hand2")
facebook_link_label.place(x=700, y=4140)

# Bind the click event to open the Facebook link
facebook_link_label.bind("<Button-1>", lambda event: open_facebook())

# Create a label with a colored background that represents the Facebook link
facebook_link_label = tk.Label(content_frame, text="03427960776", fg="white", bg="sky blue")
facebook_link_label.place(x=1000, y=4140)


# Create a label with a colored background that represents the Facebook link
facebook_link_label = tk.Label(content_frame, text="Contact Us", fg="white", bg="sky blue", font=("impact", 50))
facebook_link_label.place(x=50, y=4040)

# Make the window fullscreen
root.geometry("{0}x{0}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

root.update_idletasks()  # Update the window idle tasks to properly set the canvas size
canvas.config(scrollregion=canvas.bbox("all"))  # Set the scroll region based on the canvas content

root.mainloop()