# Caesar's Cipher in Python
def caesar_encrypt(text):
    result = ""
#
    for i in range(len(text)):
        # Obtain ASCII value using 'ord'
        char_position = ord(text[i])
        # Subtract 97 to have a character from 1 to 26
        char_position = char_position - 97
        # Add '3' to the position
        new_char_position = char_position + 3
        # Make sure that the position does not surpass
        # 26 (we're wrapping around)
        new_char_position = new_char_position % 26
        # Convert back to ASCII values
        new_char_position = new_char_position + 97
        # Convert ASCII value to character and concatenate
        # it to the final result.
        result = result + chr(new_char_position)
        print(result)
    return result
#
def caesar_decrypt(cipher_text):
    result = ""
    for i in range(len(cipher_text)):
        char_position = ord(cipher_text[i])
        char_position = char_position - 97
        # Subtract 3 instead, to get back original position
        new_char_position = char_position -3
        new_char_position = new_char_position % 26
        # Convert back to ASCII values
        new_char_position = new_char_position + 97
        # Convert ASCII value to char and concatenate
        # it to final result
        result = result + chr(new_char_position)
        print(result)
    return(result)
text = input('Enter a word to be encrypted: ')
print(f"Plain Text: {text}")
cipher_text = caesar_encrypt(text)
print(f"Encrypted: {cipher_text}")
print(f"Decrypted: {caesar_decrypt(cipher_text)}")
#
# EOF
#