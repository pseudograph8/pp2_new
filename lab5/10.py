'''
10. Write a Python program to convert a given camel case string to snake case.
'''
import re
camel = input().lower()
snake = re.sub(r'[\s-]', '_', camel)

print(snake)
