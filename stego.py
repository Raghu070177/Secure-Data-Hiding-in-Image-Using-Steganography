import cv2
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog  # Import simpledialog explicitly

# Function to select an image file
def select_image():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.jpg;*.png;*.jpeg;*.bmp;*.tiff")]
    )
    return file_path

# Function to get user input for message and password
def get_user_input():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    msg = simpledialog.askstring("Input", "Enter secret message:", parent=root)
    password = simpledialog.askstring("Input", "Enter a passcode:", parent=root, show='*')
    return msg, password

# Function to decrypt the message
def decrypt_message(img, msg_length, password, correct_password):
    if password != correct_password:
        print("YOU ARE NOT AUTHORIZED")
        return

    message = ""
    n, m, z = 0, 0, 0

    for _ in range(msg_length):
        message += c[img[n, m, z]]
        m += 1
        if m >= width:
            m = 0
            n += 1
        z = (z + 1) % 3  # Cycle through RGB channels
    print("Decrypted message:", message)

# Main program
if __name__ == "__main__":
    # Select an image
    image_path = select_image()
    if not image_path:
        print("No image selected. Exiting...")
        exit()

    # Read the image
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Invalid image file or path.")
    except Exception as e:
        print(f"Error: {e}")
        exit()

    # Get user input for message and password
    msg, password = get_user_input()
    if not msg or not password:
        print("No message or password entered. Exiting...")
        exit()

    # Create dictionaries for encryption and decryption
    d = {chr(i): i for i in range(255)}
    c = {i: chr(i) for i in range(255)}

    # Get image dimensions
    height, width, channels = img.shape

    # Make sure the image has enough space for the message
    if len(msg) > height * width * channels:
        print("Error: The image is too small to hold the entire message.")
        exit()

    # Encryption process
    n, m, z = 0, 0, 0

    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        m += 1
        if m >= width:
            m = 0
            n += 1
        z = (z + 1) % 3  # Cycle through RGB channels

    # Save the encrypted image
    encrypted_image_path = "encryptedImage.jpg"
    cv2.imwrite(encrypted_image_path, img)
    print(f"Encrypted image saved as {encrypted_image_path}")
    os.system(f"start {encrypted_image_path}")  # Open the encrypted image

    # Decryption process
    pas = input("Enter passcode for Decryption: ")
    decrypt_message(img, len(msg), pas, password)
