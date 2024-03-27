def read_string_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='latin-1') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found.")
        return None

# Example usage:
file_path = 'enc.txt'  # Change this to the path of your text file
cipher = read_string_from_file(file_path)

key = [0x76,0x22,0x99,0xf2,0x11,0x67,0xfe,0x66]

# cipher = a3[i%len(a3)] ^ a2[i]
idx=0
for c in cipher:
    print(chr(ord(c)^key[idx%len(key)]),end="")
    idx+=1