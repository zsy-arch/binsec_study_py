def my_encode(s, b64chars):
    import base64
    my_base64chars = b64chars
    std_base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    s = s.translate(str.maketrans(my_base64chars, std_base64chars))
    data = base64.b64encode(bytes(s, 'utf-8'))
    print(data)
    return data
