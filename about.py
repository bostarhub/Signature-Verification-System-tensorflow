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

def open_main_file():
    root.withdraw()
    subprocess.Popen(['python', 'administration.py'])  # Replace 'admin.py' with your admin Python file name

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Go Back", command=open_main_file )


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
image1 = Image.open("12.jpg")
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
paragraph2 = "In a world which is progressing towards innovation, signature actually assumes the most crucial part in ID of a specific individual. As years cruise by, instances of phony is likewise expanding in an incredible number. Hence, signature check framework is request of an opportunity to further develop the confirmationinteraction and give secure means to approval of authoritative archives. The mark confirmation frameworks help to separate between the first and phony marks.This section presents data about advancements utilized in project that are Image Processing and Convolutional Neural Network."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="Image Processing", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "Image processing is is a strategy to play out certain procedure on a picture, to get an improved picture or to extricate some valuable data from it."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="Artficial Neural Network", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "Artificial Neural Network is an endeavor to reproduce the organization of neurons that make up a human so the PC will actually want to learn things and settle on choices in a humanlike way."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="Convolutional Neural Network", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "A convolutional neural organization (CNN) is a kind of counterfeit neural organization utilized in picture acknowledgment and handling that is explicitly intended to deal with pixel information."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Add a heading for the "Overview" paragraph
overview_heading = tk.Label(content_frame, text="What are we constructing?", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "We are developing a system that processes image data for signature verification. Utilizing advanced techniques, particularly Convolutional Neural Networks (CNNs), the system analyzes the input image to determine the authenticity of the signature. The outcome is a conclusive result indicating whether the signature is genuine or forged. This application of CNNs enhances the accuracy and reliability of the signature verification process."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Load the image you want to add below the paragraph
image_below_paragraph = Image.open("13.png")
image_below_paragraph_photo = ImageTk.PhotoImage(image_below_paragraph)

# Create and add a label to display the image with a transparent background
image_below_paragraph_label = tk.Label(content_frame, image=image_below_paragraph_photo)
image_below_paragraph_label.image = image_below_paragraph_photo  # Keep a reference to the image
image_below_paragraph_label.pack(pady=20)

overview_heading = tk.Label(content_frame, text="Feature Extraction Results", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left


# Add paragraphs manually using label widgets
paragraph2 = "During the training phase, our system engages in a comprehensive feature extraction process on the provided image dataset. This involves extracting meaningful features from the images, a crucial step in enhancing the model's understanding of signature patterns. Utilizing a dataset comprising 50 sets, the system meticulously trains, continually refining its accuracy and learning to distinguish between genuine and forged signatures. Within our dataset, two meticulously curated folders dedicated to forged and genuine signatures respectively serve as the foundation for training our model. These folders enable the model to discern the subtle nuances between authentic and fraudulent signatures, ensuring its robustness and effectiveness in real-world scenarios."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

# Load the image you want to add below the paragraph
image_below_paragraph = Image.open("14.png")
image_below_paragraph_photo = ImageTk.PhotoImage(image_below_paragraph)

# Create and add a label to display the image with a transparent background
image_below_paragraph_label = tk.Label(content_frame, image=image_below_paragraph_photo)
image_below_paragraph_label.image = image_below_paragraph_photo  # Keep a reference to the image
image_below_paragraph_label.pack(pady=20)


overview_heading = tk.Label(content_frame, text="IMPLEMENTATIONS", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "The analysis is done by using various steps :"
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

overview_heading = tk.Label(content_frame, text="1.Data Acquisition:", font=("impact", 30), fg="grey", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "We collect handwritten signatures, along with associated identifying characteristics, to construct an extensive database for each individual. This unified database comprises the signatures of all participants, serving as a vital resource to evaluate the effectiveness of our signature verification system. It facilitates the comparison of results obtained through diverse methodologies applied to the same comprehensive dataset. In this database, we store signature images and utilize them for training the model, ensuring a robust and well-informed signature verification system."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")


# Load the image you want to add below the paragraph
image_below_paragraph = Image.open("15.png")
image_below_paragraph_photo = ImageTk.PhotoImage(image_below_paragraph)

# Create and add a label to display the image with a transparent background
image_below_paragraph_label = tk.Label(content_frame, image=image_below_paragraph_photo)
image_below_paragraph_label.image = image_below_paragraph_photo  # Keep a reference to the image
image_below_paragraph_label.pack(pady=20)

overview_heading = tk.Label(content_frame, text="2.Pre-Processing and resizing: ", font=("impact", 30), fg="grey", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "In the beginning, the image is resized to the appropriate size. Pre-processing is then carried out in accordance with the outcomes. No matter the size or slant supplied for the signature, the system must be able to retain good performance. The system's insensitivity is crucial since it will make it possible to correctthe signature image."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")


overview_heading = tk.Label(content_frame, text="3.Training Model:", font=("impact", 30), fg="grey", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "The system's insensitivity is essential since it will allow the signature image to be fixed. To build CNN, We merge the TensorFlow backend with the Keras library. We train the model and evaluate its performance after loading the pre-processed picture directories."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")


# Load the image you want to add below the paragraph
image_below_paragraph = Image.open("16.png")
image_below_paragraph_photo = ImageTk.PhotoImage(image_below_paragraph)

# Create and add a label to display the image with a transparent background
image_below_paragraph_label = tk.Label(content_frame, image=image_below_paragraph_photo)
image_below_paragraph_label.image = image_below_paragraph_photo  # Keep a reference to the image
image_below_paragraph_label.pack(pady=20)

overview_heading = tk.Label(content_frame, text="4.Implementation:", font=("impact", 30), fg="grey", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "The Keras Python library has access to the file directory structure holding the signature images utilised in this investigation. The CNN was then created in Python using Keras and the TensorFlow backend to learn the patterns related to the signatures. The next stage in assessing whether the model was appropriate for the data was to test the model's precision and loss metrics. A signature from a holdout set was utilised as the evaluation tool to assess the accuracy of the model's predictions"
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")



overview_heading = tk.Label(content_frame, text="5.Validation: ", font=("impact", 30), fg="grey", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "To verify the model's effectiveness, the predictions are contrasted with the ground truth, which is the signature's real validity."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")

overview_heading = tk.Label(content_frame, text="RESULTS", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "The CNN model's ability to discriminate between valid and invalid signatures from a bigger set without bias was evaluated using a smaller sample of signatures. The dataset was composed of 50 people were chosen at random. To investigate the effects of data augmentation on the generalization of the model and overall performance, a range of signatures with augmented data were utilized during training. To contrast the performance of genuine data vs. enhanced data during training, two unique sets with differing amounts of real signatures were used. The addition of data was also used. TenserFlow is used in this project because it produces the most accurate results for the input signatures that are provided."
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")


# Load the image you want to add below the paragraph
image_below_paragraph = Image.open("18.png")
image_below_paragraph_photo = ImageTk.PhotoImage(image_below_paragraph)

# Create and add a label to display the image with a transparent background
image_below_paragraph_label = tk.Label(content_frame, image=image_below_paragraph_photo)
image_below_paragraph_label.image = image_below_paragraph_photo  # Keep a reference to the image
image_below_paragraph_label.pack(pady=20)


overview_heading = tk.Label(content_frame, text="CONCLUSION", font=("impact", 30), fg="black", justify="left", wraplength=800)
overview_heading.pack(pady=20, anchor="w")  # Set anchor to "w" (west) to align it to the left

# Add paragraphs manually using label widgets
paragraph2 = "Here, a writer-independent strategy is used to train the CNN, and a writer-dependent approach makes use of this trained CNN to extract features from offline signatures. The findings show that the curves of the signature images are precisely examined. the output of the Python programming language on Tensor Flow. A number of offline signature databases were used, and the findings demonstrate how well.Researchers have released a variety of offline signature verification methods over the past ten years. Although separating authentic signatures from expert forgeries is still a difficult operation, mistake rates have considerably decreased recently, in part because Deep Learning improvements have been applied to the problem. evaluating the most recent developments in the field.The CNN model   at least 95% training accuracy and 60% validation accuracy. "
paragraph_label2 = tk.Label(content_frame, text=paragraph2, font=("godey", 15), justify="left", wraplength=1300, fg="grey")
paragraph_label2.pack(pady=20, anchor="w")




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
facebook_link_label.place(x=200, y=5570)

# Bind the click event to open the Facebook link
facebook_link_label.bind("<Button-1>", lambda event: open_youtube())

def open_instagram():
    webbrowser.open("https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwii6q2X5P2CAxWq2QIHHXwUDCcQwqsBegQIDRAG&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DCChuwRS06Zs&usg=AOvVaw0nZdWSCeqgCZEQlgqGqXPs&opi=89978449")  # Replace with the desired Facebook URL

# Create a label with a colored background that represents the Facebook link
facebook_link_label = tk.Label(content_frame, text="https://www.instagram.com", fg="white", bg="sky blue", cursor="hand2")
facebook_link_label.place(x=450, y=5570)

# Bind the click event to open the Facebook link
facebook_link_label.bind("<Button-1>", lambda event: open_instagram())

def open_facebook():
    webbrowser.open("https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiIz76u5P2CAxXj0wIHHY7AApQQFnoECCoQAQ&url=https%3A%2F%2Fwww.entrust.com%2Fblog%2F2020%2F05%2Fvideo-verification-for-document-signing%2F&usg=AOvVaw2J_mixvVgdAZI6D2jBzk_K&opi=89978449")  # Replace with the desired Facebook URL

# Create a label with a colored background that represents the Facebook link
facebook_link_label = tk.Label(content_frame, text="https://www.facebook.com", fg="white", bg="sky blue", cursor="hand2")
facebook_link_label.place(x=700, y=5570)

# Bind the click event to open the Facebook link
facebook_link_label.bind("<Button-1>", lambda event: open_facebook())

# Create a label with a colored background that represents the Facebook link
facebook_link_label = tk.Label(content_frame, text="03427960776", fg="white", bg="sky blue")
facebook_link_label.place(x=1000, y=5570)


# Create a label with a colored background that represents the Facebook link
facebook_link_label = tk.Label(content_frame, text="Contact Us", fg="white", bg="sky blue", font=("impact", 50))
facebook_link_label.place(x=50, y=5470)



# Make the window fullscreen
root.geometry("{0}x{0}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

root.update_idletasks()  # Update the window idle tasks to properly set the canvas size
canvas.config(scrollregion=canvas.bbox("all"))  # Set the scroll region based on the canvas content

root.mainloop()
