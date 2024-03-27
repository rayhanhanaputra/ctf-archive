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

key = [0x22,0x11,0x75,0xe1,0x66,0x12,0xa,0x75,0xe1,0x66]
v5=len(key)
idx=0
for c in cipher:
    print(chr(ord(c)^key[idx%v5]),end='')
    idx+=1