from pwn import *

for i in range(34800,37000):
	p = remote("103.145.226.206", 20048)
	
	p.recv()
	p.sendline(b"Edward Seky Soeryadjaya")
	p.recv()
	p.sendline(str(i))
	temp = (p.recv())
	print(temp,i)
	if "Correct" in temp.decode():
		break
	p.close()
