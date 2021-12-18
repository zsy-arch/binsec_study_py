import base64

def encrypt(s, n):
    for i in range(1, 11):
        for j in range(0, n):
            if n % i != 0:
                s[j] ^= i + j
            else:
                s[j] ^= (j % i) + j
            s[j] &= 0xff

s3cret = list(base64.b64decode('7G5d5bAy+TMdLWlu5CdkMTlcJnwkNUgb2AQL3CcmPpVf6DAp72scOSlb'))
print(s3cret)
encrypt(s3cret, len(s3cret))
print(''.join(list(map(chr,s3cret))))

