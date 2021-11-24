import base64

fp1 = "E:\CTF\天津2021\决赛\misc\sgcc\secret.txt"
file1 = open(fp1, 'r')
text = file1.read()
decrypt1 = base64.b64decode(text)
print(decrypt1)
decrypt2 = base64.b64decode(decrypt1)
file2 = open("E:\CTF\天津2021\决赛\misc\sgcc\secret.png", 'wb')
file2.write(decrypt2)
