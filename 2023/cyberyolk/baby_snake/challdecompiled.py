# Source Generated with Decompyle++
# File: chall.pyc (Python 3.9)


def b(i):
    r = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    a = []
    n = 0
    d = 0
    y = 0
    for p in i:
        y = y << 8 | p
        d += 8
        if d >= 6:
            l = y >> d - 6 & 63
            a.append(r[l])
            d -= 6
            continue
            continue
            if d > 0:
                n = 6 - d
                y <<= n
                l = y & 63
                a.append(r[l] + '=' * n)
    return ''.join(a)


def z(x):
    q = []
    for i in range(len(x)):
        o = ord(x[i]) ^ i
        q.append(o)
    return q

if __name__ == '__main__':
    hexa = [
        81,
        49,
        72,
        89,
        97,
        52,
        101,
        112,
        89,
        94,
        98,
        109,
        90,
        74,
        105,
        119,
        69,
        32,
        43,
        80,
        90,
        82,
        92,
        77,
        64,
        41,
        46,
        108,
        74,
        91,
        39,
        84,
        68,
        117,
        116,
        118,
        124,
        21,
        96,
        65,
        124,
        67,
        104,
        82,
        120,
        121,
        124,
        92,
        104,
        3,
        120,
        113,
        101,
        91,
        90,
        81,
        109,
        11,
        14,
        11,
        111,
        71,
        112,
        6]
    s = input('>>')
    m = s.encode()
    t = b(m)
    u = z(t)
    if ''.join((lambda .0: for v in .0:
chr(v))(u)) == ''.join((lambda .0: for v in .0:
chr(v))(hexa)):
        print('Correct!')
    else:
        print('Wrong')
