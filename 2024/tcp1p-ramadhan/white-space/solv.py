def read_whitespace(filename):
    whitespace_counts = []
    with open(filename, "r") as file:
        for line in file:
            whitespace_count = 0
            for char in line:
                if char.isspace():
                    whitespace_count += 1
            whitespace_counts.append(whitespace_count)
    return whitespace_counts

cipher = read_whitespace("output.txt")
print(cipher)

key_1 = 41
key_2 = 53

flag = ""
for i,c in enumerate(cipher):
    if (i % 2 == 0):
        flag += chr(c//key_1)
    if (i % 2 == 1):
        flag += chr(c//key_2)

print(flag)
