#!/usr/bin/python3

from sys import argv
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import bytes_to_long
from hashlib import md5
from random import randint, seed, choice
from string import ascii_letters
from base64 import b64encode

def e(a, b):
    encrypted_result = []
    b_bytes = bytes.fromhex(b)
    for zzz, z in enumerate(b64encode(str(bytes_to_long(b_bytes)).encode())):
        if zzz % 2 == 0:
            encrypted_result.append(chr(z ^ 0x01))
        else:
            encrypted_result.append(chr(z ^ 0x02))
    return ''.join(encrypted_result)

def w(filename, content):
    with open(f'{filename}.enc', 'wb') as file:
        file.write(content)

if __name__ == '__main__':
	seed('0Byte')
	
	w("flag.png", e(argv[0], argv[1]))