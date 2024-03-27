#!/usr/bin/env python3

from pwn import xor
from sys import argv
from hashlib import md5
from base64 import b64decode
from Crypto.Util.number import *

def decipher(fname, key, j):
    encrypted_data = open(fname, 'r').read().strip()
    decrypted_data = xor(b64decode(encrypted_data.encode()), key).decode()
    original_flag = ''

    for n, char in enumerate(decrypted_data):
        if n % 2 != 0:
            original_flag += bytes.fromhex(char).decode()
        else:
            original_flag += chr(int(md5(char.encode()).hexdigest(), 16) ^ j)

    return original_flag

flag = decipher('enc.txt', argv[0].encode(), 0x1337)
print(flag)
