key = "spidermanowhtvc"

def decrypt(encrypted_text):
    decrypted_text = ""
    key_length = len(key)
    
    for char in encrypted_text:
        char_index = key.find(char)
        if char_index != -1:
            # Decrypting the character by shifting it back 3 positions
            decrypted_char_index = (char_index - 3 + key_length) % key_length
            decrypted_text += key[decrypted_char_index]
        else:
            decrypted_text += char
    
    return decrypted_text


def encrypt(plaintext):
    encrypted_text = ""
    key_length = len(key)
    
    for char in plaintext:
        char_index = key.find(char)
        if char_index != -1:
            encrypted_char_index = (char_index + 3) % key_length
            encrypted_text += key[encrypted_char_index]
        else:
            encrypted_text += char
    
    return encrypted_text

#print(decrypt("Swermanowh"))
#print(encrypt("Sapiderman"))
#print(encrypt("Admin"))
#print(decrypt("Udan"))
print(encrypt("Sapiderman"))
print(encrypt("Spiderman"))
print(encrypt("Peter Parker"))
print(encrypt("sapiderman"))
print(encrypt("spiderman"))
print(encrypt("Admin"))
print(encrypt("Administrator"))
print(encrypt("10082001"))
print(encrypt("whoami"))
