def decrypt_pyc():
    import zlib
    import tinyaes

    pyc_path = r"E:\CTF\ciscn\2021\imnotavirus\main.exe_extracted\PYZ-00.pyz_extracted\sign.pyc.encrypted"
    with open(pyc_path, 'rb') as f:
        buf = f.read()
    iv = buf[:16]
    data = buf[16:]
    key = b'NoneOfUrBusiness'

    cipher = tinyaes.AES(key, iv)
    output = cipher.CTR_xcrypt_buffer(data)

    output = zlib.decompress(output)

    with open(r"E:\CTF\ciscn\2021\imnotavirus\main.exe_extracted\PYZ-00.pyz_extracted\sign.pyc", "wb") as f:
        f.write(iv + output)


def get_binary():
    import ctypes, base64, hashlib, ast

    def aaa(ttt, ggg):
        ggg = hashlib.md5(ggg).hexdigest()
        ttt = base64.b64decode(ttt)
        result = b''
        ggg_len = len(ggg)
        box = list(range(256))
        j = 0
        for i in range(256):
            j = (j + box[i] + ord(ggg[(i % ggg_len)])) % 256
            box[i], box[j] = box[j], box[i]
        else:
            i = j = 0
            for iii in ttt:
                i = (i + 1) % 256
                j = (j + box[i]) % 256
                box[i], box[j] = box[j], box[i]
                k = iii ^ box[((box[i] + box[j]) % 256)]
                result += bytes([k])
            else:
                return result

    def main():
        ctypes.windll.kernel32.VirtualAlloc.restyle = ctypes.c_uint32
        b = 'pB2M/eG2iz1pB4kej4yXXCYvTFV3b/6NDPvMVc+iOs2QwI7Tg7QcItIK6KtB5seaZhd67NGYh6xyMPAocLhd0NeJhweg5/rsEuYnzxFxqMrysaizRAiD6HQhe50rwF5UnByay04giUxuLxy6zL8me5sAQqaUAuCv0c1EsDKBxv1B1zV8MEDav5bkgsTd2t3X3Jt0+lfGKk98bxg1FIXoUhtyZjhV489SpMi+Gzs2+/zaZ0d7p12KoppTYPNs3sj9l74Q8EJPYIAecUEnMSmKDF7yPaKIFloCdW5ghVaSeiaskr5OzfzfeccpvRPevL7PW9uW1R8WmcW2oWjN9aWsinwG2Gk1B7JPa+HusBGpIxxSQhK0wBrEjQpYlIMC7fTpFZca373+p/A2oXuaXqfmOoWtE62JCM74tWqZFrSWyLdnu1/vHaClrzcdzpHLum9shEOcNHYi88Dj11mYufJxH/sEx0CBtWkTCHwEhxVs1sYkGBHlDFUpFbfpY0UagbyPJdq+bmXBdmLKEhJ/M/2cCjmsjuma6IKvo+riA7/B8+T3GB06x31G5tibi3rJMDb4bVWBswzI3gg06mc4Q9EW5dQ4+/SRKbVoYhAfbGKlBeuxSIARKzSAuJPlfm+dmJ6pHx9a4qek2UIEKr4zxA0bSMALoYOSETDF1JWZX+K0HEJLY/hXajmzq5qSTX0EAKBLJtIPkJ0e+XsaQCXyhy4Cg8mYNlQGIORNo5vyNe4QPAD8d3GKr/PZnEMwJ5WsgyoSBOGDke4PGUJd70thEyGHKN9QfTXWknC8HBZdcEojvtC3Prj7LlxXI6y8uZ7ie/1HltGogj3EsUkqU0d3WDuBPZec1Tzj/7Vs44MFGRjEJ0IuSA0U0vOCShyeHUB23qhrXqODsrO/t+s/Zohmd2H0xS46qdoquQj8L1RY2fCt3H0US3Wffk0FKf7qYboKeW/7vlkOYlchgP/HXf0Mfo5gBXhJg3e9jGJ8K5J0gt6Zra9dhPINGgekDMIoxXE='
        c = aaa(b, 'blackhand'.encode('utf-8'))
        c = ast.literal_eval("b'" + c.decode().strip() + "'")
        bc = bytearray(c)
        with open('ciscn_2021_imnotvirus_b64_1', 'wb') as f:
            i = 0x3D
            while i < len(c):
                bc[i] ^= 0x77
                i += 1
            f.write(bc)

    main()


def get_flag():
    bc = bytearray(b'J\x04`~~s Q"Y!C [j\x05e\x06aB&N#B!E Qp\\ S{\x05{\x05{\x05')
    for i in range(0, len(bc), 2):
        bc[i] ^= 0x13
        bc[i + 1] ^= 0x37
    print(bc)


get_flag()
