import streamlit as st

st.set_page_config(page_title="Ceasar Cipher Tool" , layout="wide")

st.title("Ceasar Cipher Tool")

st.caption("**Enter a message and adjust the shift to encrypt or decrypt**")

shift = st.sidebar.slider(
    "Shift",
    max_value = 10,
    min_value = 1,
    value = 5,
    step = 1,
    help = "Number of positions to shift each letter in the alphabet."
)
st.sidebar.caption("**Purpose: Sets how many positions each letter shifts in the alphabet.**")

def Encrypt(message):
    encrypt = ""
    for i in message.strip():
        if i.isalpha():
            index = letters.find(i.lower())
            encrypt = encrypt + letters[(index+shift)%26]
        else:
            encrypt = encrypt + i 

    st.success(f"**Encrypted Message: {encrypt}**")

def Decrypt(message):
    decrypt = ""
    for i in message.strip():
        if i.isalpha():
            index = letters.find(i.lower())
            decrypt = decrypt + letters[(index-shift)%26] 
        else: 
            decrypt = decrypt + i

    st.success(f"**Decrypted Message: {decrypt}**")
    
message = st.text_area("Enter the Message",  placeholder = "Type your message", help="Enter text to encrypt or decrypt.")
st.caption("**Purpose: Provides the text to be encrypted or decrypted.**")

letters = "abcdefghijklmnopqrstuvwxyz"

c_box = st.checkbox("Decrypt Mode", help="Check to decrypt the message; leave unchecked to encrypt it.")
st.caption("**Purpose: Toggles between encrypting and decrypting the input message.**")

if message:
    if c_box:
        Decrypt(message)  
    else:
        Encrypt(message)    
else:
    st.info("**Please type a message to begin.**")