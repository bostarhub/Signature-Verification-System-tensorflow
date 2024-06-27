# Signature Verification System

This project uses Python to perform signature verification, leveraging TensorFlow and Keras for machine learning tasks. It detects and verifies signatures in images and documents.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- Detect signatures in images and documents
- Verify known signatures from a dataset
- Add new signatures to the dataset
- Manage users and administrators

## Installation

To run this project, you'll need to have Python and Anaconda installed on your system. You can install the required packages using `pip`.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/Signature-Verification-System.git
   cd Signature-Verification-System
   ```

2. **Create and activate a virtual environment:**

   It is recommended to use Anaconda for managing your environments.

   - **Create a new environment:**

     ```bash
     conda create -n signature_verification python=3.8
     ```

   - **Activate the environment:**

     ```bash
     conda activate signature_verification
     ```

   - **Install TensorFlow and other dependencies:**

     ```bash
     pip install tensorflow keras opencv-python
     ```

3. **Open the project in Visual Studio Code:**

   - Attach the Anaconda environment to Visual Studio Code.
   - Open Visual Studio Code and select the `signature_verification` environment.

4. **Run the application:**

   - **Unzip the project files:**
     Download and unzip the project files if not already done.

5. **Access the User Interface:**

   - Open the administrative interface.
   - From there, you can access two main sections: Signature Verification and Adding Users/Admins.
   - In the Signature Verification section, you can verify signatures.
   - In the Adding Users/Admins section, you can add or remove new users and administrators, train models, and manage the dataset.

## Usage

Here is a basic guide on how to use the signature verification system:

1. **Setup and Run:**
   - Ensure all dependencies are installed and the environment is activated.
   - Run the `main.py` script followed by the `login.py` script to start the application.

2. **User Interface:**
   - Access the user interface where you can manage users and perform signature verification.

3. **Adding and Verifying Signatures:**
   - Use the administrative interface to add new users or administrators.
   - Verify signatures by uploading images and comparing them against the dataset.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any feature requests or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- OpenCV
- TensorFlow
- Keras

