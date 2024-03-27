def oops():
    print("oops")

def yeayy():
    pass

flag = "TCP1P{byte_code_is_HuFtt}"

if flag[0:6] != 'TCP1P{':
    oops()

if flag[6:10] != 'byte':
    oops()

if flag[10] != flag[15] or flag[15]!=flag[18]:
    oops()

if flag[11:15] != 'code':
    oops()

if flag[11] == flag[19]:
    oops()

if flag[12] == flag[20]:
    oops()

if ord(flag[16]) != 105 or ord(flag[17]) != 115:
    oops()

if flag[19] != 'H':
    oops()

if ord(flag[20]) != 117:
    oops()

if ord(flag[21]) - ord(flag[2]) != 10:
    oops()

if flag[22] != flag[0].lower():
    oops()

if flag[22] == flag[23]:
    yeayy()

