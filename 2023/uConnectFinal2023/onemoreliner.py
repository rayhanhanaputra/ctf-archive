#!/usr/bin/env python3

from pwn import xor
from sys import argv
from hashlib import md5
from base64 import b64encode
from Crypto.Util.number import *

flag = 'uconnect{one_flag_is_here}'
cipher = lambda f,i,j,k,n: open(fname, 'w').write(b64encode(xor(long_to_bytes(int(''.join([chr(_).encode().hex() if n % 2 != 0 else md5(chr(_).encode()).hexdigest() for n,_ in enumerate([ord(_) if not _.isalpha() else ord(_) ^ n for _ in i])]), 16)), j)).decode())
cipher('enc.txt', flag, argv[0].encode(), 0x1337, 10)