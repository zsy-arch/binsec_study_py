t = [
    0x13,
    0x13,
    0x11,
    0x17,
    0x12,
    0x10,
    0x48,
    0x45
]

"""
[
0x13,
0x13,
0x11,
0x17,
0x12,
0x10,
0x48,
0x45
]
"""


def encrypt(a):
    if a[0] == 'r':
        a[0] = chr(ord(a[1]) ^ ord(a[0]))
        a[1] = chr(ord(a[2]) ^ ord(a[1]))
        a[2] = chr(ord(a[3]) ^ ord(a[2]))
        a[3] = chr(ord(a[4]) ^ ord(a[3]))
        a[4] = chr(ord(a[5]) ^ ord(a[4]))
        a[5] = chr(ord(a[6]) ^ ord(a[5]))
        a[6] = chr(ord(a[7]) ^ ord(a[6]))
        a[7] = chr(ord(a[8]) ^ ord(a[7]))
    print(a)


def decrypt(a) -> list:
    a[7] = ((a[8]) ^ (a[7]))
    a[6] = ((a[7]) ^ (a[6]))
    a[5] = ((a[6]) ^ (a[5]))
    a[4] = ((a[5]) ^ (a[4]))
    a[3] = ((a[4]) ^ (a[3]))
    a[2] = ((a[3]) ^ (a[2]))
    a[1] = ((a[2]) ^ (a[1]))
    a[0] = ((a[1]) ^ (a[0]))
    return a


# encrypt(list('r12345678'))

for end in range(0x80):
    res = decrypt(t + [end])
    if res[0] == ord('r'):
        print(res)
        for rr in res:
            print(chr(rr), end='')
