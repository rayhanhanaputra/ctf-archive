flag = [65, 10, 76, 120, 69, 50, 105, 99, 71, 17, 122, 90, 48, 74, 39, 116, 88, 64, 33, 307, 22, 86, 38, 89, 42, 116, 37, 109, 170, 12, 82, 22, 300, 40, 76, 22, 64, 57]
keys = [0]*38
flagnew=""

indexKey = 0

def phase1():
    s = "TCPIP{FAKEflag}"
    v5 = 0
    i = 0

    for i in range(len(s)):
        v5 = (ord(s[i]) + v5) % 52

    global indexKey
    v1 = indexKey
    indexKey+=1
    keys[v1] = v5

    return v5

def phase2():
    s = "TCPIP{HiYAA_FAKE}"
    v5 = 33

    for i in range(0, len(s), 2):
        v5 = (ord(s[i]) + v5) % 100
    
    global indexKey
    v1 = indexKey
    indexKey+=1
    keys[v1] = v5

    return v5

def phase3():
    s = "TCPIP{stillFAKEE}"
    v5 = 23

    for i in range(len(s)):
        if i % 3 == 0:
            v5 = ((ord(s[i]) + v5) ^ 2) % 101

    global indexKey
    v1 = indexKey
    indexKey+=1
    keys[v1] = v5
    return v5 + 1

def phase4():
    v0 = phase2()
    v1 = phase1() + v0
    v4 = v1 // phase2()  # Use integer division for equivalence
    global indexKey
    v2 = indexKey
    indexKey+=1
    keys[v2] = v4
    return v4

def phase5():
    v4 = 0
    v2 = "TCPIP{ohofcourseedisFAKE}"

    for i in range(12, 3, -1):
        v4 = (ord(v2[i]) + v4 - i) % 80

    global indexKey
    v0 = indexKey
    indexKey+=1
    keys[v0] = v4

    return v4

def phase6():
    v4 = 0
    v2 = "TCPIP{donottSubmitDisFAKEE}"

    for i in range(12, 3, -1):
        v4 = (i ^ (ord(v2[i]) + v4)) % 133

    global indexKey
    v0 = indexKey
    indexKey+=1
    keys[v0] = v4

    return v4

def phase7():
    global indexKey
    v0 = indexKey
    indexKey += 1
    keys[v0] = 116
    return 116

def phase8():
    global indexKey
    v0 = indexKey
    indexKey += 1
    keys[v0] = 37
    return 122

def phase9():
    s = "}eeekaF{PIPCT}"
    v5 = 13
    v6 = 0

    for i in range(0, len(s), 3):
        v4 = ord(s[i])
        v5 += v4 ^ 2
        v6 += 3

    global indexKey
    v1 = indexKey
    indexKey += 1
    keys[v1] = (v5 % 90) + 33

    return v5

def phase10():
    v0 = phase4()
    v3 = v0 + phase6() - 20

    global indexKey
    v1 = indexKey
    indexKey += 1
    keys[v1] = v3
    return v3

def phase11():
    i = 12

    for i in range(12, 61, 28):
        pass  # Do nothing in this loop

    global indexKey
    v0 = indexKey
    indexKey += 1
    keys[v0] = i

    return i

def phase12():
    s = "TCPIP{disFAKEEE}"
    v5 = 1810

    for i in range(len(s)):
        v5 -= ord(s[i]) + i

    global indexKey
    v1 = indexKey
    indexKey += 1
    keys[v1] = v5

    return v5

def phase13():
    v0 = phase2()
    v1 = phase8() + v0
    v2 = v1 - phase2()
    v3 = phase5() + v2
    v6 = v3 - phase4() + 118

    global indexKey
    v4 = indexKey
    indexKey += 1
    keys[v4] = v6

    return v6

def phase14():
    s = "TCPIP{IsthissssFAKE?OfcourseE!}"
    v5 = 0

    for i in range(len(s)):
        v5 += ord(s[i]) - 90

    global indexKey
    v1 = indexKey
    indexKey += 1
    keys[v1] = v5

    return v5

phase1()
phase2()
phase3()
phase4()
phase5()
phase6()
phase7()
phase8()
phase9()
phase10()
phase11()
phase12()
phase13()
phase14()
phase9()
phase2()
phase12()
phase2()
phase6()
phase7()
phase8()
phase11()

for i in range(0,len(flag)):
    flagnew+=chr(flag[i]^keys[i])

print(flagnew)
