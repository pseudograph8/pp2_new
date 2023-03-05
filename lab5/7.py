"""
7. Write a python program to convert snake case string to camel case string.
"""

import re

snake = input().lower().title()

camel = re.sub(r"(_|-)+", " ", snake).replace(" ", "")

print(camel)

