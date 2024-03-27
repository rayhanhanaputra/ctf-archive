#!/usr/bin/env python3

import angr

b = angr.Project("./licrackense")

base_address = 0x400000
check_license = base_address + 0x19D8
success = base_address + 0x1C1A
failure = base_address + 0x1C30

secret = b"\x35\x78\xda\x89\xad\x90\x34\x75\x4f\x67\xfd\x89\x79\xf3\x43\x28\x9d\x67\xdf\x54\xf7\x82\x11\x20\xdf\x89\x34\x38\x9d\x67\x47\x89\xd8\x49\x08\xc6\xad\xf1\xc4\x10\x59\x0f\x73\x89\xf9\x21\xff\x57\x99\x3c\x3b\xb3\x6c\xef\x96\x41\x24\xc7\xfd\x44\x44\xa5\x43\x6b\x81\xc5\x68\x5f\x06\x00\x00\x00\x21\x00\x00\x00"

s = b.factory.blank_state(addr=check_license)

s.regs.rdi = 0x0000 # secret
s.regs.rsi = 0x1000 # input

s.memory.store(0x0000, s.se.BVV(secret))
s.memory.store(0x1000, s.se.BVS("guess", 33 * 8))

sim = b.factory.simgr(s)
sim.explore(find=success, avoid=failure)

if sim.found:
    solution_state = sim.found[0]
    license = solution_state.se.eval(solution_state.memory.load(0x1000, 33), cast_to=bytes)
    with open("license.txt", "wb") as f:
        f.write(license)
else:
    raise Exception('Could not find the solution')