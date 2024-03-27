flagenc = b'\x8c\x86\xb1\x90\x86\xc9=\xbe\x9b\x80\x87\xca\x86\x8dKJ\xc4e?\xbc\xdbC\xbe!Y \xaf'

def op1(b):
    c = [0]*len(b)
    for i in range(len(b)):
        if b[i]%2==1:
            c[i] = b[i]
        else:
            c[i] = b[i]-8
    return c

def op2(b):
    c = [0]*len(b)
    for i in range(len(b)):
        c[i] = b[i]-12
    return c

def op3(b):
    c = [0]*len(b)
    for i in range(len(b)):
        if b[i] >= 128:
            c[i] = ((b[i]-128) *2) +1 
        else:
            c[i] = (b[i]*2 )+1
    return c

def recur(b):
    if len(b) == 1:
        return b
    assert len(b) % 3 == 0
    a = len(b)
    print(b)
    return op1(recur(b[0:a//3]))+op2(recur(b[a//3:2*a//3]))+op3(recur(b[2*a//3:]))

hahah = recur(flagenc)

for h in hahah:
    print(chr(h),end="")


