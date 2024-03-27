#!/usr/bin/env python3

import random
import base64
from Crypto.Util.strxor import strxor
from Crypto.Util.number import GCD as gcd
from math import prod

cur = lambda a,b : 1 if gcd(a,b) == 1 else 0
ed = lambda : prod(se for se in b"Good_Luck_Warriors!!!!")
se = lambda a : sum([cur(se,ed()) for se in range(1,a)])

cipher = "pac0FoqwSo2xOqMqPdYVxvX7dfL5ACkaR6Qvm8MzOw1Yxndy2a57Q1KLmDL0oOm0p2mr28A="
ciphertext = base64.b64decode(cipher)

from sympy.ntheory.factor_ import totient
seed = totient(ed())
random.seed(str(seed).rstrip("0"))

plain = strxor(ciphertext, bytes([random.randint(0,255) for _ in range(len(ciphertext))]))
print(plain)

