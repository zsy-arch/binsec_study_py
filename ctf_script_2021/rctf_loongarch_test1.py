def xor_bytes(a, b):
    res = []
    for i in range(len(a)):
        res.append(a[i] ^ b[i])
    return res


def bitrev_d(a):
    return a[::-1]


def bitrev_8b(a):
    res = []
    for i in range(0, 64, 8):
        res += a[i:i + 8][::-1]
    return res


def bytepick_d(a, b, k):
    return b[8 * (k):64] + a[0:8 * (k)]


output_path = r"E:\CTF\rctf2021\3d05b37b23074a2ea63baafcc94ac68f\output"
f = open(output_path, 'rb')
buf = f.read()
xor1 = []
xor2 = []

for i in range(4):
    xor1.append(list(buf[i * 8: (i + 1) * 8]))

for i in range(4, 8):
    xor2.append(list(buf[i * 8: (i + 1) * 8]))

t = [xor_bytes(i, [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff]) for i in xor2]

s = [bitrev_8b(i) for i in t]

u = [
    bytepick_d(s[2], s[1], 5),
    bytepick_d(s[0], s[2], 5),
    bytepick_d(s[3], s[0], 5),
    bytepick_d(s[1], s[3], 5)
]

v = [bitrev_d(i) for i in u]

w = [xor_bytes(v[i], xor1[i]) for i in range(len(v))]

for i in w:
    for j in i:
        print(chr(j), end=' ')
