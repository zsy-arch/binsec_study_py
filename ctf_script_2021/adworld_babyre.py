"""from idaapi import *

start_addr = 0x600B00
patch_size = 0xB5

for i in range(patch_size):
    value = get_byte(start_addr + i)
    patch_byte(start_addr + i, (value ^ 0x0C) & 0xff)"""

flag = [0x66, 0x6D, 0x63, 0x64, 0x7F, 0x6B, 0x37, 0x64, 0x3B, 0x56, 0x60, 0x3B, 0x6E, 0x70]

for i in range(len(flag)):
    flag[i] = (flag[i] ^ i)

flag = [chr(ff) for ff in flag]
print(''.join(flag))