flag = [2852464175, 252678980, 2517025534, 252678980, 30677878,4225443349, 498629140, 366298937, 1255198513, 1812594589,4067256894, 2238339752, 1842515611, 1993550816, 4108050209,1812594589, 112844655, 1842515611, 701932520, 3707901625, 453955339, 2013832146, 3187964512, 701932520, 3187964512,2439710439, 4088798008, 2238339752, 701932520, 2852464175,4088798008, 1812594589, 2564639436, 701932520, 1466425173,2212294583, 30677878, 2852464175, 3187964512, 1684325040,4239843852]
flagnew = ""

def calculate_crc32(data):
    # CRC32 table initialization
    crc32_table = [0] * 256
    for i in range(256):
        crc = i
        for j in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0xEDB88320
            else:
                crc >>= 1
        crc32_table[i] = crc

    # Calculate CRC32
    crc = 0xFFFFFFFF
    for byte in data:
        crc = (crc >> 8) ^ crc32_table[(crc ^ byte) & 0xFF]

    # Invert the bits and return as a positive integer
    return crc ^ 0xFFFFFFFF

for i in range(len(flag)):
    for j in range(0,255):
        # data = b'H'
        crc32_value = calculate_crc32(chr(j).encode())
        # print(f"CRC32 checksum: {crc32_value}")
        if crc32_value == flag[i]:
            flagnew += chr(j)
            break
print(flagnew)
