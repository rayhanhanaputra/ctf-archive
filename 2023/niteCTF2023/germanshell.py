def rot_n(message, n):
    encrypted_message = ""
    
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            shift = 65 if char.isupper() else 97  # ASCII code for 'A' (uppercase) or 'a' (lowercase)
            encrypted_char = chr((ord(char) - shift + n) % 26 + shift)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char  # Keep non-alphabetic characters unchanged
    
    return encrypted_message

# Example usage:
message = "cat /var/quantumLava/flag.txt"
walik = message[::-1]
rotation = 0

for c in walik:
    # print(c,-rotation, rot_n(c,-rotation))
    print(rot_n(c,-rotation),end="")
    rotation+=1

# encrypted = rot_n(message, rotation)
# print("Original:", message)
# print(f"Encrypted (ROT-{rotation}):", encrypted)

#nite{tr7n517t10n_u51ng_t1m3_n0t_c001_00000yx}
#twr.cvfy/rlpZzgexjcx/wey/ tza