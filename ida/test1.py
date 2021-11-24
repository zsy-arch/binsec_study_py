import ida_bytes
import struct

des = 0x8000000
ins_addr = 0x405010
sizes_addr = 0x405220


def get_patch_addr(a2, a3):
    t = ida_bytes.get_dword(0x4052A8 + a2 * 4)
    v5 = t % 0x10
    v4 = t >> 4
    if v4 == 1:
        return 4 * (v5 + 2 * a3) + 0x405648
    if v4 == 2:
        return 4 * v5 + 0x405000
    if v4 == 3:
        return 0x405748


def patch_addr(ori, addr):
    if addr is None: return ori
    for i in range(len(ori)):
        if ori[i] == 0:
            return ori[:i] + struct.pack('I', addr) + ori[i + 4:]
    return ori


size = ida_bytes.get_dword(sizes_addr)
v14 = 0
while size != 0:
    ins = ida_bytes.get_bytes(ins_addr, size)
    pa = get_patch_addr(v14, 0)
    res = patch_addr(ins, pa)
    ida_bytes.patch_bytes(des, res)
    des += len(res)

    sizes_addr += 4
    size = ida_bytes.get_dword(sizes_addr)
    v14 += 1
    ins_addr += 16
