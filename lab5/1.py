"""
1. Write a Python program that matches a string that has an `'a'` 
followed by zero or more `'b'`'s.
"""
import re

str = input()
x = re.search('a.*b', str)

if (x):
  print("Yes, there is at least one match!")
  print(x)
else:
  print("No match")