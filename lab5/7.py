"""
7. Write a python program to convert snake case string to camel case string.
"""

import re

snake = input()
snake1 = snake[0].lower() + snake[1:].lower().title()

camel = re.sub(r"(_|-)+", " ", snake1).replace(" ", "")

print(camel)

