from pwn import *

for i in range(1,32):
	p = remote("192.168.0.45", 10125)
	p = process('./sigme')
	p.recvuntil(b">> ")
	p.sendline(b"1")
	p.recv()
	p.sendline(str(i))
	p.recv()
	p.sendline(b"2")
	p.recv()
	p.sendline(str(i))
	print(p.recv(),i)
	p.close()

