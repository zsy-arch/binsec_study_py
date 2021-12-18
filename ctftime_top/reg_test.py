a = """
a: 1
b: 2
asdas
"""

import re

c = re.compile(r'[a-z]: (\d+)')
s = c.findall(a)
print(s)