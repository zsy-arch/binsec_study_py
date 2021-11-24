from can_book.b64decode import my_encode

timestamp = list('1633831810')
fake = list('flag{this_is_fake_flag}')
encrypted_ts = my_encode('1633831810', 'abcdefghijklmnopqrstuvwxyz0123456789+/ABCDEFGHIJKLMNOPQRSTUVWXYZ')
xored_key = []

for i in range(16):
    xored_key.append(encrypted_ts[i] ^ ord(fake[i]))

