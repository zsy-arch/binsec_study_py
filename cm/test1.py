s = [0x89, 0x2c, 0xa5, 0x78, 0x1d, 0x7d, 0xe2, 0x56]
flag = [73]
sum = flag[0]

for i in range(1, 9):
    for t in range(0x80):
        temp = sum
        sum += t % (240 - i)
        if (sum + t) % 255 == s[i - 1]:
            flag.append(t)
            break
        sum = temp

for f in flag:
    print(chr(f), end='')
