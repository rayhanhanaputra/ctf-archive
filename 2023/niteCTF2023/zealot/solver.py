from z3 import *

# Creating an array of 42 symbolic integer variables
a1 = [Int('a1[%d]' % i) for i in range(42)]

# Adding constraints based on the conditions provided
s = Solver()

for i in a1:
    s.add(i>0)
    s.add(i<128)

s.add(a1[5] == 84)
s.add(a1[6] == 70)
s.add(a1[0] == a1[40])

x = a1[1]
y = a1[37]
x_bitvec = BitVec('x', 32) 
y_bitvec = BitVec('y', 32)
s.add(x_bitvec ^ y_bitvec == 0x1D) 

s.add(a1[3] == a1[18])
s.add(a1[18] == a1[32])

xx = a1[2]
yy = 0x34
xx_bitvec = BitVec('xx', 32) 
yy_bitvec = BitVec('yy', 32)
s.add(Or((xx_bitvec ^ yy_bitvec) == 20, True))

s.add(a1[8] == 103)
s.add(a1[37] != 32)
s.add(a1[21] == 116)
s.add(a1[7] + 2 == a1[41])
s.add(32 * a1[8] == 3296)
s.add(a1[17] == 104)
s.add(a1[9] == a1[10])
s.add(a1[14] == a1[29])
s.add(a1[29] == a1[39])
s.add(a1[12] == 95)

aa = a1[12] + 2051495600
bb = 0x4894482C
cc = 0x4280202
dd = 0x4C2C4251
ee = a1[16]
aa_bitvec = BitVec('aa', 32) 
bb_bitvec = BitVec('bb', 32)
cc_bitvec = BitVec('cc', 32)
dd_bitvec = BitVec('dd', 32)
ee_bitvec = BitVec('ee', 32)
s.add((ee_bitvec == (((aa_bitvec & bb_bitvec) | cc_bitvec) ^ dd_bitvec)) % 256 == 0)

s.add(a1[0] == 110)
s.add((((a1[31] ^ a1[41]) & 0x8E56) ^ 0x6D) == a1[14])
s.add(a1[23] == ((((a1[12] - 903645652) & 0x62486926) | 0x4020040) ^ 0x4602601D))
s.add(a1[2] == 116)
s.add(a1[27] == ((((a1[12] + 802870624) & 0xC0A28043) | 0x395D4B28) ^ 0x39DFCB74))
s.add(a1[31] == ((((a1[12] + 1050330464) & 0xDA04A63F) | 0x995980) ^ 0x1A99DDE0))
s.add(((a1[24] ^ 0x66) & 0x400001 | 0x64) == a1[26])
s.add(((a1[24] ^ 0x62) & 1 | 0x64) == a1[33])
s.add((((a1[28] << 25) ^ 0x60000000) & 0x200610 | 0x63) == a1[35])
s.add(a1[3] == 101)
s.add(a1[28] == 102)
s.add(a1[6] + 34 == a1[17])
s.add(a1[41] == 125)
s.add(a1[20] == (((a1[1] + a1[3]) & 0x8450) ^ 0x40 | 0x6C))
s.add(a1[36] == a1[19])
s.add(a1[19] == a1[6] + 27)
s.add(a1[34] != -563555251)
s.add(a1[1] == 105)
s.add(a1[25] == (((a1[4] >> 3) & 0x120D) ^ 0x69))
s.add(a1[21] != 0)
s.add(((a1[20] ^ 0x4E) | 0x50) == a1[15])
s.add(((a1[20] ^ 0x4E) | 0x50) == a1[30])
s.add(a1[11] == a1[22] - 4)
s.add(a1[22] == (((a1[9] ^ a1[12]) & 0xB00B) ^ 0x68))
s.add(a1[30] == a1[15])
s.add((((a1[5] - 456630272) & 0x9594815B) | 0x4A6B0680) ^ 0xCEEB06B2 == a1[24])
s.add(a1[9] == 111)
s.add(a1[4] == 67)
s.add((a1[38] == (~(a1[13]) & a1[20] ^ 9) | 0x68))
s.add((a1[13] ^ 0x62) == ((a1[20]) & 0x4696))

# Check if the constraints are satisfiable
if s.check() == sat:
    print("Satisfiable")
    m = s.model()
    for i in range(42):
        print(f"a1[{i}] = {m[a1[i]]}")
else:
    print("Unsatisfiable")
