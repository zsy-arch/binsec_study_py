v13 = [
    0x72, 0x202, 0x13, 0x13
]

v5 = 288407067 & 0xffffffff
v3 = 1668576323 & 0xffffffff
v7 = (1640531527 * -32) & 0xffffffff
print(v7)
for i in range(32):
    v8 = (v7 >> 2) & 3
    v3 -= ((v7 ^ v5) + (v5 ^ v13[v8 ^ 1])) ^ (((16 * v5) ^ (v5 >> 3)) + ((v5 >> 5) ^ (4 * v5)))
    v3 = v3 & 0xffffffff
    v6 = v3
    v5 -= ((v7 ^ v3) + (v6 ^ v13[v8])) ^ (((16 * v6) ^ (v3 >> 3)) + ((v6 >> 5) ^ (4 * v3)))
    v5 = v5 & 0xffffffff
    v7 += 1640531527
    v7 = v7 & 0xffffffff

print(hex(v5 & 0xffffffff))
print(hex(v3 & 0xffffffff))