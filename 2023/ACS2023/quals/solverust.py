from pwn import *
import string
context.log_level = 'error'
payload = b"ACS{"
flag = "2c171c245d43000e3a24202323472130092757002a2b15"
flagHex = [flag[i:i+2] for i in range(0,len(flag),2)]
for i in range(0,28):
    for j in string.printable:
        p = process("./rustarm")
        p.recvuntil(b": ")
        p.sendline(payload+j.encode()+b"}")
        p.recvuntil(b": ")
        leak = p.recvuntil("\n").decode().strip()
        if leak == flag[0:2+(i*2)]:
            payload += j.encode()
            print(payload)
            break
        p.close()
    # break

