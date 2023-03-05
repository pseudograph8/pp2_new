"""
3. Write a Python program to find sequences of lowercase letters 
joined with a underscore.
"""
import re 

str = input()

x = re.findall('^[a-z]+_[a-z]+$', str)

print(x)