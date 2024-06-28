import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import os
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import cv2
import os
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout


# Define the paths to the directories containing real and forged images
real_path = r'D:/folder-A\dataset/REAL_ALL'
forge_path = r'D:/folder-A\dataset/FORGERY_ALL'

# Initialize empty lists to store real and forged images
real_images = []

# Iterate through the files in the 'real' directory
for img_name in os.listdir(real_path):
    # Read the image in grayscale using OpenCV
    img = cv2.imread(os.path.join(real_path, img_name), cv2.IMREAD_GRAYSCALE)
    # Append the image to the list
    real_images.append(img)

# Convert the list of real images to a NumPy array with dtype=object
real_images = np.array(real_images, dtype=object)

# Display a summary of the real_images array
print("Real Images Summary:")
print(f"Shape: {real_images.shape}")
print(f"Data Type: {real_images.dtype}")
print(f"Number of Images: {len(real_images)}")
print(f"Example Image:\n{real_images[0]}")  # Display the first image as an example

# Initialize an empty list to store forged images
forge_images = []

# Iterate through the files in the 'forged' directory
for img_name in os.listdir(forge_path):
    # Read the image in grayscale using OpenCV
    img = cv2.imread(os.path.join(forge_path, img_name), cv2.IMREAD_GRAYSCALE)
    # Append the image to the list
    forge_images.append(img)

# Convert the list of forged images to a NumPy array with dtype=object
forge_images = np.array(forge_images, dtype=object)

# Display a summary of the forge_images array
print("\nForge Images Summary:")
print(f"Shape: {forge_images.shape}")
print(f"Data Type: {forge_images.dtype}")
print(f"Number of Images: {len(forge_images)}")
print(f"Example Image:\n{forge_images[0]}")  # Display the first image as an example
from sklearn.model_selection import train_test_split

real_labels = np.zeros(real_images.shape[0])
forge_labels = np.ones(forge_images.shape[0])

X = np.concatenate((real_images, forge_images), axis=0)
y = np.concatenate((real_labels, forge_labels), axis=0)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Number of images in the training set
num_train_images = X_train.shape[0]

# Number of images in the testing set
num_test_images = X_test.shape[0]

print("Number of images in the training set:", num_train_images)
print("Number of images in the testing set:", num_test_images)

# load the dataset
real_path = r'D:/folder-A/dataset/REAL_ALL'
forge_path = r'D:/folder-A/dataset/FORGERY_ALL'

# set the image size to 128x128
img_size = (128, 128)

real_images = []
for img_name in os.listdir(real_path):
    img = cv2.imread(os.path.join(real_path, img_name), cv2.IMREAD_GRAYSCALE)
    # print(f"Image: {img_name}, Size: {img.shape}")
    img = cv2.resize(img, img_size)
    real_images.append(img)

# Convert the list of real images to a NumPy array with dtype=object
real_images = np.array(real_images, dtype=object)
# Display a summary of the resized images
print("Resized Real Image Shape:", real_images[0].shape)

# Display a summary of the real_images array
print("Real Images Summary:")
print(f"Shape: {real_images.shape}")
print(f"Data Type: {real_images.dtype}")
print(f"Number of Images: {len(real_images)}")
print(f"Example Image:\n{real_images[0]}")
# Initialize an empty list to store forged images
forge_images = []

# Iterate through the files in the 'forged' directory
# Inside the loop for reading forged images
for img_name in os.listdir(forge_path):
    # Read the image in grayscale using OpenCV
    img = cv2.imread(os.path.join(forge_path, img_name), cv2.IMREAD_GRAYSCALE)

    # Check if the image is None (failed to load)
    if img is None:
        print(f"Error loading image: {img_name}")
        continue

    # Add these lines to check the shape of the loaded image
    # print(f"Image: {img_name}, Original Size: {img.shape}")

    # Resize the image to the desired size
    img = cv2.resize(img, img_size)
    # Append the image to the list
    forge_images.append(img)

# Continue with the rest of your code
# Convert the list of forged images to a NumPy array with dtype=object
forge_images = np.array(forge_images, dtype=object)
# RESIZE SUMMARY
print("Resized Forged Image Shape:", forge_images[0].shape)
# Display a summary of the forge_images array
print("\nForge Images Summary:")
print(f"Shape: {forge_images.shape}")
print(f"Data Type: {forge_images.dtype}")
print(f"Number of Images: {len(forge_images)}")
print(f"Example Image:\n{forge_images[0]}")
# normalize the data
# normalize the data
real_images = real_images.astype('float32') / 255.0
forge_images = forge_images.astype('float32') / 255.0
# import numpy as np

num_real_images = len(real_images)
num_forge_images = len(forge_images)

# Create labels for the real and forged signatures
real_labels = np.zeros(num_real_images, dtype=int)
forge_labels = np.ones(num_forge_images, dtype=int)

# Concatenate the real and forged images and labels
X = np.concatenate((real_images, forge_images), axis=0)
y = np.concatenate((real_labels, forge_labels), axis=0)

# Create dummy data
X_train = np.random.rand(40, 128, 128)

# Add another dimension to the array
X_train = np.expand_dims(X_train, axis=-1)

# Reshape the array
X_train = X_train.reshape(X_train.shape[0], 128, 128, 1)

print(X_train.shape)  # Output: (40, 128, 128, 1)
# import numpy as np

# Create dummy data
X_test = np.random.rand(40, 128, 128)

# Add another dimension to the array
X_test = np.expand_dims(X_test, axis=-1)

# Reshape the array
X_test = X_test.reshape(X_test.shape[0], 128, 128, 1)

print(X_test.shape)  # Output: (40, 128, 128, 1)

# Create a Sequential model
model = Sequential()

# Add a convolutional layer
model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(128, 128, 1)))

# Add a max pooling layer
model.add(MaxPooling2D(pool_size=(2, 2)))

# Add another convolutional layer
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))

# Add another max pooling layer
model.add(MaxPooling2D(pool_size=(2, 2)))

# Flatten the output from the convolutional layers
model.add(Flatten())

# Add a fully connected layer with 128 neurons and a relu activation function
model.add(Dense(units=128, activation='relu'))

# Add a dropout layer to reduce overfitting
model.add(Dropout(rate=0.5))

# Add the output layer with a sigmoid activation function
model.add(Dense(units=1, activation='sigmoid'))

# Print a summary of the model architecture
model.summary()


# Assuming you have already defined and compiled your 'model' as shown in the previous code

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# Add another dimension to X_train to represent the channel
# Assuming X_train and X_test have shape (batch_size, height, width)
X_train = np.expand_dims(X_train, axis=-1)
X_test = np.expand_dims(X_test, axis=-1)
# Train the model
history = model.fit(X_train, y_train, batch_size=32, epochs=50, validation_data=(X_test, y_test))
# Evaluate the model on the test set
test_loss, test_acc = model.evaluate(X_test, y_test)

# Print the test accuracy and loss
print("Test accuracy:", test_acc)
print("Test loss:", test_loss)
# Load a signature image
# You can change the image path and check if it is forged or real
img_path = r'dataset/UserID1700520204'
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded successfully
    # Resize the image
img = cv2.resize(img, (128, 128))
    
    # Ensure the image has valid dimensions
if img.shape == (128, 128):
    img = np.array(img).reshape(1, 128, 128, 1) / 255.0
        
    # Continue with further processing or prediction
    # For example, you can predict the class of the signature image
    prediction = model.predict(img)

if prediction < 0.5:
    print("The signature is real.")
else:
    print("The signature is forged.")
# Save the model to a file
model.save('signature_model.h5')
print("Model saved successfully.")