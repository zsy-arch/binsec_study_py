def test1():
    with open(r"E:\CTF\ByteCTF_2021\languages_binding\6931aec18dcb45b2826f3f0864a218d4\new_lang_script.out", 'rb') as f:
        data = f.read()

    for i in range(0xff):
        origin = []
        for j in range(len(data)):
            origin.append(data[j] ^ i)
        origin = bytes(origin)
        if b'_ENV' in origin:
            print(i)

    # with open(r"E:\CTF\ByteCTF_2021\languages_binding\6931aec18dcb45b2826f3f0864a218d4\origin.luac", 'wb') as f:
    #     f.write(bytes(origin))


def test2():
    target = ord('.')
    for i in range(0xff):
        if i ^ 0xff == target:
            print(i)


test1()
