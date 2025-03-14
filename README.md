# Caesar Cipher Tool

## Overview
The **Caesar Cipher Tool** is a Streamlit-based application that allows users to encrypt and decrypt messages using a Caesar cipher. By shifting letters in the alphabet, 
you can transform text into a secret code or decode it back to its original form. This mini-project,showcases a simple yet interactive UI for exploring ciphers.

## Set Up a Virtual Environment Create an isolated environment to manage dependencies:

python -m venv "environment-name"

**Activate the environment**

"environment-name"\Scripts\activate

## How to Install Dependencies

pip install streamlit

## Running the App

Access the App Open your web browser and visit the deployed application at:

URL: https://huggingface.co/spaces/ptlsneh/CeasorCipher

## Project Components

**Title & Description**

Purpose: Welcomes users and explains the app’s functionality. It sets the context by displaying "Caesar Cipher Tool" and a brief tagline about shifting letters for encryption/decryption.

**Shift Slider**

Purpose: Allows users to define the number of positions (1–10) each letter in the message is shifted. This controls the strength and direction of the cipher transformation.

**Text Area (Your Message)**

Purpose: Provides a space for users to input the text they want to encrypt or decrypt. It’s the core input field where the message is entered.

**Checkbox (Decrypt Mode)**

Purpose: Toggles the app between encryption and decryption modes. When unchecked, it encrypts the message; when checked, it decrypts it, offering flexibility in how the cipher is applied.

**Output Display**

Purpose: Shows the result of the encryption or decryption process. It presents the transformed message clearly, prefixed with "Encrypted Message" or "Decrypted Message" based on the mode.

## Example

Here’s a quick example to see the Caesar Cipher Tool in action:

**For Encryption**

**Input:**

Message: Hello, World!

Shift Value: 3

Decrypt Mode: Unchecked (Encrypt)

**Output:**

Encrypted Message: Khoor, Zruog!

**For Decryption**

**Input**

Message: Khoor, Zruog!

Shift Value: 3

Decrypt Mode: Checked (Decrypt)

**Output**

Decrypted Message: Hello, World!

