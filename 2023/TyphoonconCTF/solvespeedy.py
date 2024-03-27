from pwn import *

def recurs(a1):
	if a1:
		return a1*recurs(a1-1)
	else:
		return 1

def calculate_hcf(a, b):
	while b != 0:
		temp = b
		b = a % b
		a = temp
	return a

p = remote("0.cloud.chals.io",34026)

while True:
	angka = p.recv(timeout=2)
	print(angka)
	qwe = angka.decode().replace("\n", "")
	qwe = qwe.split(' ')
	asd = []
	for c in qwe:
		asd.append(int(c))

	temp = calculate_hcf(asd[0],asd[1])
	temp2 = recurs(temp+3)
	print(temp2)
	p.sendline(str(temp2))
