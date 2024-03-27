obj=''
length = len(obj)
iArr = [ord(obj[i]) << 1 for i in range(length)]

bArr = bytearray(length)