# Secure-Data-Hiding-in-Image-Using-Steganography

Overview
This project demonstrates how to securely hide a message inside an image using steganography techniques. It uses encryption and decryption methods to ensure the confidentiality of the hidden message, requiring a password to retrieve the message. The user can select an image, input a secret message, and encrypt it into the image. Later, the image can be decrypted by selecting the encrypted image and entering the correct passcode.

Features
Encryption: A secret message is embedded into an image using the least significant bit (LSB) method of steganography.
Decryption: The user can extract the hidden message from the image by providing the correct passcode.
Password Protection: The decryption process is secured with a passcode to ensure that only authorized users can retrieve the hidden message.
Image File Selection: Users can select images from their local file system for both encryption and decryption processes.
Requirements
Python 3.x
OpenCV library (cv2) for image manipulation
Tkinter for graphical user interface (GUI) to select files and provide inputs

How to Use
Step 1: Select an Image for Encryption
The program will prompt the user to select an image file (e.g., .jpg, .png, .jpeg, .bmp, .tiff).
The user is then asked to enter a secret message and a passcode to secure the message.
Step 2: Encrypt the Message into the Image
The secret message will be hidden within the image by modifying the pixel values using a simple encryption algorithm.
The encrypted image will be saved with the name encryptedImage.jpg.
Step 3: Decrypt the Message
After encryption, the user can select the encrypted image for decryption.
The program will ask for the passcode to decrypt the message. If the correct passcode is provided, the hidden message will be displayed.
Step 4: Error Handling
If the image is too small to hide the entire message, an error will be displayed.
If the passcode is incorrect during decryption, a message will inform the user that they are not authorized.
Code Explanation
Encryption:

The message is converted into its corresponding ASCII values.
The message is hidden within the image by replacing the least significant bits of the pixel values with the message characters.
The resulting image is saved as an encrypted image.
Decryption:

The encrypted image is read.
The hidden message is retrieved by extracting the least significant bits from the pixel values, and then the ASCII values are converted back to characters.
The passcode provided by the user is validated before revealing the hidden message.

Example
Encrypt a message into an image:

Select an image (e.g., myImage.jpg).
Enter the secret message you want to hide (e.g., "Hello, World!").
Set a passcode for security (e.g., 12345).
The image myImage.jpg will be saved as encryptedImage.jpg with the secret message hidden.
Decrypt the message:

Select the encryptedImage.jpg.
Enter the correct passcode (e.g., 12345).
The hidden message will be displayed in the console (e.g., "Hello, World!").
Security Considerations
Password Protection: The decryption process requires a correct passcode. Without the correct passcode, the hidden message cannot be accessed.
Message Length: Ensure the image is large enough to hold the entire message. If the image is too small, an error will be raised during encryption.
Conclusion
This project demonstrates how steganography can be used to hide a message inside an image, making it secure and unobtrusive. The use of a password provides an extra layer of security, ensuring that the hidden data can only be accessed by authorized users.
