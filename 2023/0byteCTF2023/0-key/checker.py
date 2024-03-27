def O0OOOOOOOOO(a1): #aman
    a1 = list(map(int, a1))  # Convert each element to an integer
    return ((a1[2] == a1[4] - a1[3]) ^ (a1[0] + a1[1])) != a1[2]

def OO0OOOOOOOO(a1):#
    a1 = list(map(int, a1))  # Convert each element to an integer
    return a1[8] % 3 + a1[7] % 2 + a1[6] % 5 == a1[10] % 7 - a1[9] % 11

def OOO0OOOOOOO(a1):
    a1 = list(map(int, a1))  # Convert each element to an integer
    return a1[12] * a1[16] - (a1[14] ^ a1[15]) == 8 * a1[12] + 4 * a1[13] + 16 * a1[14]

def OOOO0OOOOOO(a1):
    a1 = list(map(int, a1))  # Convert each element to an integer
    return (a1[22] >> 4) == (a1[24] ^ a1[28]) - 1 and (a1[22] & 0xF) == ((a1[25] - a1[28]) ^ 1)

def OOOOO0OOOOO(a1): #5
    a1 = list(map(int, a1))  # Convert each element to an integer
    return (a1[26] & 0xF) == (a1[21] ^ a1[20]) 

def OOOOOO0OOOO(a1):
    a1 = list(map(int, a1))  # Convert each element to an integer
    return 2 * (a1[18] >> 4) == (a1[27] & 0xF) and (a1[18] & 0xF) == 2 * (a1[27] >> 4)

def OOOOOOO0OOO(a1):
    a1 = list(map(int, a1))  # Convert each element to an integer
    return ((a1[12] == a1[18]) ^ (a1[0] ^ a1[6])) != a1[24]

def OOOOOOOO0OO(a1):
    a1 = list(map(int, a1))  # Convert each element to an integer
    return (a1[16] + a1[22]) * (a1[4] + a1[10]) == a1[28] * a1[28] * a1[28]

def OOOOOOOOO0O(a1):
    a1 = list(map(int, a1))  # Convert each element to an integer
    return a1[14] % a1[20] * (a1[2] % a1[8]) == a1[26]

def OOOOOOOOOO0(a1): #10
    a1 = list(map(int, a1))  # Convert each element to an integer
    return a1[14] - a1[9] + a1[24] * a1[19] != 0

def iiiiil(a1):
    return a1[5] == '5' and a1[11] == '5' and a1[17] == '5' and a1[23] == '5' and a1[29] == '5'

def iiiili(a1):
    v2 = 0
    for i in range(5):
        v2 += int(a1[i])
    return v2 == int(a1[30])

def iiilii(a1):
    v2 = 0
    for i in range(6, 11):
        v2 += int(a1[i])
    return v2 == int(a1[31])

def iiliii(a1):
    v2 = 0
    for i in range(12, 17):
        v2 += int(a1[i])
    return v2 == int(a1[32])

def iliiii(a1):
    v2 = 0
    for i in range(18, 23):
        v2 += int(a1[i])
    return v2 == int(a1[33])

def liiiii(a1):
    v2 = 0
    for i in range(24, 29):
        v2 += int(a1[i])
    return v2 == int(a1[34])


#         5    11    17    23    29
a = '00000-00000-00000-00000-00000-00000'

a = '00100-00101-00000-00101-10110-12023'
a = '10000-00101-00000-00101-10110-12023'
a = '00000-00100-00000-00100-00000-01000'
a = '00000-00100-00000-00100-00000-01110'
a = '00000-00100-00000-00100-00000-11010'
a = '00000-00100-00000-00100-01100-01010'
a = '00000-00100-00000-00101-00000-01010' #7
a = '00000-00100-00000-11111-10000-00000'
a = '00000-00100-00000-11111-10011-00053'
a = '00000-00100-00011-11111-10011-01253'

a = '00100500101500000500101510110512023'



total = 0
if iiiiil(a) == True: 
    total+=1
if iiiili(a) == True: 
    total+=1
if iiilii(a) == True: 
    total+=1
if iiliii(a) == True: 
    total+=1
if iliiii(a) == True: 
    total+=1
if liiiii(a) == True: 
    total+=1

if O0OOOOOOOOO(a) == True: 
    total+=1
if OO0OOOOOOOO(a) == True: 
    total+=1
if OOO0OOOOOOO(a) == True: 
    total+=1
if OOOO0OOOOOO(a) == True: 
    total+=1

if OOOOO0OOOOO(a) == True: 
    total+=6
else:
    total+=5

if OOOOOO0OOOO(a) == True: 
    total+=1

if OOOOOOO0OOO(a) == True: 
    total+=1

if OOOOOOOO0OO(a) == True: 
    total+=1

if OOOOOOOOO0O(a) == True: 
    total+=1

if OOOOOOOOOO0(a) == True: 
    total+=1

print(total)