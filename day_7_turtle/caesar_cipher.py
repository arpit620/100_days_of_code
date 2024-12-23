def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr((ord(char) + shift_amount - 65) % 26 + 65) if char.isupper() else chr((ord(char) + shift_amount - 97) % 26 + 97)
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def caesar_cipher():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    
    if direction == 'encode':
        result = encrypt(text, shift)
    elif direction == 'decode':
        result = decrypt(text, shift)
    else:
        result = "Invalid direction. Please type 'encode' or 'decode'."
    
    print(f"The resulting text is: {result}")

if __name__ == "__main__":
    caesar_cipher()
