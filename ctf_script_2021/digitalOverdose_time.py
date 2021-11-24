from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


data = [
    0xA8,
    0x37,
    0xF4,
    0xC7,
    0x52,
    0x3C,
    0x28,
    0x11,
    0x69,
    0x76,
    0xEC,
    0x98,
    0xD,
    0x12,
    0x92,
    0xDA,
    0xC8,
    0x48,
    0xBC,
    0x2,
    0xFA,
    0xFA,
    0xD2,
    0x7B,
    0x9C,
    0x47,
    0xDB,
    0x82,
    0x69,
    0xCF,
    0xB0,
    0x8F
]

iv = [
    b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F\x10'
]

a = 0

while True:
    aes = AES.new(bytes(str(a), 'ascii').zfill(16), AES.MODE_CBC,
                  b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F\x10')
    try:
        pt = unpad(aes.decrypt(bytes(data)), AES.block_size)
    except Exception as e:
        continue
    print(str(pt) + " " + str(a))
    a += 1
