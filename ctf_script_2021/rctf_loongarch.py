def qword2bit(a):
    re = []
    for i in range(64):
        re.append(a%2)
        a >>= 1
    return re[::-1]

def bit2qword(a):
    re = ""
    for i in a:
        re += str(i)
    return int(re,2)

def bitrev_8b(a):
    re = []
    for i in range(0,64,8):
        re += a[i:i+8][::-1]
    return re

def bytepick_d(a,b,n):
    return b[8*(n):64]+a[0:8*(n)]

def bitrev_d(a):
    return a[::-1]

xor1 = [0x8205f3d105b3059d,0xa89aceb3093349f3,0xd53db5adbcabb984,0x39cea0bfd9d2c2d4]
xor2 = [0xc513455508290500,0x6d621abb30b918,0xbc555b9f4c6f86a1,0x50d78ad181a626d]

a = [i^0xffffffffffffffff for i in xor2]

b = [qword2bit(i) for i in a]

c = [bitrev_8b(i) for i in b]

d = [bytepick_d(c[2],c[1],5),
    bytepick_d(c[0],c[2],5),
    bytepick_d(c[3],c[0],5),
    bytepick_d(c[1],c[3],5)]

e = [bitrev_d(i) for i in d]

f = [bit2qword(i) for i in e]

g = [f[i]^xor1[i] for i in range(4)]

for i in g:
    for j in range(8):
        print(chr(i&0xff),end='')
        i >>= 8

print()