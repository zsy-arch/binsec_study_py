s = '~}|{zyxwvutsrqponmlkjihgfedcba`_^]\[ZYXWVUTSRQPONMLKJIHGFEDCBA@?>=<;:9876543210/.-,+*)(\x27&%$# !"'
t = '*F\'\\"N,\"(I?+@'
u = [s.find(tt) + 1 for tt in t]

for uu in u:
    print(chr(uu), end='')