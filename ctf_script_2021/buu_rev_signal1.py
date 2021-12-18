vm_codes = [0x0A, 0x4, 0x10, 0x8, 0x3, 0x5, 0x1, 0x4, 0x20, 0x8, 0x5, 0x3, 0x1, 0x3, 0x2, 0x8, 0x0B, 0x1, 0x0C, 0x8,
            0x4, 0x4, 0x1, 0x5, 0x3, 0x8, 0x3, 0x21, 0x1, 0x0B, 0x8, 0x0B, 0x1, 0x4, 0x9, 0x8, 0x3, 0x20, 0x1, 0x2,
            0x51, 0x8, 0x4, 0x24, 0x1, 0x0C, 0x8, 0x0B, 0x1, 0x5, 0x2, 0x8, 0x2, 0x25, 0x1, 0x2, 0x36, 0x8, 0x4, 0x41,
            0x1, 0x2, 0x20, 0x8, 0x5, 0x1, 0x1, 0x5, 0x3, 0x8, 0x2, 0x25, 0x1, 0x4, 0x9, 0x8, 0x3, 0x20, 0x1, 0x2, 0x41,
            0x8, 0x0C, 0x1, 0x7, 0x22, 0x7, 0x3F, 0x7, 0x34, 0x7, 0x32, 0x7, 0x72, 0x7, 0x33, 0x7, 0x18, 0x7,
            0x0FFFFFFA7, 0x7, 0x31, 0x7, 0x0FFFFFFF1, 0x7, 0x28, 0x7, 0x0FFFFFF84, 0x7, 0x0FFFFFFC1, 0x7, 0x1E, 0x7,
            0x7A, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]

i = 0

while i < 0x72:
    if vm_codes[i] == 1:
        print("""Str[j_v6 + 100] = v4;
    ++i_v9;
    ++j_v6;
    ++m_v8;""")
        i += 1
    elif vm_codes[i] == 2:
        print("""v4 = a1[i_v9 + 1] + Str[m_v8];
    i_v9 += 2;""")
        i += 2
    elif vm_codes[i] == 3:
        print("""v4 = Str[m_v8] - LOBYTE(a1[i_v9 + 1]);
    i_v9 += 2;""")
        i += 2
    elif vm_codes[i] == 4:
        print("""v4 = a1[i_v9 + 1] ^ Str[m_v8];
    i_v9 += 2;""")
        i += 2
    elif vm_codes[i] == 5:
        print("""v4 = a1[i_v9 + 1] * Str[m_v8];
    i_v9 += 2;""")
        i += 2
    elif vm_codes[i] == 6:
        print("    ++i_v9;")
        i += 1
    elif vm_codes[i] == 7:
        print("""if ( Str[v7 + 100] != a1[i_v9 + 1] )
{
  printf("what a shame...");
  exit(0);
}
    ++v7;
    i_v9 += 2;""")
        i += 2
    elif vm_codes[i] == 8:
        print("""Str[v5] = v4;
    ++i_v9;
    ++v5;""")
        i += 1
    elif vm_codes[i] == 10:
        print("""read(Str);
    ++i_v9;""")
        i += 1
    elif vm_codes[i] == 11:
        print("""v4 = Str[m_v8] - 1;
    ++i_v9;""")
        i += 1
    elif vm_codes[i] == 12:
        print("""v4 = Str[m_v8] + 1;
    ++i_v9;""")
        i += 1
    else:
        print(i)