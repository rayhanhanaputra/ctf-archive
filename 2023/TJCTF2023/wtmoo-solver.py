flag = "8.'8*{;8m33[o[3[3[%\")#*\\}"

asli = ""
for c in flag:
    if ord(c) <= 96 or ord(c) > 122:
        if ord(c) <= 90 or ord(c) > 95:
            if ord(c) <= 36 or ord(c) > 62:
                if ord(c) <= 31 or ord(c) > 36:
                    c = ord(c)
                else:
                    c = ord(c)+21
            else:
                c = ord(c)+60
        else:
            c = ord(c)-43
    else:
        c = ord(c)-32
    
    print(c)
    asli += chr(c)

print(asli)