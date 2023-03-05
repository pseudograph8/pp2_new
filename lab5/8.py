'''
8. Write a Python program to split a string at uppercase letters.
'''
import re
str = input()

x = re.split(r'[A-Z]', str)
print(x)