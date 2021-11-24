s = list('fkduohv-d-jhvfklfnwhu-wr-gdun-dqjho-01.oodev')
d = {}

for ss in s:
    d[ss] = 0

for ss in s:
    d[ss] += 1

for x in range(-0xff, 0xff):
    t = s.copy()
    for i in range(len(t)):
        if t[i] in ['-', '0', '1', '.']:
            continue
        t[i] = chr(ord(t[i]) - x)
    print(''.join(t))

print(s)